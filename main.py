# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from questionWindow import Ui_QuestionWindow
from addQuiz import Ui_addQuizWindow

import json
import os
from random import sample


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 400)
        MainWindow.setMinimumSize(QtCore.QSize(545, 400))
        MainWindow.setMaximumSize(QtCore.QSize(545, 400))
        self.quizzes = {
            "ML Quiz":"/quiz_data/ml_questions.json"
        }
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(545, 378))
        self.centralwidget.setMaximumSize(QtCore.QSize(545, 378))
        self.centralwidget.setSizeIncrement(QtCore.QSize(545, 378))
        self.centralwidget.setBaseSize(QtCore.QSize(545, 378))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 525, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_error = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_error.setEnabled(True)
        self.label_error.setMinimumSize(QtCore.QSize(238, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_error.setFont(font)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_2.addWidget(self.label_error)
        self.pushButton_addQuize = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_addQuize.setFont(font)
        self.pushButton_addQuize.setObjectName("pushButton_addQuize")
        self.horizontalLayout_2.addWidget(self.pushButton_addQuize)
        self.pushButton_editQuize = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_editQuize.setFont(font)
        self.pushButton_editQuize.setObjectName("pushButton_editQuize")
        self.horizontalLayout_2.addWidget(self.pushButton_editQuize)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)
        self.comboBox_quizeChoice = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_quizeChoice.addItem("ML Quiz")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.comboBox_quizeChoice.setFont(font)
        self.comboBox_quizeChoice.setToolTip("")
        self.comboBox_quizeChoice.setStatusTip("")
        self.comboBox_quizeChoice.setWhatsThis("")
        self.comboBox_quizeChoice.setAccessibleName("")
        self.comboBox_quizeChoice.setAccessibleDescription("")
        self.comboBox_quizeChoice.setCurrentText("ML Quiz")
        self.comboBox_quizeChoice.setMaxVisibleItems(42)
        self.comboBox_quizeChoice.setObjectName("comboBox_quizeChoice")
        self.verticalLayout.addWidget(self.comboBox_quizeChoice)
        self.label_answersShow = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_answersShow.setFont(font)
        self.label_answersShow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_answersShow.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_answersShow.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_answersShow.setTextFormat(QtCore.Qt.PlainText)
        self.label_answersShow.setAlignment(QtCore.Qt.AlignCenter)
        self.label_answersShow.setWordWrap(False)
        self.label_answersShow.setIndent(-1)
        self.label_answersShow.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_answersShow.setObjectName("label_answersShow")
        self.verticalLayout.addWidget(self.label_answersShow)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.radioButton_show = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.viewAnswerGroup = QtWidgets.QButtonGroup()
        self.viewAnswerGroup.setExclusive(True)
        self.radioButton_show.setFont(font)
        self.radioButton_show.setObjectName("radioButton_show")
        self.horizontalLayout.addWidget(self.radioButton_show)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.radioButton_hide = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.radioButton_hide.setFont(font)
        self.radioButton_hide.setAutoFillBackground(False)
        self.radioButton_hide.setObjectName("radioButton_hide")
        self.horizontalLayout.addWidget(self.radioButton_hide)
        self.viewAnswerGroup.addButton(self.radioButton_show)
        self.viewAnswerGroup.addButton(self.radioButton_hide)
        self.radioButton_hide.toggle()
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_timer = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_timer.setFont(font)
        self.label_timer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_timer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_timer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_timer.setTextFormat(QtCore.Qt.PlainText)
        self.label_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timer.setWordWrap(False)
        self.label_timer.setIndent(-1)
        self.label_timer.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_timer.setObjectName("label_timer")
        self.verticalLayout.addWidget(self.label_timer)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.radioButton_timer = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.radioButton_timer.setFont(font)
        self.radioButton_timer.setObjectName("radioButton_timer")
        self.horizontalLayout_5.addWidget(self.radioButton_timer)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.radioButton_noTimer = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.radioButton_noTimer.setFont(font)
        self.radioButton_noTimer.setAutoFillBackground(False)
        self.radioButton_noTimer.setObjectName("radioButton_noTimer")
        self.horizontalLayout_5.addWidget(self.radioButton_noTimer)
        self.timerRadioGroup = QtWidgets.QButtonGroup()
        self.timerRadioGroup.setExclusive(True)
        self.timerRadioGroup.addButton(self.radioButton_timer)
        self.timerRadioGroup.addButton(self.radioButton_noTimer)
        self.radioButton_timer.toggle()
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_amount = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_amount.setFont(font)
        self.label_amount.setObjectName("label_amount")
        self.horizontalLayout_4.addWidget(self.label_amount)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.spinBox_questiionNum = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinBox_questiionNum.setFont(font)
        self.spinBox_questiionNum.setSuffix("")
        self.spinBox_questiionNum.setPrefix("")
        self.spinBox_questiionNum.setMinimum(1)
        # Set Maximum For The First Time
        self.set_maximum()
        # Set Clicked For ComboBox
        self.comboBox_quizeChoice.currentTextChanged.connect(self.set_maximum)
        self.spinBox_questiionNum.setProperty("value", 1)
        self.spinBox_questiionNum.setObjectName("spinBox_questiionNum")
        self.horizontalLayout_4.addWidget(self.spinBox_questiionNum)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.pushButton_startQuiz = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_startQuiz.clicked.connect(self.start_quiz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_startQuiz.sizePolicy().hasHeightForWidth())
        self.pushButton_startQuiz.setSizePolicy(sizePolicy)
        self.pushButton_startQuiz.setMinimumSize(QtCore.QSize(160, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton_startQuiz.setFont(font)
        self.pushButton_startQuiz.setText("start quize")
        self.pushButton_startQuiz.setObjectName("pushButton_startQuiz")
        self.horizontalLayout_3.addWidget(self.pushButton_startQuiz)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Our Code
        self.MainWindow = MainWindow

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_error.setText(_translate("MainWindow", "ERROR INFO"))
        self.pushButton_addQuize.setText(_translate("MainWindow", "add new quize"))
        self.pushButton_editQuize.setText(_translate("MainWindow", "edit chosen quize"))
        self.label_info.setText(_translate("MainWindow", "choose a quize to word on:"))
        self.label_answersShow.setText(_translate("MainWindow", "show answers at the end of the quize?"))
        self.radioButton_show.setText(_translate("MainWindow", "show answers"))
        self.radioButton_hide.setText(_translate("MainWindow", "hide answers"))
        self.label_timer.setText(_translate("MainWindow", "set timer?"))
        self.radioButton_timer.setText(_translate("MainWindow", "set timer"))
        self.radioButton_noTimer.setText(_translate("MainWindow", "no timer"))
        self.label_amount.setText(_translate("MainWindow", "how many questions you want to answer?"))
    
    def set_maximum(self):
        chosen_quiz = self.comboBox_quizeChoice.currentText()
        print(f"Your Chosen Dish Is: {chosen_quiz}")
        path = os.getcwd() + self.quizzes[chosen_quiz]
        with open(path, 'r') as f:
            self.data = json.load(f)
        self.spinBox_questiionNum.setMaximum(len(list(self.data["questions"].keys())))
        
    def start_quiz(self):
        show_ans = self.radioButton_show.isChecked()
        is_timer = self.radioButton_timer.isChecked()
        num_questions = self.spinBox_questiionNum.value()
        #sample questions
        random_questions_number = sample(self.data["questions"].keys(),k=num_questions)
        #user_questions==[questions ,answers ,images ]
        user_questions= [[self.data["questions"][i],self.data["answers"][i] ,self.data["images"][i], self.data["multiple_choice"][i] ] for i in random_questions_number ]
        
        self.ui = Ui_QuestionWindow()
        self.ui.setupUi(self.MainWindow, user_questions, show_ans, is_timer, num_questions)
        self.MainWindow.show()
        print("log:finsh open questions window")
            


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
