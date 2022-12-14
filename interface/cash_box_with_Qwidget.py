# -*- coding: utf-8 -*-

# Form implementation generated from reading cash file 'cash_box_with_Qwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from numpy import random


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.queue = 0
        self.mean = []
        self.timer = None
        self.number_Checkout = None
        self.maintenance_time = 0
        self.list_maintenance_time = []
        self.all_queue = 0
        self.time_1 = 1
        self.time_2 = 3

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(596, 170)
        Form.setStyleSheet("background-color: rgb(211, 211, 211);\n")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.number_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.number_label.setFont(font)
        self.number_label.setObjectName("number_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.number_label)
        self.number = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.number.setFont(font)
        self.number.setObjectName("number")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.number)
        self.queue_length_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.queue_length_label.setFont(font)
        self.queue_length_label.setObjectName("queue_length_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.queue_length_label)
        self.queue_length = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.queue_length.setFont(font)
        self.queue_length.setObjectName("queue_length")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.queue_length)
        self.avarage_time_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.avarage_time_label.setFont(font)
        self.avarage_time_label.setObjectName("avarage_time_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.avarage_time_label)
        self.avarage_time = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.avarage_time.setFont(font)
        self.avarage_time.setObjectName("avarage_time")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.avarage_time)
        self.workload_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.workload_label.setFont(font)
        self.workload_label.setObjectName("workload_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.workload_label)
        self.workload = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.workload.setFont(font)
        self.workload.setObjectName("workload")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.workload)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setProperty("value", 11)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.progressBar)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.service_time_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.service_time_label.setFont(font)
        self.service_time_label.setObjectName("service_time_label")
        self.verticalLayout.addWidget(self.service_time_label)
        self.service_time_1 = QtWidgets.QSpinBox(self.frame_2)
        self.service_time_1.setMinimum(1)
        self.service_time_1.setObjectName("service_time_1")
        self.verticalLayout.addWidget(self.service_time_1)
        self.service_time_2 = QtWidgets.QSpinBox(self.frame_2)
        self.service_time_2.setMinimum(3)
        self.service_time_2.setObjectName("service_time_2")
        self.verticalLayout.addWidget(self.service_time_2)
        self.set_time_button = QtWidgets.QPushButton(self.frame_2)
        self.set_time_button.setObjectName("set_time_button")
        self.verticalLayout.addWidget(self.set_time_button)
        self.interval = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.interval.setFont(font)
        self.interval.setObjectName("interval")
        self.verticalLayout.addWidget(self.interval)
        self.horizontalLayout.addWidget(self.frame_2)

        # print(self.number_Checkout)
        self.number.setText(str(self.number_Checkout))

        # self.previous_queue = self.queue
        # if self.queue != self.previous_queue:
        self.queue_length.setText(str(self.queue))

        # d = len(self.list_maintenance_time) / self.all_queue
        # self.avarage_time.setText(str(d))

        # self.service_time_1.valueChanged.connect(self.change_time_1)
        # self.service_time_2.valueChanged.connect(self.change_time_2)
        self.set_time_button.clicked.connect(self.time_changed)
        # self.time_1 = self.service_time_1.value()
        # self.time_2 = self.service_time_2.value()
        # self.maintenance_time = random.randint(self.time_1, self.time_2)
        # self.mean.append(self.maintenance_time)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.number_label.setText(_translate("Form", "???"))
        # self.number.setText(_translate("Form", "TextLabel"))
        self.queue_length_label.setText(_translate("Form", "?????????? ??????????????"))
        # self.queue_length.setText(_translate("Form", "TextLabel"))
        self.avarage_time_label.setText(_translate("Form", "?????????????? ??????????"))
        self.avarage_time.setText(_translate("Form", "TextLabel"))
        self.workload_label.setText(_translate("Form", "??????????????????????????"))
        self.workload.setText(_translate("Form", "TextLabel"))
        self.service_time_label.setText(_translate("Form", "?????????? ???????????????????????? (??)"))
        self.set_time_button.setText(_translate("Form", "??????????????????"))
        self.interval.setText(_translate("Form", "TextLabel"))

    def change_time_1(self):
        self.time_1 = self.service_time_1.value()

    def change_time_2(self):
        self.time_2 = self.service_time_2.value()

    def time_changed(self):
        self.time_1 = self.service_time_1.value()
        self.time_2 = self.service_time_2.value()
        self.interval.setText(f'[{self.time_1};{self.time_2}]')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
