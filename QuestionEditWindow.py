

from ftplib import error_temp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import functools
import json
import shutil
AASCII=65 #A number in ascii table

class Ui_addQestion_window(object):
    def setupUi(self, addQestion_window,quiz_name):
        self.answerNum={"question":"","answers":{},"image":False}# will hold the question and it's answers
        self.addQestion_window=addQestion_window
        self.addQestion_window.setObjectName("addQestion_window")
        self.addQestion_window.resize(805, 570)
        self.addQestion_window.setMinimumSize(QtCore.QSize(805, 570))
        self.addQestion_window.setMaximumSize(QtCore.QSize(805, 570))
        self.addQestion_window.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.addQestion_window.setFont(font)
        self.addQestion_window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self.addQestion_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 10, 771, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.questionEdit_Vert = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.questionEdit_Vert.setContentsMargins(0, 0, 0, 0)
        self.questionEdit_Vert.setObjectName("questionEdit_Vert")
        self.horizontalLayout_question = QtWidgets.QHBoxLayout()
        self.horizontalLayout_question.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_question.setObjectName("horizontalLayout_question")
        self.label_question = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_question.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_question.setFont(font)
        self.label_question.setObjectName("label_question")
        self.horizontalLayout_question.addWidget(self.label_question)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_question.addItem(spacerItem)
        self.textEdit_question = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_question.setMinimumSize(QtCore.QSize(0, 90))
        self.textEdit_question.setMaximumSize(QtCore.QSize(16777215, 75))
        self.textEdit_question.setObjectName("textEdit_question")
        self.horizontalLayout_question.addWidget(self.textEdit_question)
        self.questionEdit_Vert.addLayout(self.horizontalLayout_question)
        self.horizontalLayout_image = QtWidgets.QHBoxLayout()
        self.horizontalLayout_image.setObjectName("horizontalLayout_image")
        self.label_imageName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_imageName.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_imageName.setFont(font)
        self.label_imageName.setObjectName("label_imageName")
        self.horizontalLayout_image.addWidget(self.label_imageName)
        self.pushButton_upload = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.horizontalLayout_image.addWidget(self.pushButton_upload)
        self.pushButton_show = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_show.setFont(font)
        self.pushButton_show.setObjectName("pushButton_show")
        self.horizontalLayout_image.addWidget(self.pushButton_show)
        self.questionEdit_Vert.addLayout(self.horizontalLayout_image)
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 310))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 767, 308))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_scrollview = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_scrollview.setObjectName("verticalLayout_scrollview")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_fream = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_fream.setObjectName("verticalLayout_fream")
        self.verticalLayout_scrollview.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.questionEdit_Vert.addWidget(self.scrollArea)
        self.horizontalLayout_controlBTN = QtWidgets.QHBoxLayout()
        self.horizontalLayout_controlBTN.setObjectName("horizontalLayout_controlBTN")
        self.pushButton_answer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_answer.setFont(font)
        self.pushButton_answer.setObjectName("pushButton_answer")
        self.horizontalLayout_controlBTN.addWidget(self.pushButton_answer)
        self.pushButton_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_controlBTN.addWidget(self.pushButton_cancel)
        self.pushButton_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_controlBTN.addWidget(self.pushButton_save)
        self.questionEdit_Vert.addLayout(self.horizontalLayout_controlBTN)
        self.addQestion_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.addQestion_window)
        self.statusbar.setObjectName("statusbar")
        self.addQestion_window.setStatusBar(self.statusbar)

        #region clicks
        self.pushButton_answer.clicked.connect(self.addAnswer)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_upload.clicked.connect(self.upload)
        self.pushButton_show.clicked.connect(self.show_image)
        self.pushButton_cancel.clicked.connect(self.closeWindow)
        
       

        self.retranslateUi(self.addQestion_window)
        QtCore.QMetaObject.connectSlotsByName(self.addQestion_window)
        
        #variables
        self.photo_path=False
        self.quiz_name=quiz_name
        self.question_number=0

    def retranslateUi(self, addQestion_window):
        _translate = QtCore.QCoreApplication.translate
        addQestion_window.setWindowTitle(_translate("addQestion_window", "MainWindow"))
        self.label_question.setText(_translate("addQestion_window", "question:"))
        self.label_imageName.setText(_translate("addQestion_window", "image:"))
        self.pushButton_upload.setText(_translate("addQestion_window", "upload"))
        self.pushButton_show.setText(_translate("addQestion_window", "show image"))
        self.pushButton_answer.setText(_translate("addQestion_window", "add answer"))
        self.pushButton_cancel.setText(_translate("addQestion_window", "cancel"))
        self.pushButton_save.setText(_translate("addQestion_window", "save question"))
    

    def clear_layout(self,layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    layout.removeWidget(child.widget())
                    # child.widget().deleteLater()
                    # child.widget().setParent(None)
                    
                elif child.layout() is not None:
                    self.clear_layout(child.layout())
    def rmAnswer(self,key):
        #1)set text in the keys (getting everything to the former key)
        #2)remove old UI
        #3)reload the UI with the correct text
        keyAscii=ord(key)
        toChange=[]
        for i in range((len(self.answerNum["answers"])-(keyAscii-AASCII))):
            layout=self.verticalLayout_fream.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_answer"+chr(keyAscii+i))
            toChange.append(layout)
            
        if len(toChange)>0:
            for i in range(len(toChange)-1):
                cuttLay=toChange[i]
                nxtLay=toChange[i+1]
                chkbx=cuttLay.itemAt(0).widget()
                txtedit=cuttLay.itemAt(1).widget()
                chkbx.setChecked(nxtLay.itemAt(0).widget().isChecked())
                txtedit.setText(nxtLay.itemAt(1).widget().toPlainText())
        else:
            toChange=[self.verticalLayout_fream.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_answer"+chr(keyAscii))]
        self.clear_layout(toChange[-1]) 
        
        self.answerNum["answers"].popitem() 
    def addAnswer(self,key=False):
        #TODO: add the remove action for the button
        if not key:
            key=chr(AASCII+len(self.answerNum["answers"]))
        #creating UI elements
        horizontalLayout_answer = QtWidgets.QHBoxLayout()
        horizontalLayout_answer.setObjectName("horizontalLayout_answer"+str(key))
        checkBox_isAnswer = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        checkBox_isAnswer.setFont(font)
        checkBox_isAnswer.setObjectName("checkBox_isAnswer"+str(key))
        checkBox_isAnswer.setText("{})".format(str(key))) #TODO: won't use since ordering it while creating is a headeach
        horizontalLayout_answer.addWidget(checkBox_isAnswer)
        textEdit_answer = QtWidgets.QTextEdit(self.frame)
        textEdit_answer.setMinimumSize(QtCore.QSize(0, 75))
        textEdit_answer.setMaximumSize(QtCore.QSize(16777215, 75))
        textEdit_answer.setObjectName("textEdit_answer"+str(key))
        horizontalLayout_answer.addWidget(textEdit_answer)
        pushButton_delete_answer = QtWidgets.QPushButton(self.frame)
        pushButton_delete_answer.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resorces/icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_delete_answer.setIcon(icon)
        pushButton_delete_answer.setObjectName("pushButton_delete_answer"+str(key))
        pushButton_delete_answer.clicked.connect(functools.partial(self.rmAnswer,str(key)))
        horizontalLayout_answer.addWidget(pushButton_delete_answer)
        self.verticalLayout_fream.addLayout(horizontalLayout_answer)
        
        self.answerNum["answers"][str(key)]=""
    def setup_data(self,data,question_number):
        self.textEdit_question.setPlainText(data[0])
        for ans in data[1].values():
            self.setqusions(ans)
        self.question_number=question_number
        self.photo_path=data[3]
            
         
    def setqusions(self,answer,key=False): #change 3 add answer prem
        #TODO: add the remove action for the button
        if not key:
            key=chr(AASCII+len(self.answerNum["answers"]))
        #creating UI elements
        horizontalLayout_answer = QtWidgets.QHBoxLayout()
        horizontalLayout_answer.setObjectName("horizontalLayout_answer"+str(key))
        checkBox_isAnswer = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        checkBox_isAnswer.setFont(font)
        checkBox_isAnswer.setObjectName("checkBox_isAnswer"+str(key))
        checkBox_isAnswer.setText("{})".format(str(key))) #TODO: won't use since ordering it while creating is a headeach
        #set checkbox #change 1
        checkBox_isAnswer.setCheckState(answer[1])
        
        horizontalLayout_answer.addWidget(checkBox_isAnswer)
        textEdit_answer = QtWidgets.QTextEdit(self.frame)
        textEdit_answer.setMinimumSize(QtCore.QSize(0, 75))
        textEdit_answer.setMaximumSize(QtCore.QSize(16777215, 75))
        textEdit_answer.setObjectName("textEdit_answer"+str(key))
        horizontalLayout_answer.addWidget(textEdit_answer)
        pushButton_delete_answer = QtWidgets.QPushButton(self.frame)
        #set the answer text #change 2
        textEdit_answer.setText(answer[0])
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resorces/icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_delete_answer.setIcon(icon)
        pushButton_delete_answer.setObjectName("pushButton_delete_answer"+str(key))
        pushButton_delete_answer.clicked.connect(functools.partial(self.rmAnswer,str(key)))
        horizontalLayout_answer.addWidget(pushButton_delete_answer)
        self.verticalLayout_fream.addLayout(horizontalLayout_answer)
        
        self.answerNum["answers"][str(key)]=answer[0]
    def save(self):
        eror_mesage=False
        #check if  the question is in format

        #if more then 2 questions
        if len(self.answerNum["answers"])<1:eror_mesage="there need to be at least 2 posibale answers"
        # if there is question
        elif self.textEdit_question.toPlainText()=="": eror_mesage="there need to be question"
        else:
            #loop over all answers and check for check anser and save the answer
            ansers={}
            check_count=0
            for widgets in self.verticalLayout_fream.children():
                try:
                    tempcheck=widgets.itemAt(0).widget().isChecked()
                    #save one answer
                    ansers[widgets.itemAt(0).widget().text()[:-1]]  =[widgets.itemAt(1).widget().toPlainText(),tempcheck]
                    #check for text in answer
                    if ansers[widgets.itemAt(0).widget().text()[:-1]]=="":
                        eror_mesage="there must be text in ansers"
                        break
            
                    elif tempcheck:check_count+=1
                except:
                    print("log: eror in save_to_json",ansers)
                    
            if check_count:
                if self.save_to_json(ansers,check_count):
                    from addQuiz import Ui_addQuizWindow
                    self.ui = Ui_addQuizWindow(True,"quiz_data_devlop/quiz_json/"+self.quiz_name+".json")
                    self.ui.setupUi(self.addQestion_window)
                    self.addQestion_window.show()
                    
                #the answer need to save and go back to ????
            else:eror_mesage="you need to check at least one answer"
            
        #show mesage with correct eror
        if eror_mesage:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("eror")
            msg.setText(eror_mesage)
            msg.exec_()
        
        
    
    def save_to_json(self,ansers,check_count): 
        try:
            with open("quiz_data_devlop/quiz_json/"+self.quiz_name+".json") as j: 
                temp_question=json.load(j)
                question_number= self.question_number if self.question_number else len(temp_question["questions"])+1 #change 4
                #add the question
                temp_question["questions"][question_number]=self.textEdit_question.toPlainText()
                #add the answers
                temp_question["answers"][question_number]=ansers
                #images url
                temp_question["images"][question_number]=self.photo_path
                #multiple_choice condton
                temp_question["multiple_choice"][question_number]=  check_count>1
            with open("quiz_data_devlop/quiz_json/"+self.quiz_name+".json", 'w') as f:
                    json.dump(temp_question, f,indent=4)
            return True
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("eror")
            msg.setText("eror in save question")
            msg.exec_()
            return False
        
    def upload(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        
        try:
            with open("quiz_data_devlop/quiz_json/"+self.quiz_name+".json") as j: 
                temp_question=json.load(j)
                question_number=self.question_number if self.question_number else len(temp_question["questions"])+1 #change 4
            temp="quiz_data_devlop/images/"+self.quiz_name+"/"+str(question_number)+"."+path.split(".")[-1]
            #check if we can open the photo
            QtGui.QPixmap(temp)
            #copy photo 
            shutil.copy2(path,temp)
            self.photo_path=temp
        except Exception as e:
            print("log: eror upload photo ", e)
    def show_image(self):
        from image_window import Ui_Image
        if self.photo_path:
            self.imageWindow = QtWidgets.QMainWindow()
            self.imageUi = Ui_Image()
            self.imageUi.setupUi(self.imageWindow, self.photo_path)
            self.imageWindow.show()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("eror")
            msg.setText("upload photo first")
            msg.exec_()
    def closeWindow(self):
        print("log i - clicked on close")
        msg = QtWidgets.QMessageBox()
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        msg.setWindowTitle("exit")
        msg.setText("are you sure you want to exit?")
        msg.exec_()
        if msg.standardButton(msg.clickedButton()) == QtWidgets.QMessageBox.Yes:
            # from main import Ui_MainWindow
            # self.ui = Ui_MainWindow()
            # self.ui.setupUi(self.addQestion_window)
            # self.addQestion_window.show()  
            from addQuiz import Ui_addQuizWindow
            self.ui = Ui_addQuizWindow(True,"quiz_data_devlop/quiz_json/"+self.quiz_name+".json")
            self.ui.setupUi(self.addQestion_window)
            self.addQestion_window.show()
   
                 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addQestion_window = QtWidgets.QMainWindow()
    ui = Ui_addQestion_window()
    ui.setupUi(addQestion_window,"ml_questions")
    addQestion_window.show()
    sys.exit(app.exec_())
