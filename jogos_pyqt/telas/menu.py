
from PyQt5 import QtCore, QtGui, QtWidgets
from velha import Velha
from jokenpo import Jokenpo
import forca

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.imagem_menu = QtWidgets.QLabel(Form)
        self.imagem_menu.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.imagem_menu.setText("")
        self.imagem_menu.setPixmap(QtGui.QPixmap("./imagens/menu.png"))
        self.imagem_menu.setScaledContents(True)
        self.imagem_menu.setObjectName("imagem_menu")

        self.botao_velha = QtWidgets.QPushButton(Form)
        self.botao_velha.setGeometry(QtCore.QRect(420, 260, 261, 51))
        self.botao_velha.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_velha.setText("")
        self.botao_velha.clicked.connect(self.abrir_velha)
        self.botao_velha.setObjectName("botao_velha")

        self.botao_jokenpo = QtWidgets.QPushButton(Form)
        self.botao_jokenpo.setGeometry(QtCore.QRect(80, 260, 261, 51))
        self.botao_jokenpo.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_jokenpo.setText("")
        self.botao_jokenpo.clicked.connect(self.abrir_jokenpo)
        self.botao_jokenpo.setObjectName("botao_jokenpo")

        self.botao_forca = QtWidgets.QPushButton(Form)
        self.botao_forca.setGeometry(QtCore.QRect(250, 390, 281, 51))
        self.botao_forca.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_forca.setText("")
        self.botao_forca.clicked.connect(self.abrir_forca)
        self.botao_forca.setObjectName("botao_forca")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MENU", "Jogos da Tay"))

    def abrir_jokenpo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Jokenpo()
        self.ui.setupUi(self.window)
        self.window.show()

    def abrir_velha(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Velha()
        self.ui.setupUi(self.window)
        self.window.show()

    def abrir_forca(self):
        self.window = QtWidgets.QMainWindow()
        forca.main(self.window)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
