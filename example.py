from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QFormLayout, QGroupBox, QScrollArea, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self, val):
        super().__init__()
        self.title = "PyQt5 QScroll Area"
        self.left = 200
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "home.png"

        self.setWindowTitle(self.title)
        self.windowIcon()
        self.setGeometry(self.left, self.top, self.width, self.height)

        formLayout = QFormLayout()
        groupBox = QGroupBox("This is Group Box")

        labelList = []
        buttonList = []

        for i in range(val):
            labelList.append(QLabel(f"Label №{i}"))
            buttonList.append(QPushButton("Click me!"))
            formLayout.addRow(labelList[i], buttonList[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)

        self.show()


App = QApplication(sys.argv)
window = Window(40)
sys.exit(App.exec())
