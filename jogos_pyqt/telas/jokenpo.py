from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint

class Jokenpo(object):
    def setupUi(self, Form):
        Form.setObjectName("JOKENPO")
        Form.resize(800, 500)
        self.placar_jogador = 0
        self.placar_computador = 0
        self.jogada_usuario = ""
        self.jogada_computador = ""
        self.vencedor = False
        self.opcoes = ("Pedra", "Papel", "Tesoura")

        self.imagem_jokenpo = QtWidgets.QLabel(Form)
        self.imagem_jokenpo.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.imagem_jokenpo.setText("DERROTA")
        self.imagem_jokenpo.setPixmap(QtGui.QPixmap("./imagens/jokenpo.png"))
        self.imagem_jokenpo.setScaledContents(True)
        self.imagem_jokenpo.setObjectName("imagem_jokenpo")

        self.label_resultado_derrota = QtWidgets.QLabel(Form)
        self.label_resultado_derrota.setGeometry(QtCore.QRect(60, 200, 161, 71))
        self.label_resultado_derrota.setText("DERROTA")
        self.label_resultado_derrota.setStyleSheet("font: 30px; color: 'red'")
        self.label_resultado_derrota.hide()

        self.label_resultado_vitoria = QtWidgets.QLabel(Form)
        self.label_resultado_vitoria.setGeometry(QtCore.QRect(60, 200, 161, 71))
        self.label_resultado_vitoria.setText("VITÓRIA")
        self.label_resultado_vitoria.setStyleSheet("font: 30px; color: 'green'")
        self.label_resultado_vitoria.hide()

        self.label_resultado_empate = QtWidgets.QLabel(Form)
        self.label_resultado_empate.setGeometry(QtCore.QRect(60, 200, 161, 71))
        self.label_resultado_empate.setText("EMPATE")
        self.label_resultado_empate.setStyleSheet("font: 30px; color: 'yellow'")
        self.label_resultado_empate.hide()

        self.placar_usuario = QtWidgets.QLabel(Form)
        self.placar_usuario.setGeometry(QtCore.QRect(420, 30, 47, 51))
        self.placar_usuario.setText(str(self.placar_jogador))
        self.placar_usuario.setStyleSheet("font: 30px; color: 'blue'")
        self.placar_usuario.setObjectName("placar_usuario")

        self.placar_pc = QtWidgets.QLabel(Form)
        self.placar_pc.setGeometry(QtCore.QRect(520, 30, 47, 51))
        self.placar_pc.setText(str(self.placar_computador))
        self.placar_pc.setStyleSheet("font: 30px; color: 'red'")
        self.placar_pc.setObjectName("placar_pc")

        self.botao_pedra = QtWidgets.QPushButton(Form)
        self.botao_pedra.setGeometry(QtCore.QRect(320, 360, 111, 100))
        self.botao_pedra.setStyleSheet("background: rgba(255, 255, 255, 0); border: 2px solid white;border-radius: 10px")
        self.botao_pedra.setText("")
        self.botao_pedra.clicked.connect(lambda: self.jogada(0))
        self.botao_pedra.setObjectName("botao_pedra")


        self.botao_papel = QtWidgets.QPushButton(Form)
        self.botao_papel.setGeometry(QtCore.QRect(480, 360, 111, 100))
        self.botao_papel.setStyleSheet("background: rgba(255, 255, 255, 0); border: 2px solid white;border-radius: 10px")
        self.botao_papel.setText("")
        self.botao_papel.clicked.connect(lambda: self.jogada(1))
        self.botao_papel.setObjectName("botao_papel")


        self.botao_tesoura = QtWidgets.QPushButton(Form)
        self.botao_tesoura.setGeometry(QtCore.QRect(650, 360, 111, 100))
        self.botao_tesoura.setStyleSheet("background: rgba(255, 255, 255, 0); border: 2px solid white;border-radius: 10px")
        self.botao_tesoura.setText("")
        self.botao_tesoura.clicked.connect(lambda: self.jogada(2))
        self.botao_tesoura.setObjectName("botao_tesoura")


        self.escolha_usuario = QtWidgets.QLabel(Form)
        self.escolha_usuario.setGeometry(QtCore.QRect(320, 170, 121, 101))
        self.escolha_usuario.setText("")
        self.escolha_usuario.setScaledContents(True)
        self.escolha_usuario.setPixmap(QtGui.QPixmap("./imagens_ppt/tesoura.png"))
        self.escolha_usuario.setObjectName("escolha_usuario")
        self.escolha_usuario.hide()

        self.escolha_pc = QtWidgets.QLabel(Form)
        self.escolha_pc.setGeometry(QtCore.QRect(540, 170, 121, 101))
        self.escolha_pc.setText("")
        self.escolha_pc.setScaledContents(True)
        self.escolha_pc.setPixmap(QtGui.QPixmap("./imagens_ppt/tesoura.png"))
        self.escolha_pc.setObjectName("escolha_pc")
        self.escolha_pc.hide()

        self.botao_playagain = QtWidgets.QPushButton(Form)
        self.botao_playagain.setGeometry(QtCore.QRect(50, 450, 155, 30))
        self.botao_playagain.setStyleSheet("background: 'transparent'")
        self.botao_playagain.setText("")
        self.botao_playagain.clicked.connect(self.playagain)
        self.botao_playagain.setObjectName("botao_playagain")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("JOKENPO", "JOKENPO"))

    def verificar_vencedor(self):
        if self.jogada_computador == "Pedra":  # jogou pedra
            if self.jogada_usuario == "Papel":
                self.label_resultado_vitoria.show()
                self.placar_jogador += 1
                self.placar_usuario.setText(str(self.placar_jogador))
                
            elif self.jogada_usuario == "Tesoura":
                self.label_resultado_derrota.show()
                self.placar_computador += 1
                self.placar_pc.setText(str(self.placar_computador))
            elif self.jogada_computador == self.jogada_usuario:
                self.label_resultado_empate.show()
                
        elif self.jogada_computador == "Papel":  # jogou papel
            if self.jogada_usuario == "Pedra":
                self.label_resultado_derrota.show()
                self.placar_computador += 1
                self.placar_pc.setText(str(self.placar_computador))
                self.vencedor = False
            elif self.jogada_usuario == "Tesoura":
                self.label_resultado_vitoria.show()
                self.placar_jogador += 1
                self.placar_usuario.setText(str(self.placar_jogador))
            elif self.jogada_computador == self.jogada_usuario:
                self.label_resultado_empate.show()
                

        elif self.jogada_computador == "Tesoura":  # jogou tesoura
            if self.jogada_usuario == "Pedra":
                self.label_resultado_vitoria.show()
                self.placar_jogador += 1
                self.placar_usuario.setText(str(self.placar_jogador))
                

            elif self.jogada_usuario == "Papel":
                self.label_resultado_derrota.show()
                self.placar_computador += 1
                self.placar_pc.setText(str(self.placar_computador))
            
            elif self.jogada_computador == self.jogada_usuario:
                self.label_resultado_empate.show()
        

    def sortear_jogada(self):
        computador = randint(0, 2)
        imagens = ("imagens_ppt/pedra.png", "imagens_ppt/papel.png", "imagens_ppt/tesoura.png")
        self.escolha_pc.setPixmap(QtGui.QPixmap(imagens[computador]))

        self.jogada_computador = self.opcoes[computador]
        if self.jogada_computador == 'Pedra':
            self.escolha_pc.setScaledContents(True)
            self.escolha_pc.setPixmap(QtGui.QPixmap("./imagens_ppt/pedra.png"))
            self.escolha_pc.show()
        elif self.jogada_computador == 'Papel':
            self.escolha_pc.setScaledContents(True)
            self.escolha_pc.setPixmap(QtGui.QPixmap("./imagens_ppt/papel.png"))
            self.escolha_pc.show()
        elif self.jogada_computador == 'Tesoura':
            self.escolha_pc.setScaledContents(True)
            self.escolha_pc.setPixmap(QtGui.QPixmap("./imagens_ppt/tesoura.png"))
            self.escolha_pc.show()

        self.verificar_vencedor()
        

    def jogada(self, escolha):
        self.opcoes = ("Pedra", "Papel", "Tesoura")
        self.jogada_usuario = self.opcoes[escolha]
        self.resposta_jogador = self.jogada_usuario

        if self.jogada_usuario == 'Pedra':
            self.escolha_usuario.setScaledContents(True)
            self.escolha_usuario.setPixmap(QtGui.QPixmap("./imagens_ppt/pedra.png"))
            self.escolha_usuario.show()
            self.label_resultado_derrota.hide()
            self.label_resultado_empate.hide()
            self.label_resultado_vitoria.hide()
            
        elif self.jogada_usuario == 'Papel':
            self.escolha_usuario.setScaledContents(True)
            self.escolha_usuario.setPixmap(QtGui.QPixmap("./imagens_ppt/papel.png"))
            self.escolha_usuario.show()
            self.label_resultado_derrota.hide()
            self.label_resultado_empate.hide()
            self.label_resultado_vitoria.hide()

        elif self.jogada_usuario == 'Tesoura':
            self.escolha_usuario.setScaledContents(True)
            self.escolha_usuario.setPixmap(QtGui.QPixmap("./imagens_ppt/tesoura.png"))
            self.escolha_usuario.show()
            self.label_resultado_derrota.hide()
            self.label_resultado_empate.hide()
            self.label_resultado_vitoria.hide()
        self.sortear_jogada()


    def playagain(self):
        self.escolha_usuario.hide()
        self.escolha_pc.hide()

        self.label_resultado_derrota.hide()
        self.label_resultado_empate.hide()
        self.label_resultado_vitoria.hide()

        self.placar_jogador = 0
        self.placar_computador = 0
        self.placar_usuario.setText(str(self.placar_jogador))
        self.placar_pc.setText(str(self.placar_computador))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Jokenpo()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
