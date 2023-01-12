from PyQt5 import QtCore, QtGui, QtWidgets


class Velha(object):
    def setupUi(self, Form):
        Form.setObjectName("TIC-TAC-TOE")
        Form.resize(800, 500)
        
        self.forma_usuario = 'X'
        self.forma_pc = 'O'
        self.placar_usuario = 0
        self.placar_pc = 0
        self.placar_velha = 0
        self.vez = 'jogador1'
        self.titulo="JOGO DA VELHA"
        self.botao_a1_bool = False
        self.botao_a2_bool = False
        self.botao_a3_bool = False
        self.botao_b1_bool = False
        self.botao_b2_bool = False
        self.botao_b3_bool = False
        self.botao_c1_bool = False
        self.botao_c2_bool = False
        self.botao_c3_bool = False
        
        self.imagem_velha = QtWidgets.QLabel(Form)
        self.imagem_velha.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.imagem_velha.setText("")
        self.imagem_velha.setPixmap(QtGui.QPixmap("./imagens/velha.png"))
        self.imagem_velha.setScaledContents(True)
        self.imagem_velha.setObjectName("imagem_velha")

        self.botao_1 = QtWidgets.QPushButton(Form)
        self.botao_1.setGeometry(QtCore.QRect(454, 160, 81, 91))
        self.botao_1.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_1.setText("")
        self.botao_1.clicked.connect(lambda : self.escolha_usuario(1))
        self.botao_1.setObjectName("botao_1")

        self.botao_2 = QtWidgets.QPushButton(Form)
        self.botao_2.setGeometry(QtCore.QRect(560, 160, 91, 91))
        self.botao_2.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_2.setText("")
        self.botao_2.clicked.connect(lambda : self.escolha_usuario(2))
        self.botao_2.setObjectName("botao_2")

        self.botao_3 = QtWidgets.QPushButton(Form)
        self.botao_3.setGeometry(QtCore.QRect(670, 160, 81, 91))
        self.botao_3.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_3.setText("")
        self.botao_3.clicked.connect(lambda : self.escolha_usuario(3))
        self.botao_3.setObjectName("botao_3")

        self.botao_4 = QtWidgets.QPushButton(Form)
        self.botao_4.setGeometry(QtCore.QRect(460, 260, 81, 81))
        self.botao_4.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_4.setText("")
        self.botao_4.clicked.connect(lambda : self.escolha_usuario(4))
        self.botao_4.setObjectName("botao_4")

        self.botao_5 = QtWidgets.QPushButton(Form)
        self.botao_5.setGeometry(QtCore.QRect(550, 260, 101, 81))
        self.botao_5.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_5.setText("")
        self.botao_5.clicked.connect(lambda : self.escolha_usuario(5))
        self.botao_5.setObjectName("botao_5")

        self.botao_6 = QtWidgets.QPushButton(Form)
        self.botao_6.setGeometry(QtCore.QRect(670, 260, 81, 81))
        self.botao_6.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_6.setText("")
        self.botao_6.clicked.connect(lambda : self.escolha_usuario(6))
        self.botao_6.setObjectName("botao_6")

        self.botao_7 = QtWidgets.QPushButton(Form)
        self.botao_7.setGeometry(QtCore.QRect(450, 360, 101, 71))
        self.botao_7.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_7.setText("")
        self.botao_7.clicked.connect(lambda : self.escolha_usuario(7))
        self.botao_7.setObjectName("botao_7")

        self.botao_8 = QtWidgets.QPushButton(Form)
        self.botao_8.setGeometry(QtCore.QRect(550, 360, 101, 71))
        self.botao_8.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_8.setText("")
        self.botao_8.clicked.connect(lambda : self.escolha_usuario(8))
        self.botao_8.setObjectName("botao_8")

        self.botao_9 = QtWidgets.QPushButton(Form)
        self.botao_9.setGeometry(QtCore.QRect(670, 360, 101, 71))
        self.botao_9.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_9.setText("")
        self.botao_9.clicked.connect(lambda : self.escolha_usuario(9))
        self.botao_9.setObjectName("botao_9")

        self.botao_reset = QtWidgets.QPushButton(Form)
        self.botao_reset.setGeometry(QtCore.QRect(30, 440, 121, 31))
        self.botao_reset.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.botao_reset.setText("")
        self.botao_reset.clicked.connect(self.resetar_jogo)
        self.botao_reset.setObjectName("botao_reset")

        self.placar_vencedorO = QtWidgets.QLabel(Form)
        self.placar_vencedorO.setGeometry(QtCore.QRect(145, 235, 71, 61))
        self.placar_vencedorO.setText("")
        self.placar_vencedorO.setObjectName("placar_vencedorO")
        self.placar_vencedorO.setStyleSheet('QLabel {color: "red"; font: 50px;}')

        self.placar_vencedorX = QtWidgets.QLabel(Form)
        self.placar_vencedorX.setGeometry(QtCore.QRect(145, 150, 71, 61))
        self.placar_vencedorX.setText("")
        self.placar_vencedorX.setObjectName("placar_vencedorX")
        self.placar_vencedorX.setStyleSheet('QLabel {color: "black"; font: 50px}')
        
        self.lbl_velha = QtWidgets.QLabel(Form)
        self.lbl_velha.move(590, 70)
        self.lbl_velha.resize(110, 50)
        self.lbl_velha.setText('VELHA')
        self.lbl_velha.setStyleSheet('QLabel {color: "yellow"; font: 35px}')
        self.lbl_velha.setObjectName("lbl_velha")
        self.lbl_velha.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("TIC-TAC-TOE", "TIC-TAC-TOE"))
    
    
    def escolha_usuario(self, botao):
        if self.vez == 'jogador1':
            if botao == 1:
                self.botao_1.setText("X")
                self.botao_1.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_a1_bool = True
                self.botao_1.setStyleSheet('QPushButton {font:80px bold; color: "black"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 2:
                self.botao_2.setText("X")
                self.botao_2.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_a2_bool = True
                self.botao_2.setStyleSheet('QPushButton {font:80px bold; color: "black"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 3:
                self.botao_3.setText("X")
                self.botao_3.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_a3_bool = True
                self.botao_3.setStyleSheet('QPushButton {font:80px bold; color: "black"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 4:
                self.botao_4.setText("X")
                self.botao_4.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_b1_bool = True
                self.botao_4.setStyleSheet('QPushButton {font:80px bold; color: "black"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 5:
                self.botao_5.setText("X")
                self.botao_5.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_b2_bool = True
                self.botao_5.setStyleSheet('QPushButton {font:80px bold; color: "black"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 6:
                self.botao_6.setText("X")
                self.botao_6.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_b3_bool = True
                self.botao_6.setStyleSheet('QPushButton {font:80px bold; color: "black"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 7:
                self.botao_7.setText("X")
                self.botao_7.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_c1_bool = True
                self.botao_7.setStyleSheet('QPushButton {font:80px bold; color: "black"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 8:
                self.botao_8.setText("X")
                self.botao_8.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_c2_bool = True
                self.botao_8.setStyleSheet('QPushButton {font:80px bold; color: "black"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 9:
                self.botao_9.setText("X")
                self.botao_9.setDisabled(True)
                self.vez = 'jogador2'
                self.botao_c3_bool = True
                self.botao_9.setStyleSheet('QPushButton {font:80px bold; color: "black"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            
            if self.verificar_vencedor_x():
                self.placar_usuario += 1
                self.placar_vencedorX.setText(str(self.placar_usuario))
                self.botao_1.setDisabled(True)
                self.botao_2.setDisabled(True)
                self.botao_3.setDisabled(True)
                self.botao_4.setDisabled(True)
                self.botao_5.setDisabled(True)
                self.botao_6.setDisabled(True)
                self.botao_7.setDisabled(True)
                self.botao_8.setDisabled(True)
                self.botao_9.setDisabled(True)
            else:
                if self.botao_a1_bool == True and self.botao_a2_bool == True and self.botao_a3_bool == True and self.botao_b1_bool == True and self.botao_b2_bool == True and self.botao_b3_bool == True and self.botao_c1_bool == True and self.botao_c2_bool == True and self.botao_c3_bool == True:
                    self.verificar_velha()

        else:
            if botao == 1:
                self.botao_1.setText("O")
                self.botao_1.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_a1_bool = True
                self.botao_1.setStyleSheet('QPushButton {font:80px bold; color: "red"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 2:
                self.botao_2.setText("O")
                self.botao_2.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_a2_bool = True
                self.botao_2.setStyleSheet('QPushButton {font:80px bold; color: "red"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 3:
                self.botao_3.setText("O")
                self.botao_3.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_a3_bool = True
                self.botao_3.setStyleSheet('QPushButton {font:80px bold; color: "red"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 4:
                self.botao_4.setText("O")
                self.botao_4.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_b1_bool = True
                self.botao_4.setStyleSheet('QPushButton {font:80px bold; color: "red"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 5:
                self.botao_5.setText("O")
                self.botao_5.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_b2_bool = True
                self.botao_5.setStyleSheet('QPushButton {font:80px bold; color: "red"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 6:
                self.botao_6.setText("O")
                self.botao_6.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_b3_bool = True
                self.botao_6.setStyleSheet('QPushButton {font:80px bold; color: "red"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 7:
                self.botao_7.setText("O")
                self.botao_7.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_c1_bool = True
                self.botao_7.setStyleSheet('QPushButton {font:80px bold; color: "red"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 8:
                self.botao_8.setText("O")
                self.botao_8.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_c2_bool = True
                self.botao_8.setStyleSheet('QPushButton {font:80px bold; color: "red"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            elif botao == 9:
                self.botao_9.setText("O")
                self.botao_9.setDisabled(True)
                self.vez = 'jogador1'
                self.botao_c3_bool = True
                self.botao_9.setStyleSheet('QPushButton {font:80px bold; color: "red"; border:2px solid transparent; background: "transparent"; border-radius:10px;}')
            
            if self.verificar_vencedor_o():
                self.placar_pc += 1
                self.placar_vencedorO.setText(str(self.placar_pc))
                self.botao_1.setDisabled(True)
                self.botao_2.setDisabled(True)
                self.botao_3.setDisabled(True)
                self.botao_4.setDisabled(True)
                self.botao_5.setDisabled(True)
                self.botao_6.setDisabled(True)
                self.botao_7.setDisabled(True)
                self.botao_8.setDisabled(True)
                self.botao_9.setDisabled(True)
                
            else: 
                if self.botao_a1_bool == True and self.botao_a2_bool == True and self.botao_a3_bool == True and self.botao_b1_bool == True and self.botao_b2_bool == True and self.botao_b3_bool == True and self.botao_c1_bool == True and self.botao_c2_bool == True and self.botao_c3_bool == True:
                    self.verificar_velha()


    def verificar_vencedor_x(self):
        if self.botao_1.text() == "X" and self.botao_2.text() == "X" and self.botao_3.text() == "X":
            return True
        elif self.botao_4.text() == "X" and self.botao_5.text()  == "X" and self.botao_6.text() == "X":
            return True
        elif self.botao_7.text() == "X" and self.botao_8.text() == "X" and self.botao_9.text() == "X":
            return True
        elif self.botao_1.text() == "X" and self.botao_4.text() == "X" and self.botao_7.text() == "X":
            return True
        elif self.botao_2.text() == "X" and self.botao_5.text() == "X" and self.botao_8.text() == "X":
            return True
        elif self.botao_3.text() == "X" and self.botao_6.text() == "X" and self.botao_9.text() == "X":
            return True
        elif self.botao_1.text() == "X" and self.botao_5.text() == "X" and self.botao_9.text() == "X":
            return True
        elif self.botao_3.text() == "X" and self.botao_5.text() == "X" and self.botao_7.text() == "X":
            return True
        else:
            return False


    def verificar_vencedor_o(self):
        if self.botao_1.text() == "O" and self.botao_2.text() == "O" and self.botao_3.text() == "O":
            return True
        elif self.botao_4.text() == "O" and self.botao_5.text()  == "O" and self.botao_6.text() == "O":
            return True
        elif self.botao_7.text() == "O" and self.botao_8.text() == "O" and self.botao_9.text() == "O":
            return True
        elif self.botao_1.text() == "O" and self.botao_4.text() == "O" and self.botao_7.text() == "O":
            return True
        elif self.botao_2.text() == "O" and self.botao_5.text() == "O" and self.botao_8.text() == "O":
            return True
        elif self.botao_3.text() == "O" and self.botao_6.text() == "O" and self.botao_9.text() == "O":
            return True
        elif self.botao_1.text() == "O" and self.botao_5.text() == "O" and self.botao_9.text() == "O":
            return True
        elif self.botao_3.text() == "O" and self.botao_5.text() == "O" and self.botao_7.text() == "O":
            return True
        else:
            return False


    def verificar_velha(self):
        self.lbl_velha.show()
    
    
    def resetar_jogo(self):
            self.vez = 'jogador1'
            self.botao_1.setDisabled(False)
            self.botao_2.setDisabled(False)
            self.botao_3.setDisabled(False)
            self.botao_4.setDisabled(False)
            self.botao_5.setDisabled(False)
            self.botao_6.setDisabled(False)
            self.botao_7.setDisabled(False)
            self.botao_8.setDisabled(False)
            self.botao_9.setDisabled(False)

            self.botao_1.setText("")
            self.botao_2.setText("")
            self.botao_3.setText("")
            self.botao_4.setText("")
            self.botao_5.setText("")
            self.botao_6.setText("")
            self.botao_7.setText("")
            self.botao_8.setText("")
            self.botao_9.setText("")

            self.botao_a1_bool = False
            self.botao_a2_bool = False
            self.botao_a3_bool = False
            self.botao_b1_bool = False
            self.botao_b2_bool = False
            self.botao_b3_bool = False
            self.botao_c1_bool = False
            self.botao_c2_bool = False
            self.botao_c3_bool = False
            
            self.lbl_velha.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Velha()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
