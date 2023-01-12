
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Perdedor(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.img_derrota = QtWidgets.QLabel(Form)
        self.img_derrota.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.img_derrota.setText("")
        self.img_derrota.setPixmap(QtGui.QPixmap("./imagens/perdedor_forca.png"))
        self.img_derrota.setObjectName("img_derrota")

        self.play_again = QtWidgets.QPushButton(Form)
        self.play_again.setGeometry(QtCore.QRect(389, 418, 211, 41))
        self.play_again.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.play_again.setText("")
        self.play_again.setObjectName("play_again")
        self.play_again.clicked.connect(self.novamente)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Perdedor()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
