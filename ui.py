from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1128, 873)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 60, 850, 790))
        self.label.setStyleSheet("\n"
                                  "border-image: url(:/img/img/21.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(720, 140, 211, 51))
        self.frame.setStyleSheet("QPushButton{\n"
                                 "    border:none;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "    padding-bottom:5px;\n"
                                 "}")

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(280, 162, 161, 21))
        self.progressBar.setStyleSheet("#progressBar{\n"
                                        "    background:transparent;\n"
                                        "    border-radius: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "#progressBar::chunk {\n"
                                        "    border-radius: 5px;\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(222, 220, 245), stop:1 rgb(215, 248, 247));\n"
                                        "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setTextVisible(False)  # 不显示数字

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(530, 710, 101, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background:transparent;\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "border:2px solid rgb(222, 221, 246);")
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 210, 640, 480))
        self.label_2.setStyleSheet("border-radius:45px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.showMinimized) # type: ignore
        self.pushButton_2.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "顾某"))
        self.lineEdit.setPlaceholderText(_translate("Form", "距离设置"))
