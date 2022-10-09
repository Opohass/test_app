# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import sys



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
        from main import Ui_MainWindow
        #self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        print("log:try go back to main window")
        
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Results()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
