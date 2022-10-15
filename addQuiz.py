# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addQuiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import functools
import json,os
from PyQt5.QtCore import pyqtSlot

class Ui_addQuizWindow(object):
    def __init__(self,isEdit=False,quizName=""): #FIXME: make sure from main that a quizName was passed when on edit
        self.isEdit=isEdit
        self.quizName=quizName
        
    def setupUi(self, addQuizWindow):
        addQuizWindow.setObjectName("addQuizWindow")
        addQuizWindow.resize(640, 605)
        addQuizWindow.setMinimumSize(QtCore.QSize(640, 605))
        addQuizWindow.setMaximumSize(QtCore.QSize(640, 605))
        self.MainWindow=addQuizWindow
        self.centralwidget = QtWidgets.QWidget(addQuizWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_quizName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_quizName.setEnabled(True)
        self.label_quizName.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_quizName.setFont(font)
        self.label_quizName.setObjectName("label_quizName")
        self.horizontalLayout_2.addWidget(self.label_quizName)
        self.lineEdit_quizName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_quizName.setFont(font)
        self.lineEdit_quizName.setObjectName("lineEdit_quizName")
        self.horizontalLayout_2.addWidget(self.lineEdit_quizName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_addQuestion = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_addQuestion.setObjectName("pushButton_addQuestion")
        self.verticalLayout.addWidget(self.pushButton_addQuestion)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 350))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 605, 453))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.pushButton_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        addQuizWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addQuizWindow)
        self.statusbar.setObjectName("statusbar")
        addQuizWindow.setStatusBar(self.statusbar)

        if not self.isEdit:
            self.questions={"questions":{},"answers":{},"images":{},"multiple_choice":{}}
        else:
            self.lineEdit_quizName.setEnabled(False)
            self.lineEdit_quizName.setText(self.quizName) #FIXME: show quiz name only
            self.loadQuestions(self.quizName)
            self.loadQuestionToUI()

        self.retranslateUi(addQuizWindow)
        QtCore.QMetaObject.connectSlotsByName(addQuizWindow)

        #button events
        self.pushButton_cancel.clicked.connect(self.closeWindow)
        self.pushButton_save.clicked.connect(self.saveQuiz)

    def retranslateUi(self, addQuizWindow):
        _translate = QtCore.QCoreApplication.translate
        addQuizWindow.setWindowTitle(_translate("addQuizWindow", "MainWindow"))
        self.label_quizName.setText(_translate("addQuizWindow", "quiz name:"))
        self.pushButton_addQuestion.setText(_translate("addQuizWindow", "add question"))
        self.pushButton_cancel.setText(_translate("addQuizWindow", "cancel"))
        self.pushButton_save.setText(_translate("addQuizWindow", "save"))

    def loadQuestionToUI(self):
        icon_edit = QtGui.QIcon()
        icon_edit.addPixmap(QtGui.QPixmap("./resorces/icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_remove = QtGui.QIcon()
        icon_remove.addPixmap(QtGui.QPixmap("./resorces/icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for i,(question,answer) in enumerate(zip(self.questions["questions"].values(),self.questions["answers"].values()),start=1):
            verticalLayout_questionContainer = QtWidgets.QVBoxLayout() #question and answers container
            horizontalLayout_questionNbuttons = QtWidgets.QHBoxLayout() #question label+HL for edit/remove buttons
            #creating question label
            label_question = QtWidgets.QLabel()
            label_question.setMinimumSize(QtCore.QSize(500, 90))
            label_question.setMaximumSize(QtCore.QSize(500, 16777215))
            label_question.setObjectName("label_question")
            label_question.setText(question)
            label_question.setWordWrap(True)
            horizontalLayout_questionNbuttons.addWidget(label_question)

            verticalLayout_editRemoveBtns = QtWidgets.QVBoxLayout() #HL for edit and remove buttons
            #edit button
            pushButton_edit = QtWidgets.QPushButton()
            pushButton_edit.setMinimumSize(QtCore.QSize(35, 35))
            pushButton_edit.setMaximumSize(QtCore.QSize(35, 35))
            pushButton_edit.setIcon(icon_edit) 
            pushButton_edit.clicked.connect(functools.partial(print,pushButton_edit))#TODO: set event to the button
            verticalLayout_editRemoveBtns.addWidget(pushButton_edit)
            #remove button
            pushButton_remove = QtWidgets.QPushButton()
            pushButton_remove.setMinimumSize(QtCore.QSize(35, 35))
            pushButton_remove.setMaximumSize(QtCore.QSize(35, 35))
            pushButton_remove.setIcon(icon_remove)
            pushButton_remove.clicked.connect(functools.partial(self.removeQuestion,str(i)))
            verticalLayout_editRemoveBtns.addWidget(pushButton_remove)
            horizontalLayout_questionNbuttons.addLayout(verticalLayout_editRemoveBtns) #inserting the HL edit/remove to question container
            verticalLayout_questionContainer.addLayout(horizontalLayout_questionNbuttons)

            for key,value in answer.items():
                horizontalLayout_answers = QtWidgets.QHBoxLayout() #holds answer A-F,answer content,checkbox isAnswer
                #answer location
                label_location = QtWidgets.QLabel()
                label_location.setMinimumSize(QtCore.QSize(0, 0))
                label_location.setMaximumSize(QtCore.QSize(12, 16777215))
                label_location.setObjectName("label_location")
                label_location.setText(key)
                label_location.setWordWrap(True)
                horizontalLayout_answers.addWidget(label_location)
                #answer label
                label_answer = QtWidgets.QLabel()
                label_answer.setObjectName("label_answer")
                label_answer.setText(value[0])
                label_answer.setWordWrap(True)
                horizontalLayout_answers.addWidget(label_answer)
                #checkbox to mark if correct answer
                checkBox_isAnswer = QtWidgets.QCheckBox()
                checkBox_isAnswer.setEnabled(False)
                checkBox_isAnswer.setMaximumSize(QtCore.QSize(70, 16777215))
                checkBox_isAnswer.setFont(font)
                checkBox_isAnswer.setChecked(value[1])
                horizontalLayout_answers.addWidget(checkBox_isAnswer)

                verticalLayout_questionContainer.addLayout(horizontalLayout_answers)

            self.verticalLayout_4.addLayout(verticalLayout_questionContainer)
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.verticalLayout_4.addWidget(line)

    def clear_layout(self,layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clear_layout(child.layout())

    def removeQuestion(self,key):
        print(f"log A - removing questin with the key:{key}")
        #remove the image data form the delete question
        if self.questions["images"][str(key)]:
                try:
                    os.remove("./quiz_data/images/"+self.questions["images"][str(key)])
                except:
                    print(f"log E - image of question {key} does not exist while it is mentioned")

        #reorgnize the questin
        for i in range(int(key),len(self.questions["questions"])):
            
            self.questions["questions"][str(i)]=self.questions["questions"][str(i+1)]
            #del self.questions["questions"][str(i+1)]
            self.questions["answers"][str(i)]=self.questions["answers"][str(i+1)]
            #del self.questions["answers"][str(i+1)]
            self.questions["multiple_choice"][str(i)]=self.questions["multiple_choice"][str(i+1)]
            #del self.questions["multiple_choice"][str(i+1)]
            self.questions["images"][str(i)]=self.questions["images"][str(i+1)]
            #if question has image delete it
            # if str(i) in self.questions["images"] and self.questions["images"][str(i)]:
            #     try:
            #         os.remove("./quiz_data/images/"+self.questions["images"][str(i)])
            #     except:
            #         print(f"log E - image of question {i} does not exist while it is mentioned")
            # elif str(i+1) in self.questions["images"] and self.questions["images"][str(i+1)]:
            #     os.rename("./quiz_data/images/"+self.questions["images"][str(i+1)],
            #                 "./quiz_data/images/"+self.questions["images"][str(i+1)].split("/")[0]+f"/q{i}.png")
            # self.questions["images"][str(i)]=self.questions["images"][str(i+1)]
            # del self.questions["images"][str(i+1)]
        #remove the last question
        temp=str(len(self.questions["questions"]))
        del self.questions["questions"][temp]
        del self.questions["answers"][temp]
        del self.questions["multiple_choice"][temp]
        del self.questions["images"][temp]   
        
        self.clear_layout(self.verticalLayout_4)
        self.loadQuestionToUI()
        
        
    def loadQuestions(self,quizName):
        print("log i - opening questions")
        with open(quizName) as j: 
                self.questions=json.load(j)
    
    def saveQuiz(self):
        print("log i - clicked on save")
        if not len(self.questions)>0:
            print("log e - user is mega dumb and is tring to save a quiz without adding questions")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("ERROR T_T")
            msg.setText("must have at least 1 question at your test")
            msg.exec_()
        else:
            with open('data.json', 'w') as f:
                json.dump(self.questions, f,indent=4)
    
    def closeWindow(self):
        print("log i - clicked on close")
        msg = QtWidgets.QMessageBox()
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        msg.setWindowTitle("exit")
        msg.setText("are you sure you want to exit?")
        msg.exec_()
        if msg.standardButton(msg.clickedButton()) == QtWidgets.QMessageBox.Yes:
            from main import Ui_MainWindow
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()
    
    @pyqtSlot(dict)
    def change_question(self, new_question):
        import urllib
        quiz_name = self.quizName.split("/")[-1][:-5]
        self.questions["questions"][new_question["pos"]] = new_question["question"]
        self.questions["answers"][new_question["pos"]] = new_question["answer"]
        self.questions["questions"][new_question["pos"]] = new_question["question"]
        if new_question["image"]:
            self.questions["images"][new_question["pos"]] = quiz_name + "/" + new_question["pos"] + "." + new_question["image"].split(".")[-1]
        else:
            self.questions["images"][new_question["pos"]] = False
        self.questions["multiple_choice"][new_question["pos"]] = new_question["multiple_choice"]
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # addQuizWindow = QtWidgets.QMainWindow()
    addQuizWindow = QtWidgets.QMainWindow()
    ui = Ui_addQuizWindow(True,"./quiz_data/ml_questions.json")
    ui.setupUi(addQuizWindow)
    addQuizWindow.show()
    sys.exit(app.exec_())
