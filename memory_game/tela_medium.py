
from PyQt5 import QtCore, QtGui, QtWidgets


class Medium(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.img_easy = QtWidgets.QLabel(Form)
        self.img_easy.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.img_easy.setText("")
        self.img_easy.setPixmap(QtGui.QPixmap("./imagens_telas/tela_medium.png"))
        self.img_easy.setObjectName("img_easy")

        self.placar_jogador1 = QtWidgets.QLabel(Form)
        self.placar_jogador1.setGeometry(QtCore.QRect(240, 110, 47, 41))
        self.placar_jogador1.setText("")
        self.placar_jogador1.setObjectName("placar_jogador1")

        self.placar_jogador2 = QtWidgets.QLabel(Form)
        self.placar_jogador2.setGeometry(QtCore.QRect(240, 190, 47, 41))
        self.placar_jogador2.setText("")
        self.placar_jogador2.setObjectName("placar_jogador2")

        self.bnt_0 = QtWidgets.QPushButton(Form)
        self.bnt_0.setGeometry(QtCore.QRect(388, 27, 60, 60))
        self.bnt_0.setStyleSheet("background: rgba(255,255,255,0)")
        self.bnt_0.setText("")
        self.bnt_0.setObjectName("bnt_0")

        self.btn_1 = QtWidgets.QPushButton(Form)
        self.btn_1.setGeometry(QtCore.QRect(470, 30, 60, 60))
        self.btn_1.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")

        self.btn_2 = QtWidgets.QPushButton(Form)
        self.btn_2.setGeometry(QtCore.QRect(550, 30, 60, 60))
        self.btn_2.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QPushButton(Form)
        self.btn_3.setGeometry(QtCore.QRect(635, 30, 60, 60))
        self.btn_3.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")

        self.btn_4 = QtWidgets.QPushButton(Form)
        self.btn_4.setGeometry(QtCore.QRect(387, 105, 60, 60))
        self.btn_4.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")

        self.btn_5 = QtWidgets.QPushButton(Form)
        self.btn_5.setGeometry(QtCore.QRect(470, 104, 60, 60))
        self.btn_5.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")

        self.btn_6 = QtWidgets.QPushButton(Form)
        self.btn_6.setGeometry(QtCore.QRect(553, 105, 60, 60))
        self.btn_6.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")

        self.btn_7 = QtWidgets.QPushButton(Form)
        self.btn_7.setGeometry(QtCore.QRect(635, 105, 60, 60))
        self.btn_7.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")

        self.btn_8 = QtWidgets.QPushButton(Form)
        self.btn_8.setGeometry(QtCore.QRect(387, 180, 60, 60))
        self.btn_8.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")

        self.btn_9 = QtWidgets.QPushButton(Form)
        self.btn_9.setGeometry(QtCore.QRect(470, 181, 60, 60))
        self.btn_9.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")

        self.btn_10 = QtWidgets.QPushButton(Form)
        self.btn_10.setGeometry(QtCore.QRect(553, 182, 60, 60))
        self.btn_10.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_10.setText("")
        self.btn_10.setObjectName("btn_10")

        self.btn_11 = QtWidgets.QPushButton(Form)
        self.btn_11.setGeometry(QtCore.QRect(634, 182, 60, 60))
        self.btn_11.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_11.setText("")
        self.btn_11.setObjectName("btn_11")
        
        self.btn_12 = QtWidgets.QPushButton(Form)
        self.btn_12.setGeometry(QtCore.QRect(387, 260, 60, 60))
        self.btn_12.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_12.setText("")
        self.btn_12.setObjectName("btn_12")

        self.btn_13 = QtWidgets.QPushButton(Form)
        self.btn_13.setGeometry(QtCore.QRect(470, 260, 60, 60))
        self.btn_13.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_13.setText("")
        self.btn_13.setObjectName("btn_13")

        self.btn_14 = QtWidgets.QPushButton(Form)
        self.btn_14.setGeometry(QtCore.QRect(552, 260, 60, 60))
        self.btn_14.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_14.setText("")
        self.btn_14.setObjectName("btn_14")

        self.btn_15 = QtWidgets.QPushButton(Form)
        self.btn_15.setGeometry(QtCore.QRect(635, 261, 60, 60))
        self.btn_15.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_15.setText("")
        self.btn_15.setObjectName("btn_15")

        self.btn_16 = QtWidgets.QPushButton(Form)
        self.btn_16.setGeometry(QtCore.QRect(387, 337, 60, 60))
        self.btn_16.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_16.setText("")
        self.btn_16.setObjectName("btn_16")

        self.btn_17 = QtWidgets.QPushButton(Form)
        self.btn_17.setGeometry(QtCore.QRect(470, 337, 60, 60))
        self.btn_17.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_17.setText("")
        self.btn_17.setObjectName("btn_17")

        self.btn_18 = QtWidgets.QPushButton(Form)
        self.btn_18.setGeometry(QtCore.QRect(553, 337, 60, 60))
        self.btn_18.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_18.setText("")
        self.btn_18.setObjectName("btn_18")

        self.btn_19 = QtWidgets.QPushButton(Form)
        self.btn_19.setGeometry(QtCore.QRect(635, 338, 60, 60))
        self.btn_19.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_19.setText("")
        self.btn_19.setObjectName("btn_19")

        self.btn_20 = QtWidgets.QPushButton(Form)
        self.btn_20.setGeometry(QtCore.QRect(387, 414, 60, 60))
        self.btn_20.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_20.setText("")
        self.btn_20.setObjectName("btn_20")

        self.btn_21 = QtWidgets.QPushButton(Form)
        self.btn_21.setGeometry(QtCore.QRect(469, 415, 60, 60))
        self.btn_21.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_21.setText("")
        self.btn_21.setObjectName("btn_21")

        self.btn_22 = QtWidgets.QPushButton(Form)
        self.btn_22.setGeometry(QtCore.QRect(552, 417, 60, 60))
        self.btn_22.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_22.setText("")
        self.btn_22.setObjectName("btn_22")
        
        self.btn_23 = QtWidgets.QPushButton(Form)
        self.btn_23.setGeometry(QtCore.QRect(635, 416, 60, 60))
        self.btn_23.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_23.setText("")
        self.btn_23.setObjectName("btn_23")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Medium()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
