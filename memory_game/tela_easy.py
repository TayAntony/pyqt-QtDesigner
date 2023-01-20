from PyQt5 import QtCore, QtGui, QtWidgets

class Easy(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.img_easy = QtWidgets.QLabel(Form)
        self.img_easy.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.img_easy.setText("")
        self.img_easy.setPixmap(QtGui.QPixmap("./imagens_telas/tela_easy.png"))
        self.img_easy.setObjectName("img_easy")

        self.btn_0 = QtWidgets.QPushButton(Form)
        self.btn_0.setGeometry(QtCore.QRect(365, 66, 69, 68))
        self.btn_0.setStyleSheet("QPushButton{\n background-image: url(./cartas_memoria/easy/gnar.png);\n border-radius: 10px; background-size:cover; background-repeat:no-repeat;}")
        self.btn_0.setText("")
        self.btn_0.setObjectName("btn_0")

        self.btn_1 = QtWidgets.QPushButton(Form)
        self.btn_1.setGeometry(QtCore.QRect(464, 66, 69, 68))
        self.btn_1.setStyleSheet("QPushButton{\n background-image: url(./cartas_memoria/easy/poppy.png);\n border-radius: 10px; background-size:cover; background-repeat:no-repeat;}")
        self.btn_1.setText("")
        self.btn_1.setObjectName("")

        self.btn_2 = QtWidgets.QPushButton(Form)
        self.btn_2.setGeometry(QtCore.QRect(570, 66, 69, 68))
        self.btn_2.setStyleSheet("QPushButton{\n background-image: url(./cartas_memoria/easy/lulu.png);\n border-radius: 10px; background-size:cover; background-repeat:no-repeat;}")
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QPushButton(Form)
        self.btn_3.setGeometry(QtCore.QRect(365, 164, 69, 68))
        self.btn_3.setStyleSheet("QPushButton{\n background-image: url(./cartas_memoria/easy/tristana.png);\n border-radius: 10px; background-size:cover; background-repeat:no-repeat;}")
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")

        self.btn_4 = QtWidgets.QPushButton(Form)
        self.btn_4.setGeometry(QtCore.QRect(468, 164, 69, 68))
        self.btn_4.setStyleSheet("QPushButton{\n background-image: url(./cartas_memoria/easy/yuumi_easy.png);\n border-radius: 10px; background-size:cover; background-repeat:no-repeat;}")
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")

        self.btn_5 = QtWidgets.QPushButton(Form)
        self.btn_5.setGeometry(QtCore.QRect(568, 165, 69, 68))
        self.btn_5.setStyleSheet("QPushButton{\n background-image: url(./cartas_memoria/easy/teemo.png);\n border-radius: 10px; background-size:cover; background-repeat:no-repeat;}")
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")

        self.btn_6 = QtWidgets.QPushButton(Form)
        self.btn_6.setGeometry(QtCore.QRect(364, 252, 69, 68))
        self.btn_6.setStyleSheet("background-image: url(./cartas_memoria/easy/.png); border-radius: 10px")
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")

        self.btn_7 = QtWidgets.QPushButton(Form)
        self.btn_7.setGeometry(QtCore.QRect(467, 252, 69, 68))
        self.btn_7.setStyleSheet("background-image: url(./cartas_memoria/easy/.png); border-radius: 10px")
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")

        self.btn_8 = QtWidgets.QPushButton(Form)
        self.btn_8.setGeometry(QtCore.QRect(569, 252, 69, 68))
        self.btn_8.setStyleSheet("background-image: url(./cartas_memoria/easy/.png); border-radius: 10px")
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")

        self.btn_9 = QtWidgets.QPushButton(Form)
        self.btn_9.setGeometry(QtCore.QRect(364, 349, 69, 68))
        self.btn_9.setStyleSheet("background-image: url(./cartas_memoria/easy/.png); border-radius: 10px")
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")

        self.btn_10 = QtWidgets.QPushButton(Form)
        self.btn_10.setGeometry(QtCore.QRect(466, 349, 69, 68))
        self.btn_10.setStyleSheet("background-image: url(./cartas_memoria/easy/.png); border-radius: 10px")
        self.btn_10.setText("")
        self.btn_10.setObjectName("btn_10")

        self.btn_11 = QtWidgets.QPushButton(Form)
        self.btn_11.setGeometry(QtCore.QRect(567, 349, 69, 68))
        self.btn_11.setStyleSheet("background-image: url(./cartas_memoria/easy/.png); border-radius: 10px")
        self.btn_11.setText("")
        self.btn_11.setObjectName("btn_11")

        self.placar_jogador1 = QtWidgets.QLabel(Form)
        self.placar_jogador1.setGeometry(QtCore.QRect(240, 110, 47, 41))
        self.placar_jogador1.setText("")
        self.placar_jogador1.setObjectName("placar_jogador1")

        self.placar_jogador2 = QtWidgets.QLabel(Form)
        self.placar_jogador2.setGeometry(QtCore.QRect(240, 190, 47, 41))
        self.placar_jogador2.setText("")
        self.placar_jogador2.setObjectName("placar_jogador2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Easy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Easy()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
