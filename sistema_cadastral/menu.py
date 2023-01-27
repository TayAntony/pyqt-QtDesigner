
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from cadastrado import Cadastrado

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(800, 500)
        self.img_menu = QtWidgets.QLabel(Menu)
        self.img_menu.setGeometry(QtCore.QRect(0, 0, 800, 500))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.img_menu.setFont(font)
        self.img_menu.setText("")
        self.img_menu.setPixmap(QtGui.QPixmap("./imagens/menu_sistema.png"))
        self.img_menu.setObjectName("img_menu")

        self.enter_button = QtWidgets.QPushButton(Menu)
        self.enter_button.setGeometry(QtCore.QRect(450, 380, 41, 51))
        self.enter_button.setStyleSheet("background: rgba(255, 255, 255, 0);\n"
"border-radius: 100px;")
        self.enter_button.clicked.connect(self.criar_usuario)
        self.enter_button.setText("")
        self.enter_button.setObjectName("enter_button")

        self.data_nascimento = QtWidgets.QDateEdit(Menu)
        self.data_nascimento.setGeometry(QtCore.QRect(60, 389, 261, 30))
        self.data_nascimento.setStyleSheet("background: rgba(255,255,255, 0); border:  rgba(255,255,255, 0)")
        self.data_nascimento.setObjectName("data_nascimento")

        self.label_erro = QtWidgets.QLabel(Menu)
        self.label_erro.setGeometry(QtCore.QRect(60, 436, 251, 21))
        font = QtGui.QFont()
        self.label_erro.setFont(font)
        self.label_erro.setStyleSheet("color: red;")
        self.label_erro.setScaledContents(True)
        self.label_erro.setText("")
        self.label_erro.setObjectName("label_erro")

        self.lineEdit_nome = QtWidgets.QLineEdit(Menu)
        self.lineEdit_nome.setGeometry(QtCore.QRect(60, 168, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setStyleSheet("background: rgba(255,255,255,0)")
        self.lineEdit_nome.setText("")
        self.lineEdit_nome.setObjectName("lineEdit_nome")

        self.lineEdit_cpf = QtWidgets.QLineEdit(Menu)
        self.lineEdit_cpf.setGeometry(QtCore.QRect(60, 270, 251, 31))
        font = QtGui.QFont()
        self.lineEdit_cpf.setMaxLength(11)
        cpfRegex = QRegExp('^[0-9]*$')
        cpfValidator = QRegExpValidator(cpfRegex, self.lineEdit_cpf)
        self.lineEdit_cpf.setValidator(cpfValidator)
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.lineEdit_cpf.setFont(font)
        self.lineEdit_cpf.setStyleSheet("background: rgba(255,255,255,0)")
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Form"))


    def criar_usuario(self):
        users = open(r'usuarios.txt', 'r', encoding='utf-8')
        cadastros = users.readlines()
        if self.lineEdit_nome.text()=='' or self.lineEdit_cpf.text()=='':
            self.label_erro.setPixmap(QtGui.QPixmap("./imagens/preencha.png"))
        else:
            for cadastro in cadastros:
                separando = cadastro.split('_')
                if separando[1].strip() == self.lineEdit_cpf.text():
                    self.label_erro.setPixmap(QtGui.QPixmap("./imagens/cpf_cadastrado.png"))
                else:
                    cadastros = open(r'usuarios.txt', 'a', encoding='utf-8')
                    
                    cadastros.write(f'{self.lineEdit_nome.text().upper()}_{self.lineEdit_cpf.text()}\n')
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Cadastrado()
                    self.ui.setupUi(self.window)
                    self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QWidget()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
