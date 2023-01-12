from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Vencedor(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.img_vencedor = QtWidgets.QLabel(Form)
        self.img_vencedor.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.img_vencedor.setText("")
        self.img_vencedor.setPixmap(QtGui.QPixmap("./imagens/vencedor_forca.png"))
        self.img_vencedor.setObjectName("img_vencedor")

        self.play_again = QtWidgets.QPushButton(Form)
        self.play_again.setGeometry(QtCore.QRect(10, 184, 211, 41))
        self.play_again.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.play_again.setText("")
        self.play_again.setObjectName("play_again")
        self.play_again.clicked.connect(self.novamente)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def novamente(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Vencedor()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
