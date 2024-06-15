#这个代码仅有算法没有UI
import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import pygame
import threading
from PIL import Image, ImageDraw, ImageFont
import numpy as np
# 初始化pygame.mixer
pygame.mixer.init()
# 加载音频文件
pygame.mixer.music.load('7359.wav')  # 靠的太近啦
# 设置摄像头
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
# 定义播放音频的函数
def play_audio():
    pygame.mixer.music.play(1)
    while pygame.mixer.music.get_busy():
        continue
# 开始检测人脸
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.5
        f = 600  #焦距
        d = (W * f) / w
        print(d)
        # 设置距离颜色
        if d < 35:
            print("过近提醒")
            # 检查是否正在播放音频
            if not pygame.mixer.music.get_busy():
                # 使用线程播放音频，避免阻塞主程序
                audio_thread = threading.Thread(target=play_audio)
                audio_thread.start()
            text_color = (255, 0, 0)  # 红色
        else:
            text_color = (0, 0, 255)  # 蓝色
        # 将 Depth 文本显示为汉语
        pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_img)
        font = ImageFont.truetype("msyh.ttc", 36)  # 使用微软雅黑字体，大小为36
        draw.text((face[10][0] - 95, face[10][1] - 5), f'距离:{int(d)}厘米', font=font, fill=text_color)
        img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    cv2.imshow("Distance recognition", img)  # 窗口名只能是英文
    cv2.waitKey(1)
