
from PyQt5 import QtCore, QtGui, QtWidgets
import functools

AASCII=65 #A number in ascii table

class Ui_addQestion_window(object):
    def setupUi(self, addQestion_window):
        self.answerNum={"question":"","answers":{},"image":False}# will hold the question and it's answers

        addQestion_window.setObjectName("addQestion_window")
        addQestion_window.resize(805, 570)
        addQestion_window.setMinimumSize(QtCore.QSize(805, 570))
        addQestion_window.setMaximumSize(QtCore.QSize(805, 570))
        addQestion_window.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        addQestion_window.setFont(font)
        addQestion_window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(addQestion_window)
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
        addQestion_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addQestion_window)
        self.statusbar.setObjectName("statusbar")
        addQestion_window.setStatusBar(self.statusbar)

        #region clicks
        self.pushButton_answer.clicked.connect(self.addAnswer)
        self.pushButton_cancel.clicked.connect(self.back)
        #endregion
        
        #region DEMO
        # self.horizontalLayout_answer = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_answer.setObjectName("horizontalLayout_answer")
        # self.checkBox_isAnswer = QtWidgets.QCheckBox(self.frame)
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(14)
        # self.checkBox_isAnswer.setFont(font)
        # self.checkBox_isAnswer.setObjectName("checkBox_isAnswer")
        # self.checkBox_isAnswer.setText("A)") #NOT NEEDED
        # self.horizontalLayout_answer.addWidget(self.checkBox_isAnswer)
        # self.textEdit_answer = QtWidgets.QTextEdit(self.frame)
        # self.textEdit_answer.setMinimumSize(QtCore.QSize(0, 75))
        # self.textEdit_answer.setMaximumSize(QtCore.QSize(16777215, 75))
        # self.textEdit_answer.setObjectName("textEdit_answer")
        # self.horizontalLayout_answer.addWidget(self.textEdit_answer)
        # self.pushButton_delete = QtWidgets.QPushButton(self.frame)
        # self.pushButton_delete.setText("")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("./resorces/icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton_delete.setIcon(icon)
        # self.pushButton_delete.setObjectName("pushButton_delete")
        # self.horizontalLayout_answer.addWidget(self.pushButton_delete)
        # self.verticalLayout_fream.addLayout(self.horizontalLayout_answer)
        #endregion

        self.retranslateUi(addQestion_window)
        QtCore.QMetaObject.connectSlotsByName(addQestion_window)

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
    
    def uploadImage(self):
        #returns the image name
        #saves the image in self.image_uWu or something idk
        #updates self.label_imageName to image name
        pass
    
    def showImage(self):
        #open the image_window.py with the image as a side window
        #if no image file show window 'lol you dumb' or somthing idk
        pass

    def clear_layout(self,layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
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
        # for k in self.answerNum["answers"]:
        #     # self.answerNum["answers"][k]=
        #     layout=self.verticalLayout_fream.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_answer"+k)
        #     l=layout.itemAt(1).widget()
        #     print(k,layout,l.toPlainText())
        # layout=self.verticalLayout_fream.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_answer"+key)
        # self.clear_layout(layout)
        # print(65-ord(key)) #use to loop over the keys
    
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

    def back(self,status=False):
        #if status True then return the data to addQuiz
        #if status True -> 
        #                  1)make sure there are at least 2 answers 
        #                  2) make sure at least 1 is marked ->
        #                     2.1)if more then 1 answer then return it as multiAnswer
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addQestion_window = QtWidgets.QMainWindow()
    ui = Ui_addQestion_window()
    ui.setupUi(addQestion_window)
    addQestion_window.show()
    sys.exit(app.exec_())
