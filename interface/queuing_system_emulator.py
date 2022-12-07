# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queuing_system_emulator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel

from interface.cash_box_with_Qwidget import Ui_Form


class Ui_queuing_system_emulator(QtWidgets.QWidget):
    def setupUi(self, queuing_system_emulator):
        queuing_system_emulator.setObjectName("queuing_system_emulator")
        queuing_system_emulator.resize(910, 500)
        queuing_system_emulator.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.centralwidget = QtWidgets.QWidget(queuing_system_emulator)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Frame with buttons, lables and spinbox
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        # Arrival time
        self.arrival_time = QtWidgets.QSpinBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.arrival_time.setFont(font)
        self.arrival_time.setMinimum(1)
        self.arrival_time.setObjectName("arrival_time")
        self.gridLayout.addWidget(self.arrival_time, 2, 2, 1, 1)

        # People label
        self.people_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.people_label.setFont(font)
        self.people_label.setObjectName("people_label")
        self.gridLayout.addWidget(self.people_label, 1, 0, 1, 1)

        # Stop button
        self.stop_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 3, 2, 1, 1)

        # Checkout label
        self.checkout_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkout_label.setFont(font)
        self.checkout_label.setObjectName("checkout_label")
        self.gridLayout.addWidget(self.checkout_label, 0, 0, 1, 1)

        # Arrival time label
        self.arrival_time_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.arrival_time_label.setFont(font)
        self.arrival_time_label.setObjectName("arrival_time_label")
        self.gridLayout.addWidget(self.arrival_time_label, 2, 0, 1, 1)

        # Checkout
        self.checkout = QtWidgets.QSpinBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.checkout.setFont(font)
        self.checkout.setMinimum(3)
        self.checkout.setObjectName("checkout")
        self.gridLayout.addWidget(self.checkout, 0, 2, 1, 1)

        # People
        self.people = QtWidgets.QSpinBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.people.setFont(font)
        self.people.setMinimum(1)
        self.people.setObjectName("people")
        self.gridLayout.addWidget(self.people, 1, 2, 1, 1)

        # Start button
        self.start_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 3, 0, 1, 2)
        self.horizontalLayout.addWidget(self.frame)

        # Scrollarea
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: rgb(192, 192, 192);")
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 544, 476))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.scrollArea.raise_()
        self.frame.raise_()
        queuing_system_emulator.setCentralWidget(self.centralwidget)

        self.checkouts = []
        self.clock_1 = []
        self.clock_2 = []

        # Change in spinbox
        for i in range(0, self.checkout.value()):
            Form = QtWidgets.QWidget()
            cash = Ui_Form()
            cash.number_Checkout = i + 1

            cash.timer = QtCore.QTimer(self)
            cash.timer.timeout.connect(lambda inter=i: self.removing_people_from_queue(inter))

            t_1 = cash.time_1
            self.clock_1.append(t_1)
            t_2 = cash.time_2
            self.clock_2.append(t_2)
            cash.maintenance_time = random.randint(self.clock_1[i], self.clock_2[i])
            # print("cash.maintenance_time: ", cash.maintenance_time)

            cash.timer.setInterval((cash.maintenance_time + 1) * 1000)
            cash.timer.start()
            self.checkouts.append(cash)

            cash.setupUi(Form)
            self.verticalLayout.addWidget(Form)
            # self.checkouts.append(ui)
            # print("print(len(self.checkouts)): ", len(self.checkouts))

        self.scrollAreaWidgetContents.setLayout(self.verticalLayout)

        self.previous_value_of_the_number_of_cash_registers = self.checkout.value()
        self.checkout.valueChanged.connect(self.change_the_number_of_checkouts)

        # Change in arrival_time spinbox
        # arrival_time = random.uniform(1, self.arrival_time.value())

        self.mainTimer = QtCore.QTimer(self)
        self.mainTimer.timeout.connect(self.print_people)
        self.mainTimer.start()

        self.flag = True
        # Change in people spinbox

        self.people.valueChanged.connect(self.print_people)
        self.all_peoples = 0

        self.stop_button.clicked.connect(self.stop)
        self.start_button.clicked.connect(self.resume)

        self.retranslateUi(queuing_system_emulator)
        QtCore.QMetaObject.connectSlotsByName(queuing_system_emulator)

    def retranslateUi(self, queuing_system_emulator):
        _translate = QtCore.QCoreApplication.translate
        queuing_system_emulator.setWindowTitle(
            _translate("queuing_system_emulator", "Эмулятор системы массового обслуживания"))
        self.people_label.setText(_translate("queuing_system_emulator", "Кол-во людей"))
        self.stop_button.setText(_translate("queuing_system_emulator", "Stop"))
        self.checkout_label.setText(_translate("queuing_system_emulator", "Число касс"))
        self.arrival_time_label.setText(_translate("queuing_system_emulator", "Время прихода"))
        self.start_button.setText(_translate("queuing_system_emulator", "Start"))

    def change_the_number_of_checkouts(self):
        n1 = self.checkout.value()
        n2 = self.previous_value_of_the_number_of_cash_registers
        number = self.checkout.value() - self.previous_value_of_the_number_of_cash_registers
        if number > 0:
            for i in range(self.previous_value_of_the_number_of_cash_registers, self.checkout.value()):
                # Form = QtWidgets.QWidget()
                # cash = Ui_Form()
                # cash.number_Checkout = i + 1
                # cash.setupUi(Form)
                # self.verticalLayout.addWidget(Form)
                # self.checkouts.append(cash)
                Form = QtWidgets.QWidget()
                cash = Ui_Form()
                cash.number_Checkout = i + 1

                cash.timer = QtCore.QTimer(self)
                cash.timer.timeout.connect(lambda inter=i: self.removing_people_from_queue(inter))

                t_1 = cash.time_1
                self.clock_1.append(t_1)
                t_2 = cash.time_2
                self.clock_2.append(t_2)
                cash.maintenance_time = random.randint(self.clock_1[i], self.clock_2[i])
                # print("cash.maintenance_time: ", cash.maintenance_time)

                cash.timer.setInterval((cash.maintenance_time + 1) * 1000)
                cash.timer.start()
                self.checkouts.append(cash)

                cash.setupUi(Form)
                self.verticalLayout.addWidget(Form)
                # print("print(len(self.checkouts)): ", len(self.checkouts))
        else:
            for i in range(self.verticalLayout.count() - 1,
                           self.verticalLayout.count() - 1 - (self.verticalLayout.count() - self.checkout.value()), -1):
                delete_widget = self.verticalLayout.takeAt(i).widget()
                if delete_widget is not None:
                    delete_widget.deleteLater()
                self.checkouts.pop()
                # print("print(len(self.checkouts)): ", len(self.checkouts))

        self.scrollAreaWidgetContents.setLayout(self.verticalLayout)
        self.previous_value_of_the_number_of_cash_registers = self.checkout.value()

    def print_people(self):
        if self.flag:
            arrival_time = random.randint(1, self.arrival_time.value())
            self.mainTimer.setInterval(arrival_time * 1000)
            people = random.randint(0, self.people.value())
            for i in range(people):
                min_queue = self.find_min_people_in_queue()
                min_queue.queue += 1
                min_queue.queue_length.setText(f'{min_queue.queue}')
        # self.all_peoples += people

    def find_min_people_in_queue(self):
        min = 1000
        for i in range(len(self.checkouts)):
            if min > self.checkouts[i].queue:
                min = self.checkouts[i].queue
                min_index = i
        return self.checkouts[min_index]

    # def find_min_people_in_queue(self):
    #     min = self.checkouts[0].queue
    #     for i in range(1, len(self.checkouts)):
    #         if min > self.checkouts[i].queue:
    #             min = self.checkouts[i].queue
    #             min_index = i
    #     return self.checkouts[min_index]

    def removing_people_from_queue(self, number_cash_desk):
        if self.checkouts[number_cash_desk].queue != 0:
            self.checkouts[number_cash_desk].queue -= 1
            self.clock_1[number_cash_desk] = self.checkouts[number_cash_desk].time_1
            self.clock_2[number_cash_desk] = self.checkouts[number_cash_desk].time_2
            # self.checkouts[number_cash_desk - 1].maintenance_time = random.randint(self.time_1,
            #                                                                        self.time_2)
            self.checkouts[number_cash_desk].maintenance_time = random.randint(self.clock_1[number_cash_desk],
                                                                                   self.clock_2[number_cash_desk])

            print(
                f"Номер кассы: {self.checkouts[number_cash_desk].number_Checkout}, first_time: {self.clock_1[number_cash_desk]}, second_time: {self.clock_2[number_cash_desk]}")
            print(f"Рандомное время: {self.checkouts[number_cash_desk].maintenance_time}")

            self.checkouts[number_cash_desk].timer.setInterval(
                self.checkouts[number_cash_desk].maintenance_time * 1000)
            self.checkouts[number_cash_desk].queue_length.setText(f'{self.checkouts[number_cash_desk].queue}')
            # min_queue.queue_length.setText(f'{min_queue.queue}')
        else:
            print("касса свободна")

    def stop(self):
        self.flag = False
        self.mainTimer.stop()
        for i in range(len(self.checkouts)):
            print(self.checkouts[i].number_Checkout)
            self.checkouts[i].timer.stop()

    def resume(self):
        self.flag = True
        self.mainTimer.start()
        for i in range(len(self.checkouts)):
            self.checkouts[i].timer.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    queuing_system_emulator = QtWidgets.QMainWindow()
    ui = Ui_queuing_system_emulator()
    ui.setupUi(queuing_system_emulator)
    queuing_system_emulator.show()
    sys.exit(app.exec_())
