import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from ui import Ui_Form  # UI
import qrc  # qrc生成的py #样式表
import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import pygame
import threading
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("com.example.myapp")
class guWindow(QWidget):
    close_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.gu = Ui_Form()
        self.gu.setupUi(self)
        self.gu.lineEdit.returnPressed.connect(self.gumou)  # lineEdit回车运行
        self.video_label = self.gu.label_2# 2 QLabel2
        self.user_name_qwidget = self.gu.lineEdit
        self.progress_bar = self.gu.progressBar  #进度条
        self.setWindowOpacity(0.90)  # 设置窗口透明度
        self.setWindowFlag(Qt.FramelessWindowHint)  # 去除边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 去除白色背景
        self.offset = QPoint()  # 记录鼠标按下的初始位置
        self.close_signal.connect(self.closeEvent)

    def closeEvent(self, event):
        # 关闭窗口时发送信号
        self.stop_capture()

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)  # 移动窗口位置

    def gumou(self):  # 按钮绑定的函数 功能
        s = self.user_name_qwidget.text()
        self.user_name_qwidget.clear()
        try:
            distance_threshold = float(s)  # 将用户输入的文本转换为浮点数作为距离阈值
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        cap = cv2.VideoCapture(0)
        self.detector = FaceMeshDetector(maxFaces=1)
        pygame.mixer.init()
        # 加载音频文件
        pygame.mixer.music.load('7359.wav')  # 靠的太近啦
        self.capture_active = True

        def play_audio():
            pygame.mixer.music.play(1)
            while pygame.mixer.music.get_busy():
                continue

        while self.capture_active:
            success, img = cap.read()
            img, faces = self.detector.findFaceMesh(img, draw=False)
            if faces:
                face = faces[0]
                pointLeft = face[145]
                pointRight = face[374]
                w, _ = self.detector.findDistance(pointLeft, pointRight)
                W = 6.5
                f = 600  # 焦距
                d = (W * f) / w
                print(d)
                # 设置距离颜色
                if d < distance_threshold:  # 使用用户输入的距离阈值作为判断条件
                    print("过近提醒")
                    # 检查是否正在播放音频
                    if not pygame.mixer.music.get_busy():
                        # 使用线程播放音频，避免阻塞主程序
                        audio_thread = threading.Thread(target=play_audio)
                        audio_thread.start()
                    text_color = (255, 0, 0)  # 红色
                else:
                    text_color = (0, 0, 255)  # 蓝色
                # Update the QProgressBar value
                self.progress_bar.setValue(int(d))
                # 将 Depth 文本显示为汉语
                pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                draw = ImageDraw.Draw(pil_img)
                font = ImageFont.truetype("msyh.ttc", 36)  # 使用微软雅黑字体，大小为36
                draw.text((face[10][0] - 95, face[10][1] - 5), f'距离:{int(d)}厘米', font=font, fill=text_color)
                img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            h, w, c = img.shape
            bytesPerLine = c * w
            if c == 3:  # 如果颜色通道为3（BGR）
                q_img = QtGui.QImage(img.data, w, h, bytesPerLine, QtGui.QImage.Format_BGR888)
            else:  # 如果颜色通道为4（BGRA）
                q_img = QtGui.QImage(img.data, w, h, bytesPerLine, QtGui.QImage.Format_BGRA8888)
            # Convert QImage to QPixmap
            pixmap = QtGui.QPixmap.fromImage(q_img)
            # Display QPixmap on QLabel
            self.video_label.setPixmap(pixmap)
            self.video_label.setScaledContents(True)
            self.video_label.update()
            cv2.waitKey(1)

    def stop_capture(self):
        self.capture_active = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = QtGui.QIcon(':/img/img/ai.ico')
    app.setWindowIcon(icon)
    # 创建可拖动窗口实例
    ui = guWindow()  # 函数
    # 显示窗口
    ui.show()
    # 启动应用程序事件循环
    sys.exit(app.exec_())
