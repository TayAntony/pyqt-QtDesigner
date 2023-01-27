
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.img_menu = QtWidgets.QLabel(Form)
        self.img_menu.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.img_menu.setText("")
        self.img_menu.setPixmap(QtGui.QPixmap("./imagens/menu_senha.png"))
        self.img_menu.setObjectName("img_menu")

        self.lineEdit_nome = QtWidgets.QLineEdit(Form)
        self.lineEdit_nome.setGeometry(QtCore.QRect(60, 168, 261, 31))
        self.lineEdit_nome.setObjectName("lineEdit_nome")

        self.lineEdit_cpf = QtWidgets.QLineEdit(Form)
        self.lineEdit_cpf.setGeometry(QtCore.QRect(60, 269, 261, 31))
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")

        self.lineEdit_senha = QtWidgets.QLineEdit(Form)
        self.lineEdit_senha.setGeometry(QtCore.QRect(60, 388, 261, 31))
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_erro = QtWidgets.QLabel(Form)
        self.label_erro.setGeometry(QtCore.QRect(50, 440, 301, 21))
        self.label_erro.setText("")
        self.label_erro.setObjectName("label_erro")

        self.enter_button = QtWidgets.QPushButton(Form)
        self.enter_button.setGeometry(QtCore.QRect(440, 380, 61, 51))
        self.enter_button.setStyleSheet("background: rgba(255,255,255,0)")
        self.enter_button.setText("")
        self.enter_button.setObjectName("enter_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
