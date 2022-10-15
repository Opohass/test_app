# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
import os
from random import sample
import datetime
from PyQt5.QtCore import QTimer,QDateTime
from image_window import Ui_Image


import sys


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
            
class Ui_QuestionWindow(object):
    def setupUi(self, QuestionWindow, data_file, show_ans, is_timer, num_questions):
        self.quiz_data = data_file
        self.show_answers = show_ans
        self.is_timer = is_timer
        self.num_questions = num_questions
        self.curent_ques_number =0
        QuestionWindow.setObjectName("QuestionWindow")
        QuestionWindow.resize(941, 565)
        QuestionWindow.setMinimumSize(QtCore.QSize(941, 565))
        QuestionWindow.setMaximumSize(QtCore.QSize(905, 525))
        font = QtGui.QFont()
        font.setFamily("Arial")
        QuestionWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(QuestionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 925, 527))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_question = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_question.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_question.setFont(font)
        self.label_question.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_question.setObjectName("label_question")
        self.label_question.setWordWrap(True)
        self.horizontalLayout_7.addWidget(self.label_question)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_timer = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_timer.setFont(font)
        self.label_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timer.setObjectName("label_timer")
        self.verticalLayout.addWidget(self.label_timer)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        #region hard coded demo
        # self.radioButton_c = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        # self.radioButton_c.setObjectName("radioButton_c")
        # self.gridLayout_2.addWidget(self.radioButton_c, 2, 0, 1, 1)
        # self.radioButton_b = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        # self.radioButton_b.setObjectName("radioButton_b")
        # self.gridLayout_2.addWidget(self.radioButton_b, 1, 0, 1, 1)
        # self.label_b = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label_b.setMinimumSize(QtCore.QSize(840, 70))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_b.setFont(font)
        # self.label_b.setObjectName("label_b")
        # self.gridLayout_2.addWidget(self.label_b, 1, 1, 1, 1)
        # self.label_a = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label_a.setMinimumSize(QtCore.QSize(840, 70))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_a.setFont(font)
        # self.label_a.setObjectName("label_a")
        # self.gridLayout_2.addWidget(self.label_a, 0, 1, 1, 1)
        # self.radioButton_a = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        # self.radioButton_a.setObjectName("radioButton_a")
        # self.gridLayout_2.addWidget(self.radioButton_a, 0, 0, 1, 1)
        # self.radioButton_d = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        # self.radioButton_d.setObjectName("radioButton_d")
        # self.gridLayout_2.addWidget(self.radioButton_d, 3, 0, 1, 1)
        # self.label_c = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label_c.setMinimumSize(QtCore.QSize(840, 70))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_c.setFont(font)
        # self.label_c.setObjectName("label_c")
        # self.gridLayout_2.addWidget(self.label_c, 2, 1, 1, 1)
        # self.label_d = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label_d.setMinimumSize(QtCore.QSize(840, 70))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_d.setFont(font)
        # self.label_d.setObjectName("label_d")
        # self.gridLayout_2.addWidget(self.label_d, 3, 1, 1, 1)
        
        # endregion
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_previous = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_previous.setEnabled(False)
        self.pushButton_previous.setMinimumSize(QtCore.QSize(45, 65))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_previous.setFont(font)
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.horizontalLayout.addWidget(self.pushButton_previous)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_next = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_next.setMinimumSize(QtCore.QSize(45, 65))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        QuestionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QuestionWindow)
        self.statusbar.setObjectName("statusbar")
        QuestionWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(QuestionWindow)
        QtCore.QMetaObject.connectSlotsByName(QuestionWindow)
        ##temp save windows?
        self.QuestionWindow=QuestionWindow
        
        #button
        self.pushButton_next.clicked.connect(self.next_question)
        self.pushButton_previous.clicked.connect(self.previous_question)
        #SaveAnswer
        self.UserAnswer=[False for i in range(self.num_questions)]
        # Call Update Question
        self.update_question()
        # Set Button Text
        self.pushButton_next.setText("Next Question")
        self.pushButton_previous.setText("No Previous")
        #timer'
        self.label_2.setText("00:00:00")
        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.startTime=QDateTime.currentDateTime()
    def showTime(self):
        time= (self.num_questions*120)+(QDateTime.currentDateTime().secsTo(self.startTime))
        #check if time end
        if time<=0:
            self.timer.stop()
            self.label_2.setText("Time end")  
            #!end queq?
        else:
            self.label_2.setText(str(datetime.timedelta(seconds=time)))  
            
    def next_question(self):
        self.submit_answer()
        self.curent_ques_number+=1
        #for test
        print(f"log: {self.curent_ques_number}")
        #end test
        if self.curent_ques_number==self.num_questions:
            self.timer.stop()
            self.call_result_window()
            print("log: end test")
        else:
            self.update_question()
            if self.curent_ques_number<self.num_questions-1:
                #change previous button label
                if self.pushButton_previous.text()=="No Previous": self.pushButton_previous.setText("previous question")
                
                
                #!todo change label to new question in position self.curent_ques_number
                #enbale previous_Button
                self.pushButton_previous.setEnabled(True)
                pass
            elif self.curent_ques_number==self.num_questions-1:
                #!todo change nextquestion label to end test
                self.pushButton_next.setText("End Test")
                pass
     
    
    def previous_question(self):
        #for test
        print(f"log: {self.curent_ques_number}")
        self.submit_answer()
        self.curent_ques_number-=1
        #!todo change label to new question in position self.curent_ques_number
        self.update_question()
        if self.curent_ques_number==0:
            #!todo change nextquestion label to end test
            self.pushButton_previous.setText("No Previous")
            self.pushButton_previous.setEnabled(False)
            pass
        if self.curent_ques_number == self.num_questions - 2:
            self.pushButton_next.setText("Next Question")
            self.pushButton_previous.setText("Previous Question")
            
    def update_question(self):
         #try to close photo window
        try:
            self.imageWindow.close()
        except:
            pass
        self.clear_layout()
        self.label_question.setText(self.quiz_data[self.curent_ques_number][0])
        pos = 0
        for i in self.quiz_data[self.curent_ques_number][1].keys():
            multiple_choice = self.quiz_data[self.curent_ques_number][-1]
            if multiple_choice:
                button = QtWidgets.QCheckBox(self.verticalLayoutWidget)
                button.setObjectName(f"checkBox_{i}")
            else:
                button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
                button.setObjectName(f"radioButton_{i}")
            self.gridLayout_2.addWidget(button, pos, 0, 1, 1)
            label = QtWidgets.QLabel(self.verticalLayoutWidget)
            label.setMinimumSize(QtCore.QSize(840, 70))
            font = QtGui.QFont()
            font.setPointSize(16)
            label.setFont(font)
            label.setObjectName(f"label_ans_{i}")
            label.setText(i + ". " + self.quiz_data[self.curent_ques_number][1][i][0])
            label.setWordWrap(True)
            self.gridLayout_2.addWidget(label, pos, 1, 1, 1)
            if self.UserAnswer[self.curent_ques_number]:
                if i in self.UserAnswer[self.curent_ques_number]:
                    button.toggle()
            pos += 1
        
    def submit_answer(self):
        pos = 0
        multiple_choice = self.quiz_data[self.curent_ques_number][-1]
        # if multiple_choice:
        #     self.UserAnswer[self.curent_ques_number] = []
        self.UserAnswer[self.curent_ques_number] = []
        for i in self.quiz_data[self.curent_ques_number][1].keys():
            if multiple_choice:
                if self.gridLayout_2.itemAtPosition(pos,0).widget().isChecked():
                    self.UserAnswer[self.curent_ques_number].append(i)
            else:
                if self.gridLayout_2.itemAtPosition(pos,0).widget().isChecked():
                    #self.UserAnswer[self.curent_ques_number] = i
                    self.UserAnswer[self.curent_ques_number].append(i)
            pos += 1
        
    def show_image(self):
        path = os.getcwd() + "/quiz_data/images/" + self.quiz_data[self.curent_ques_number][-2]
        print(path)
        self.imageWindow = QtWidgets.QMainWindow()
        self.imageUi = Ui_Image()
        self.imageUi.setupUi(self.imageWindow, path)
        self.imageWindow.show()
    
    
    
    def show_results(self):
        # correct color: #2c702b, incorrect result: #750404
        self.resultWindow = QtWidgets.QMainWindow()
        self.resultUi = Ui_Results()
        
    def call_result_window(self):
        
        self.ui = Ui_Results()
        self.ui.setupUi(self.QuestionWindow,self.quiz_data,self.UserAnswer)
        #self.QuestionWindow.show()
    def clear_layout(self):
        for i in reversed(range(self.gridLayout_2.count())): 
            self.gridLayout_2.itemAt(i).widget().setParent(None)
