from PyQt5 import QtCore, QtGui, QtWidgets


class Hard(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.img_hard = QtWidgets.QLabel(Form)
        self.img_hard.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.img_hard.setText("")
        self.img_hard.setPixmap(QtGui.QPixmap("./imagens_telas/tela_hard.png"))
        self.img_hard.setObjectName("img_hard")

        self.placar_jogador1 = QtWidgets.QLabel(Form)
        self.placar_jogador1.setGeometry(QtCore.QRect(240, 110, 47, 41))
        self.placar_jogador1.setText("")
        self.placar_jogador1.setObjectName("placar_jogador1")

        self.placar_jogador2 = QtWidgets.QLabel(Form)
        self.placar_jogador2.setGeometry(QtCore.QRect(240, 190, 47, 41))
        self.placar_jogador2.setText("")
        self.placar_jogador2.setObjectName("placar_jogador2")
        
        self.btn_0 = QtWidgets.QPushButton(Form)
        self.btn_0.setGeometry(QtCore.QRect(387, 12, 51, 51))
        self.btn_0.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_0.setText("")
        self.btn_0.setObjectName("btn_0")

        self.btn_1 = QtWidgets.QPushButton(Form)
        self.btn_1.setGeometry(QtCore.QRect(455, 12, 51, 51))
        self.btn_1.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")

        self.btn_2 = QtWidgets.QPushButton(Form)
        self.btn_2.setGeometry(QtCore.QRect(523, 12, 51, 51))
        self.btn_2.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QPushButton(Form)
        self.btn_3.setGeometry(QtCore.QRect(590, 12, 51, 51))
        self.btn_3.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")

        self.btn_4 = QtWidgets.QPushButton(Form)
        self.btn_4.setGeometry(QtCore.QRect(659, 12, 51, 51))
        self.btn_4.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")

        self.btn_5 = QtWidgets.QPushButton(Form)
        self.btn_5.setGeometry(QtCore.QRect(387, 69, 51, 51))
        self.btn_5.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")

        self.btn_6 = QtWidgets.QPushButton(Form)
        self.btn_6.setGeometry(QtCore.QRect(455, 69, 51, 51))
        self.btn_6.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")

        self.btn_7 = QtWidgets.QPushButton(Form)
        self.btn_7.setGeometry(QtCore.QRect(523, 69, 51, 51))
        self.btn_7.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")

        self.btn_8 = QtWidgets.QPushButton(Form)
        self.btn_8.setGeometry(QtCore.QRect(591, 69, 51, 51))
        self.btn_8.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")

        self.btn_9 = QtWidgets.QPushButton(Form)
        self.btn_9.setGeometry(QtCore.QRect(658, 69, 51, 51))
        self.btn_9.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")

        self.btn_10 = QtWidgets.QPushButton(Form)
        self.btn_10.setGeometry(QtCore.QRect(387, 126, 51, 51))
        self.btn_10.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_10.setText("")
        self.btn_10.setObjectName("btn_10")

        self.btn_11 = QtWidgets.QPushButton(Form)
        self.btn_11.setGeometry(QtCore.QRect(455, 126, 51, 51))
        self.btn_11.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_11.setText("")
        self.btn_11.setObjectName("btn_11")

        self.btn_12 = QtWidgets.QPushButton(Form)
        self.btn_12.setGeometry(QtCore.QRect(523, 127, 51, 51))
        self.btn_12.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_12.setText("")
        self.btn_12.setObjectName("btn_12")

        self.btn_13 = QtWidgets.QPushButton(Form)
        self.btn_13.setGeometry(QtCore.QRect(591, 126, 51, 51))
        self.btn_13.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_13.setText("")
        self.btn_13.setObjectName("btn_13")

        self.btn_14 = QtWidgets.QPushButton(Form)
        self.btn_14.setGeometry(QtCore.QRect(658, 127, 51, 51))
        self.btn_14.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_14.setText("")
        self.btn_14.setObjectName("btn_14")

        self.btn_15 = QtWidgets.QPushButton(Form)
        self.btn_15.setGeometry(QtCore.QRect(387, 184, 51, 51))
        self.btn_15.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_15.setText("")
        self.btn_15.setObjectName("btn_15")

        self.btn_16 = QtWidgets.QPushButton(Form)
        self.btn_16.setGeometry(QtCore.QRect(455, 184, 51, 51))
        self.btn_16.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_16.setText("")
        self.btn_16.setObjectName("btn_16")

        self.btn_17 = QtWidgets.QPushButton(Form)
        self.btn_17.setGeometry(QtCore.QRect(523, 184, 51, 51))
        self.btn_17.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_17.setText("")
        self.btn_17.setObjectName("btn_17")

        self.btn_18 = QtWidgets.QPushButton(Form)
        self.btn_18.setGeometry(QtCore.QRect(591, 184, 51, 51))
        self.btn_18.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_18.setText("")
        self.btn_18.setObjectName("btn_18")

        self.btn_19 = QtWidgets.QPushButton(Form)
        self.btn_19.setGeometry(QtCore.QRect(658, 184, 51, 51))
        self.btn_19.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_19.setText("")
        self.btn_19.setObjectName("btn_19")

        self.btn_20 = QtWidgets.QPushButton(Form)
        self.btn_20.setGeometry(QtCore.QRect(387, 242, 51, 51))
        self.btn_20.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_20.setText("")
        self.btn_20.setObjectName("btn_20")

        self.btn_21 = QtWidgets.QPushButton(Form)
        self.btn_21.setGeometry(QtCore.QRect(455, 242, 51, 51))
        self.btn_21.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_21.setText("")
        self.btn_21.setObjectName("btn_21")

        self.btn_22 = QtWidgets.QPushButton(Form)
        self.btn_22.setGeometry(QtCore.QRect(523, 242, 51, 51))
        self.btn_22.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_22.setText("")
        self.btn_22.setObjectName("btn_22")

        self.btn_23 = QtWidgets.QPushButton(Form)
        self.btn_23.setGeometry(QtCore.QRect(591, 242, 51, 51))
        self.btn_23.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_23.setText("")
        self.btn_23.setObjectName("btn_23")

        self.btn_24 = QtWidgets.QPushButton(Form)
        self.btn_24.setGeometry(QtCore.QRect(659, 242, 51, 51))
        self.btn_24.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_24.setText("")
        self.btn_24.setObjectName("btn_24")

        self.btn_25 = QtWidgets.QPushButton(Form)
        self.btn_25.setGeometry(QtCore.QRect(591, 300, 51, 51))
        self.btn_25.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_25.setText("")
        self.btn_25.setObjectName("btn_25")

        self.btn_26 = QtWidgets.QPushButton(Form)
        self.btn_26.setGeometry(QtCore.QRect(387, 300, 51, 51))
        self.btn_26.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_26.setText("")
        self.btn_26.setObjectName("btn_26")

        self.btn_27 = QtWidgets.QPushButton(Form)
        self.btn_27.setGeometry(QtCore.QRect(659, 300, 51, 51))
        self.btn_27.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_27.setText("")
        self.btn_27.setObjectName("btn_27")

        self.btn_28 = QtWidgets.QPushButton(Form)
        self.btn_28.setGeometry(QtCore.QRect(455, 300, 51, 51))
        self.btn_28.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_28.setText("")
        self.btn_28.setObjectName("btn_28")

        self.btn_29 = QtWidgets.QPushButton(Form)
        self.btn_29.setGeometry(QtCore.QRect(523, 300, 51, 51))
        self.btn_29.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_29.setText("")
        self.btn_29.setObjectName("btn_29")

        self.btn_30 = QtWidgets.QPushButton(Form)
        self.btn_30.setGeometry(QtCore.QRect(591, 358, 51, 51))
        self.btn_30.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_30.setText("")
        self.btn_30.setObjectName("btn_30")

        self.btn_31 = QtWidgets.QPushButton(Form)
        self.btn_31.setGeometry(QtCore.QRect(387, 358, 51, 51))
        self.btn_31.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_31.setText("")
        self.btn_31.setObjectName("btn_31")

        self.btn_32 = QtWidgets.QPushButton(Form)
        self.btn_32.setGeometry(QtCore.QRect(455, 358, 51, 51))
        self.btn_32.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_32.setText("")
        self.btn_32.setObjectName("btn_32")

        self.btn_33 = QtWidgets.QPushButton(Form)
        self.btn_33.setGeometry(QtCore.QRect(522, 358, 51, 51))
        self.btn_33.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_33.setText("")
        self.btn_33.setObjectName("btn_33")

        self.btn_34 = QtWidgets.QPushButton(Form)
        self.btn_34.setGeometry(QtCore.QRect(659, 358, 51, 51))
        self.btn_34.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_34.setText("")
        self.btn_34.setObjectName("btn_34")

        self.btn_35 = QtWidgets.QPushButton(Form)
        self.btn_35.setGeometry(QtCore.QRect(523, 416, 51, 51))
        self.btn_35.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_35.setText("")
        self.btn_35.setObjectName("btn_35")

        self.btn_36 = QtWidgets.QPushButton(Form)
        self.btn_36.setGeometry(QtCore.QRect(388, 416, 51, 51))
        self.btn_36.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_36.setText("")
        self.btn_36.setObjectName("btn_36")

        self.btn_37 = QtWidgets.QPushButton(Form)
        self.btn_37.setGeometry(QtCore.QRect(455, 416, 51, 51))
        self.btn_37.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_37.setText("")
        self.btn_37.setObjectName("btn_37")

        self.btn_38 = QtWidgets.QPushButton(Form)
        self.btn_38.setGeometry(QtCore.QRect(590, 416, 51, 51))
        self.btn_38.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_38.setText("")
        self.btn_38.setObjectName("btn_38")
        
        self.btn_39 = QtWidgets.QPushButton(Form)
        self.btn_39.setGeometry(QtCore.QRect(659, 416, 51, 51))
        self.btn_39.setStyleSheet("background: rgba(255,255,255,0)")
        self.btn_39.setText("")
        self.btn_39.setObjectName("btn_39")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Hard()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
