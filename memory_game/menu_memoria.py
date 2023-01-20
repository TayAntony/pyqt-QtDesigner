
from PyQt5 import QtCore, QtGui, QtWidgets
from tela_easy import Easy
from tela_medium import Medium
from tela_hard import Hard

class Menu(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.img_yuumi = QtWidgets.QLabel(Form)
        self.img_yuumi.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.img_yuumi.setText("")
        self.img_yuumi.setPixmap(QtGui.QPixmap("./imagens_telas/menu_memoria.png"))
        self.img_yuumi.setObjectName("img_yuumi")

        self.botao_easy = QtWidgets.QPushButton(Form)
        self.botao_easy.setGeometry(QtCore.QRect(490, 160, 241, 41))
        self.botao_easy.setStyleSheet("background: rgba(255,255,255,0)")
        self.botao_easy.setText("")
        self.botao_easy.setObjectName("botao_easy")
        self.botao_easy.clicked.connect(self.easy_mode)

        self.botao_medium = QtWidgets.QPushButton(Form)
        self.botao_medium.setGeometry(QtCore.QRect(490, 230, 241, 41))
        self.botao_medium.setStyleSheet("background: rgba(255,255,255,0)")
        self.botao_medium.setText("")
        self.botao_medium.setObjectName("botao_medium")
        self.botao_medium.clicked.connect(self.medium_mode)

        self.botao_hard = QtWidgets.QPushButton(Form)
        self.botao_hard.setGeometry(QtCore.QRect(490, 300, 241, 41))
        self.botao_hard.setStyleSheet("background: rgba(255,255,255,0)")
        self.botao_hard.setText("")
        self.botao_hard.setObjectName("botao_hard")
        self.botao_hard.clicked.connect(self.hard_mode)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MENU"))
    
    def easy_mode(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Easy()
        self.ui.setupUi(self.window)
        self.window.show()

    def medium_mode(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Medium()
        self.ui.setupUi(self.window)
        self.window.show()

    def hard_mode(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Hard()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Menu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