class Ui_Results(object):
    #def setupUi(self, MainWindow, score, quiz_data, userAnswers, correct_answers):
    def setupUi(self,MainWindow,quiz_data,userAnswers):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        # Our Code
        
        self.quiz_data = quiz_data
        self.userAnswers = userAnswers
        self.score, self.correct_answers= self.calculate_score()
        # self.score = score
        # self.correct_answers = correct_answers
        # end
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.score_announce_label = QtWidgets.QLabel(self.centralwidget)
        self.score_announce_label.setGeometry(QtCore.QRect(190, 20, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.score_announce_label.setFont(font)
        self.score_announce_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score_announce_label.setObjectName("score_announce_label")
        self.final_score_label = QtWidgets.QLabel(self.centralwidget)
        self.final_score_label.setGeometry(QtCore.QRect(420, 20, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.final_score_label.setFont(font)
        self.final_score_label.setObjectName("final_score_label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 751, 401))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 490, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #027aa6; color: black;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #windows
        self.MainWindow=MainWindow
        #set _list
        self.set_list()
        #button
        self.pushButton.clicked.connect(self.back_mainwindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.score_announce_label.setText(_translate("MainWindow", "Final Score:"))
        self.final_score_label.setText(_translate("MainWindow", str(self.score)))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        # self.listWidget.setSortingEnabled(False)
        # item = self.listWidget.item(0)
        # item.setText(_translate("MainWindow", "Example"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Back To Menu"))
        
    def set_list(self):
        for i in range(len(self.quiz_data)):
            item = QtWidgets.QListWidgetItem()
            inp_str = ''
            if self.correct_answers[i]:
                inp_str = "Correct Answer\n"+ "You Answered: " + ", ".join(self.userAnswers[i]) + "\n"
                item.setText(inp_str)
                item.setBackground(QtGui.QColor('#2c702b'))
            else:
                inp_str = "Incorrect Answer\n"+ "You Answered: " + ", ".join(self.userAnswers[i]) + "\n"+" the Correct Answers is "+", ".join(self.Right_Anser[i])
                item.setText(inp_str)
                item.setBackground(QtGui.QColor('#750404'))
            # if self.quiz_data[i][-1]:
            #     if self.correct_answers[i]:
            #         inp_str = inp_str + "You Answered: " + ", ".join(self.userAnswers[i]) + "\n"
            
            self.listWidget.addItem(item)
                    
    def calculate_score(self):
        #process the quiz_data to only right answers
        self.Right_Anser=  [[L for L,anser in question[1].items() if anser[1] ]for question in self.quiz_data  ]
        #check if the answer is correct
        couter=0
        user_right_anser=[]
        for UserAnser,RightAnser in zip(self.userAnswers,self.Right_Anser):
            if UserAnser == RightAnser:
                user_right_anser.append(True)
                couter+=1
            else:user_right_anser.append(False)
        score= int(couter/len(user_right_anser)*100)
        return score,user_right_anser
    
    def back_mainwindow(self):
        
        #self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        print("log:try go back to main window")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())