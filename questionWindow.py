# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/questionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import datetime
from operator import imod
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QDateTime
import os
from image_window import Ui_Image
from result_window import Ui_Results


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
        else:
            #!todo end test
             #for test
            print("log: end test")
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
            if multiple_choice:
                if self.UserAnswer[self.curent_ques_number]:
                    if i in self.UserAnswer[self.curent_ques_number]:
                        button.toggle()
            else:
                if self.UserAnswer[self.curent_ques_number] == i:
                    button.toggle()
            if self.quiz_data[self.curent_ques_number][-2]:
                self.show_image()
            pos += 1
        
    def submit_answer(self):
        pos = 0
        multiple_choice = self.quiz_data[self.curent_ques_number][-1]
        if multiple_choice:
            self.UserAnswer[self.curent_ques_number] = []
        for i in self.quiz_data[self.curent_ques_number][1].keys():
            if multiple_choice:
                if self.gridLayout_2.itemAtPosition(pos,0).widget().isChecked():
                    self.UserAnswer[self.curent_ques_number].append(i)
            else:
                if self.gridLayout_2.itemAtPosition(pos,0).widget().isChecked():
                    self.UserAnswer[self.curent_ques_number] = i
            pos += 1
        
    def show_image(self):
        path = os.getcwd() + "/quiz_data/images/" + self.quiz_data[self.curent_ques_number][-2]
        print(path)
        self.imageWindow = QtWidgets.QMainWindow()
        self.imageUi = Ui_Image()
        self.imageUi.setupUi(self.imageWindow, path)
        self.imageWindow.show()
    
    def calculate_score(self):
        pass
    
    def show_results(self):
        # correct color: #2c702b, incorrect result: #750404
        self.resultWindow = QtWidgets.QMainWindow()
        self.resultUi = Ui_Results()
        
        
            
            
    
        
        
    
    # def retranslateUi(self, QuestionWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     QuestionWindow.setWindowTitle(_translate("QuestionWindow", "MainWindow"))
    #     self.label_question.setText(_translate("QuestionWindow", "You are building an ML model to detect anomalies in real-time sensor data.<br>You will use Pub/Sub to handle incoming requests.<br> You want to store the results for analytics and visualization.<br>How should you configure the pipeline?"))
    #     self.label_timer.setText(_translate("QuestionWindow", "time<br>remening"))
    #     #self.label_2.setText(_translate("QuestionWindow", "TextLabel"))
    #     self.radioButton_c.setText(_translate("QuestionWindow", "C"))
    #     self.radioButton_b.setText(_translate("QuestionWindow", "B"))
    #     self.label_b.setText(_translate("QuestionWindow", "1 = DataProc, 2 = AutoML, 3 = Cloud Bigtable"))
    #     self.label_a.setText(_translate("QuestionWindow", "1 = Dataflow, 2 = AI Platform, 3 = BigQuery"))
    #     self.radioButton_a.setText(_translate("QuestionWindow", "A"))
    #     self.radioButton_d.setText(_translate("QuestionWindow", "D"))
    #     self.label_c.setText(_translate("QuestionWindow", "1 = BigQuery, 2 = AutoML, 3 = Cloud Functions"))
    #     self.label_d.setText(_translate("QuestionWindow", "1 = BigQuery, 2 = AI Platform, 3 = Cloud Storage"))
    #     self.pushButton_previous.setText(_translate("QuestionWindow", "previous question"))
    #     self.pushButton_next.setText(_translate("QuestionWindow", "next question"))
    
    def clear_layout(self):
        for i in reversed(range(self.gridLayout_2.count())): 
            self.gridLayout_2.itemAt(i).widget().setParent(None)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     QuestionWindow = QtWidgets.QMainWindow()
#     ui = Ui_QuestionWindow()
#     ui.setupUi(QuestionWindow)
#     QuestionWindow.show()
#     sys.exit(app.exec_())
