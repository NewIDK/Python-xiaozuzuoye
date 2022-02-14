import os

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication

import sys
from detect import run
from PyQt5.QtGui import QIcon
run_dict = {
    'weights': 'kid.pt',
    'source': 0,
    'imgsz': [640, 640],
    'conf_thres': 0.70,
    'iou_thres': 0.60,
    'max_det': 10,
    'device': '0',
    'view_img': False,
    'save_txt': False,
    'save_conf': False,
    'save_crop': False,
    'nosave': True,
    'classes': None,
    'agnostic_nms': False,
    'augment': False,
    'visualize': False,
    'update': False,
    'project': 'runs/detect',
    'name': 'exp',
    'exist_ok': False,
    'line_thickness': 3,
    'hide_labels': False,
    'hide_conf': False,
    'half': False,
}

run_dict_file = {
    'weights': 'kid.pt',
    'source': 'data/images',
    'imgsz': [640, 640],
    'conf_thres': 0.70,
    'iou_thres': 0.60,
    'max_det': 10,
    'device': '0',
    'view_img': False,
    'save_txt': False,
    'save_conf': False,
    'save_crop': False,
    'nosave': False,
    'classes': None,
    'agnostic_nms': False,
    'augment': False,
    'visualize': False,
    'update': False,
    'project': 'runs/detect',
    'name': 'exp',
    'exist_ok': False,
    'line_thickness': 3,
    'hide_labels': False,
    'hide_conf': False,
    'half': False,
}

class WindowClass(QWidget):
    def __init__(self,parent=None):
        super(WindowClass, self).__init__(parent)
        self.setWindowTitle('口罩佩戴检测__by_Kid')
        self.setWindowIcon(QIcon('ico.jpg'))
        self.btn_1 = QPushButton("从摄像头开始")
        self.btn_2 = QPushButton("从文件开始")
        self.btn_3 = QPushButton("显示结果")
        self.btn_4 = QPushButton("退出")


        self.btn_1.setCheckable(True)
        self.btn_1.toggle()

        self.btn_1.clicked.connect(lambda :self.wichBtn(self.btn_1))
        self.btn_2.clicked.connect(lambda :self.wichBtn(self.btn_2))
        self.btn_3.clicked.connect(lambda :self.wichBtn(self.btn_3))
        self.btn_4.clicked.connect(lambda :self.wichBtn(self.btn_4))

        self.resize(300,300)
        layout=QVBoxLayout()
        layout.addWidget(self.btn_1)
        layout.addWidget(self.btn_2)
        layout.addWidget(self.btn_3)
        layout.addWidget(self.btn_4)

        self.setLayout(layout)


    def wichBtn(self,btn):
        print("点击的按钮是：" , btn.text())
        if btn.text() == '退出':
            sys.exit()
        if btn.text() == '从摄像头开始':
            run(**run_dict)
        if btn.text() == '显示结果':
            path = os.getcwd() + r'\runs\detect'
            os.system("start explorer %s" %path)
        if btn.text() == '从文件开始':
            run(**run_dict_file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowClass()
    win.show()
    sys.exit(app.exec_())