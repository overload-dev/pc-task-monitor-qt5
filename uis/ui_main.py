# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 500)
        MainWindow.setMinimumSize(QtCore.QSize(670, 500))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgba(28, 29, 73, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.555012 rgba(28, 29, 73, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_title = QtWidgets.QFrame(self.frame)
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_title.setStyleSheet("background-color:none;")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(60, 231, 195)")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_title)
        self.frame_contents = QtWidgets.QFrame(self.frame)
        self.frame_contents.setStyleSheet("background-color:none;")
        self.frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contents.setObjectName("frame_contents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_contents)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_cpu = QtWidgets.QFrame(self.frame_contents)
        self.frame_cpu.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_cpu.setStyleSheet("QFrame {\n"
"    background-color: none;\n"
"    border: 5px solid rgb(60, 231, 195);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"    border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_cpu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cpu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cpu.setObjectName("frame_cpu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_cpu)
        self.verticalLayout_4.setContentsMargins(10, 50, 10, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_cpu_title = QtWidgets.QLabel(self.frame_cpu)
        self.label_cpu_title.setMinimumSize(QtCore.QSize(0, 30))
        self.label_cpu_title.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_cpu_title.setFont(font)
        self.label_cpu_title.setStyleSheet("color:rgb(60, 231, 195);\n"
"border:none;")
        self.label_cpu_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpu_title.setObjectName("label_cpu_title")
        self.verticalLayout_4.addWidget(self.label_cpu_title)
        self.label_cpu_usage_per = QtWidgets.QLabel(self.frame_cpu)
        self.label_cpu_usage_per.setMinimumSize(QtCore.QSize(0, 80))
        self.label_cpu_usage_per.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        self.label_cpu_usage_per.setFont(font)
        self.label_cpu_usage_per.setStyleSheet("border:none;\n"
"color: rgb(220, 220, 220);")
        self.label_cpu_usage_per.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpu_usage_per.setObjectName("label_cpu_usage_per")
        self.verticalLayout_4.addWidget(self.label_cpu_usage_per)
        self.label_cpu_model = QtWidgets.QLabel(self.frame_cpu)
        self.label_cpu_model.setMinimumSize(QtCore.QSize(0, 20))
        self.label_cpu_model.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_cpu_model.setFont(font)
        self.label_cpu_model.setStyleSheet("border:none;\n"
"color: rgb(128, 102, 168);")
        self.label_cpu_model.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpu_model.setObjectName("label_cpu_model")
        self.verticalLayout_4.addWidget(self.label_cpu_model)
        self.frame_cpu_detail = QtWidgets.QFrame(self.frame_cpu)
        self.frame_cpu_detail.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_cpu_detail.setStyleSheet("border: none;")
        self.frame_cpu_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cpu_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cpu_detail.setObjectName("frame_cpu_detail")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_cpu_detail)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_cpu_detail_column = QtWidgets.QFrame(self.frame_cpu_detail)
        self.frame_cpu_detail_column.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cpu_detail_column.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cpu_detail_column.setObjectName("frame_cpu_detail_column")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_cpu_detail_column)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_freq_title = QtWidgets.QLabel(self.frame_cpu_detail_column)
        self.label_freq_title.setMinimumSize(QtCore.QSize(0, 0))
        self.label_freq_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_freq_title.setFont(font)
        self.label_freq_title.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_freq_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_freq_title.setObjectName("label_freq_title")
        self.verticalLayout_5.addWidget(self.label_freq_title)
        self.label_core_phy_title = QtWidgets.QLabel(self.frame_cpu_detail_column)
        self.label_core_phy_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_core_phy_title.setFont(font)
        self.label_core_phy_title.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_core_phy_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_core_phy_title.setObjectName("label_core_phy_title")
        self.verticalLayout_5.addWidget(self.label_core_phy_title)
        self.label_core_log_title = QtWidgets.QLabel(self.frame_cpu_detail_column)
        self.label_core_log_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_core_log_title.setFont(font)
        self.label_core_log_title.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_core_log_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_core_log_title.setObjectName("label_core_log_title")
        self.verticalLayout_5.addWidget(self.label_core_log_title)
        self.horizontalLayout_2.addWidget(self.frame_cpu_detail_column, 0, QtCore.Qt.AlignTop)
        self.frame_cpu_detail_data = QtWidgets.QFrame(self.frame_cpu_detail)
        self.frame_cpu_detail_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cpu_detail_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cpu_detail_data.setObjectName("frame_cpu_detail_data")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_cpu_detail_data)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_freq = QtWidgets.QLabel(self.frame_cpu_detail_data)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_freq.setFont(font)
        self.label_freq.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_freq.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_freq.setObjectName("label_freq")
        self.verticalLayout_6.addWidget(self.label_freq)
        self.label_core_phy = QtWidgets.QLabel(self.frame_cpu_detail_data)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_core_phy.setFont(font)
        self.label_core_phy.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_core_phy.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_core_phy.setObjectName("label_core_phy")
        self.verticalLayout_6.addWidget(self.label_core_phy)
        self.label_core_log = QtWidgets.QLabel(self.frame_cpu_detail_data)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_core_log.setFont(font)
        self.label_core_log.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_core_log.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_core_log.setObjectName("label_core_log")
        self.verticalLayout_6.addWidget(self.label_core_log)
        self.horizontalLayout_2.addWidget(self.frame_cpu_detail_data, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.frame_cpu_detail)
        self.horizontalLayout.addWidget(self.frame_cpu)
        self.frame_memory = QtWidgets.QFrame(self.frame_contents)
        self.frame_memory.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_memory.setStyleSheet("QFrame {\n"
"    background-color: none;\n"
"    border: 5px solid rgb(60, 231, 195);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"    border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_memory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_memory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_memory.setObjectName("frame_memory")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_memory)
        self.verticalLayout_9.setContentsMargins(10, 50, 10, 0)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_memory_title = QtWidgets.QLabel(self.frame_memory)
        self.label_memory_title.setMinimumSize(QtCore.QSize(0, 30))
        self.label_memory_title.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_memory_title.setFont(font)
        self.label_memory_title.setStyleSheet("color:rgb(60, 231, 195);\n"
"border:none;")
        self.label_memory_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_memory_title.setObjectName("label_memory_title")
        self.verticalLayout_9.addWidget(self.label_memory_title)
        self.label_memory_usage_per = QtWidgets.QLabel(self.frame_memory)
        self.label_memory_usage_per.setMinimumSize(QtCore.QSize(0, 80))
        self.label_memory_usage_per.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        self.label_memory_usage_per.setFont(font)
        self.label_memory_usage_per.setStyleSheet("border:none;\n"
"color: rgb(220, 220, 220);")
        self.label_memory_usage_per.setAlignment(QtCore.Qt.AlignCenter)
        self.label_memory_usage_per.setObjectName("label_memory_usage_per")
        self.verticalLayout_9.addWidget(self.label_memory_usage_per)
        self.frame_memory_detail = QtWidgets.QFrame(self.frame_memory)
        self.frame_memory_detail.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_memory_detail.setStyleSheet("border: none;")
        self.frame_memory_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_memory_detail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_memory_detail.setObjectName("frame_memory_detail")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_memory_detail)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_memory_detail_column = QtWidgets.QFrame(self.frame_memory_detail)
        self.frame_memory_detail_column.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_memory_detail_column.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_memory_detail_column.setObjectName("frame_memory_detail_column")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_memory_detail_column)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_memory_total_title = QtWidgets.QLabel(self.frame_memory_detail_column)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_memory_total_title.setFont(font)
        self.label_memory_total_title.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_total_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_memory_total_title.setObjectName("label_memory_total_title")
        self.verticalLayout_7.addWidget(self.label_memory_total_title)
        self.label_memory_free_title = QtWidgets.QLabel(self.frame_memory_detail_column)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_memory_free_title.setFont(font)
        self.label_memory_free_title.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_free_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_memory_free_title.setObjectName("label_memory_free_title")
        self.verticalLayout_7.addWidget(self.label_memory_free_title)
        self.label_memory_used_title = QtWidgets.QLabel(self.frame_memory_detail_column)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_memory_used_title.setFont(font)
        self.label_memory_used_title.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_used_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_memory_used_title.setObjectName("label_memory_used_title")
        self.verticalLayout_7.addWidget(self.label_memory_used_title)
        self.horizontalLayout_3.addWidget(self.frame_memory_detail_column, 0, QtCore.Qt.AlignTop)
        self.frame_memory_detail_data = QtWidgets.QFrame(self.frame_memory_detail)
        self.frame_memory_detail_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_memory_detail_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_memory_detail_data.setObjectName("frame_memory_detail_data")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_memory_detail_data)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_memory_total = QtWidgets.QLabel(self.frame_memory_detail_data)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_memory_total.setFont(font)
        self.label_memory_total.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_total.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_memory_total.setObjectName("label_memory_total")
        self.verticalLayout_8.addWidget(self.label_memory_total)
        self.label_memory_free = QtWidgets.QLabel(self.frame_memory_detail_data)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_memory_free.setFont(font)
        self.label_memory_free.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_free.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_memory_free.setObjectName("label_memory_free")
        self.verticalLayout_8.addWidget(self.label_memory_free)
        self.label_memory_used = QtWidgets.QLabel(self.frame_memory_detail_data)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_memory_used.setFont(font)
        self.label_memory_used.setStyleSheet("border:none;\n"
"color: rgb(60, 231, 195);")
        self.label_memory_used.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_memory_used.setObjectName("label_memory_used")
        self.verticalLayout_8.addWidget(self.label_memory_used)
        self.horizontalLayout_3.addWidget(self.frame_memory_detail_data, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_9.addWidget(self.frame_memory_detail)
        self.horizontalLayout.addWidget(self.frame_memory)
        self.verticalLayout_2.addWidget(self.frame_contents)
        self.verticalLayout.addWidget(self.frame)
        self.frame_credits = QtWidgets.QFrame(self.centralwidget)
        self.frame_credits.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_credits.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_credits.setObjectName("frame_credits")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_credits)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.frame_credits)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(128, 102, 168);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_credits)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task Monitor"))
        self.label.setText(_translate("MainWindow", "Task Monitor"))
        self.label_cpu_title.setText(_translate("MainWindow", "CPU"))
        self.label_cpu_usage_per.setText(_translate("MainWindow", "50%"))
        self.label_cpu_model.setText(_translate("MainWindow", "Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz"))
        self.label_freq_title.setText(_translate("MainWindow", "Speed :"))
        self.label_core_phy_title.setText(_translate("MainWindow", "Core (Physical) :"))
        self.label_core_log_title.setText(_translate("MainWindow", "Core (logical) :"))
        self.label_freq.setText(_translate("MainWindow", "3.1920 GHz"))
        self.label_core_phy.setText(_translate("MainWindow", "6"))
        self.label_core_log.setText(_translate("MainWindow", "12"))
        self.label_memory_title.setText(_translate("MainWindow", "MEMORY"))
        self.label_memory_usage_per.setText(_translate("MainWindow", "50%"))
        self.label_memory_total_title.setText(_translate("MainWindow", "Total :"))
        self.label_memory_free_title.setText(_translate("MainWindow", "Free :"))
        self.label_memory_used_title.setText(_translate("MainWindow", "Used :"))
        self.label_memory_total.setText(_translate("MainWindow", "32 GB"))
        self.label_memory_free.setText(_translate("MainWindow", "19 GB"))
        self.label_memory_used.setText(_translate("MainWindow", "13 GB"))
        self.label_2.setText(_translate("MainWindow", "Create By Overload"))