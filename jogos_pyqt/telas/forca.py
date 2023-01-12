from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys

from perdedor import Perdedor
from vencedor import Vencedor


class Forca(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.vidas = 5
        self.lista_chutes = []

        self.imagen_forca = QtWidgets.QLabel(Form)
        self.imagen_forca.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.imagen_forca.setText("")
        self.imagen_forca.setPixmap(QtGui.QPixmap("./imagens/forca.png"))
        self.imagen_forca.setScaledContents(True)
        self.imagen_forca.setObjectName("imagen_forca")

        self.label_dica = QtWidgets.QLabel(Form)
        self.label_dica.setGeometry(QtCore.QRect(140, 235, 641, 31))
        self.label_dica.setText("dica 123")
        self.label_dica.setObjectName("label_dica")
        self.label_dica.setStyleSheet("font: 26px; color: 'white'")
        self.label_dica.hide()

        self.label_chutes = QtWidgets.QLabel(Form)
        self.label_chutes.setGeometry(QtCore.QRect(180, 290, 241, 171))
        self.label_chutes.setText("")
        self.label_chutes.setObjectName("label_chutes")
        self.label_chutes.setStyleSheet("font: 26px; color: 'white'")

        self.label_vidas = QtWidgets.QLabel(Form)
        self.label_vidas.setGeometry(QtCore.QRect(145, 52, 61, 51))
        self.label_vidas.setText("5")
        self.label_vidas.setObjectName("label_vidas")
        self.label_vidas.setStyleSheet("font: 50px; color: 'white'")
        self.label_vidas.hide()

        self.palavra_sorteada = QtWidgets.QLabel(Form)
        self.palavra_sorteada.setGeometry(QtCore.QRect(100, 150, 651, 41))
        self.palavra_sorteada.setText(''.join(""))
        self.palavra_sorteada.setObjectName("palavra_sorteada")
        self.palavra_sorteada.setStyleSheet("font: 36px; color: 'white'")
        self.palavra_sorteada.hide()

        self.play_again = QtWidgets.QPushButton(Form)
        self.play_again.setGeometry(QtCore.QRect(240, 50, 190, 35))
        self.play_again.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.play_again.setText("")
        self.play_again.setObjectName("play_again")
        self.play_again.clicked.connect(lambda : self.sortear_palavra())


        self.botao_a = QtWidgets.QPushButton(Form)
        self.botao_a.setGeometry(QtCore.QRect(446, 290, 38, 36))
        self.botao_a.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_a.setText("")
        self.botao_a.setObjectName("botao_a")
        self.botao_a.clicked.connect(lambda : self.chutes('a'))
        self.botao_a.setDisabled(True)

        self.botao_b = QtWidgets.QPushButton(Form)
        self.botao_b.setGeometry(QtCore.QRect(497, 290, 37, 36))
        self.botao_b.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_b.setText("")
        self.botao_b.setObjectName("botao_b")
        self.botao_b.clicked.connect(lambda : self.chutes('b'))

        self.botao_c = QtWidgets.QPushButton(Form)
        self.botao_c.setGeometry(QtCore.QRect(546, 290, 38, 36))
        self.botao_c.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_c.setText("")
        self.botao_c.setObjectName("botao_c")
        self.botao_c.clicked.connect(lambda : self.chutes('c'))

        self.botao_d = QtWidgets.QPushButton(Form)
        self.botao_d.setGeometry(QtCore.QRect(594, 290, 38, 36))
        self.botao_d.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_d.setText("")
        self.botao_d.setObjectName("botao_d")
        self.botao_d.clicked.connect(lambda : self.chutes('d'))

        self.botao_e = QtWidgets.QPushButton(Form)
        self.botao_e.setGeometry(QtCore.QRect(643, 290, 38, 36))
        self.botao_e.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_e.setText("")
        self.botao_e.setObjectName("botao_e")
        self.botao_e.clicked.connect(lambda : self.chutes('e'))


        self.botao_f = QtWidgets.QPushButton(Form)
        self.botao_f.setGeometry(QtCore.QRect(693, 290, 38, 36))
        self.botao_f.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_f.setText("")
        self.botao_f.setObjectName("botao_f")
        self.botao_f.clicked.connect(lambda : self.chutes('f'))

        self.botao_g = QtWidgets.QPushButton(Form)
        self.botao_g.setGeometry(QtCore.QRect(740, 290, 38, 36))
        self.botao_g.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_g.setText("")
        self.botao_g.setObjectName("botao_g")
        self.botao_g.clicked.connect(lambda : self.chutes('g'))

        self.botao_h = QtWidgets.QPushButton(Form)
        self.botao_h.setGeometry(QtCore.QRect(448, 339, 38, 36))
        self.botao_h.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_h.setText("")
        self.botao_h.setObjectName("botao_h")
        self.botao_h.clicked.connect(lambda : self.chutes('h'))

        self.botao_i = QtWidgets.QPushButton(Form)
        self.botao_i.setGeometry(QtCore.QRect(497, 339, 38, 36))
        self.botao_i.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_i.setText("")
        self.botao_i.setObjectName("botao_i")
        self.botao_i.clicked.connect(lambda : self.chutes('i'))

        self.botao_j = QtWidgets.QPushButton(Form)
        self.botao_j.setGeometry(QtCore.QRect(547, 339, 38, 36))
        self.botao_j.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_j.setText("")
        self.botao_j.setObjectName("botao_j")
        self.botao_j.clicked.connect(lambda : self.chutes('j'))
        
        self.botao_k = QtWidgets.QPushButton(Form)
        self.botao_k.setGeometry(QtCore.QRect(594, 339, 38, 36))
        self.botao_k.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_k.setText("")
        self.botao_k.setObjectName("botao_k")
        self.botao_k.clicked.connect(lambda : self.chutes('k'))

        self.botao_l = QtWidgets.QPushButton(Form)
        self.botao_l.setGeometry(QtCore.QRect(644, 339, 38, 36))
        self.botao_l.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_l.setText("")
        self.botao_l.setObjectName("botao_l")
        self.botao_l.clicked.connect(lambda : self.chutes('l'))

        self.botao_m = QtWidgets.QPushButton(Form)
        self.botao_m.setGeometry(QtCore.QRect(693, 339, 38, 36))
        self.botao_m.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_m.setText("")
        self.botao_m.setObjectName("botao_m")
        self.botao_m.clicked.connect(lambda : self.chutes('m'))

        self.botao_n = QtWidgets.QPushButton(Form)
        self.botao_n.setGeometry(QtCore.QRect(739, 339, 38, 36))
        self.botao_n.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_n.setText("")
        self.botao_n.setObjectName("botao_n")
        self.botao_n.clicked.connect(lambda : self.chutes('n'))

        self.botao_o = QtWidgets.QPushButton(Form)
        self.botao_o.setGeometry(QtCore.QRect(448, 388, 38, 36))
        self.botao_o.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_o.setText("")
        self.botao_o.setObjectName("botao_o")
        self.botao_o.clicked.connect(lambda : self.chutes('o'))

        self.botao_p = QtWidgets.QPushButton(Form)
        self.botao_p.setGeometry(QtCore.QRect(497, 387, 38, 36))
        self.botao_p.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_p.setText("")
        self.botao_p.setObjectName("botao_p")
        self.botao_p.clicked.connect(lambda : self.chutes('p'))

        self.botao_q = QtWidgets.QPushButton(Form)
        self.botao_q.setGeometry(QtCore.QRect(546, 387, 38, 36))
        self.botao_q.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_q.setText("")
        self.botao_q.setObjectName("botao_q")
        self.botao_q.clicked.connect(lambda : self.chutes('q'))

        self.botao_r = QtWidgets.QPushButton(Form)
        self.botao_r.setGeometry(QtCore.QRect(594, 388, 38, 36))
        self.botao_r.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_r.setText("")
        self.botao_r.setObjectName("botao_r")
        self.botao_r.clicked.connect(lambda : self.chutes('r'))

        self.botao_s = QtWidgets.QPushButton(Form)
        self.botao_s.setGeometry(QtCore.QRect(643, 388, 38, 36))
        self.botao_s.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_s.setText("")
        self.botao_s.setObjectName("botao_s")
        self.botao_s.clicked.connect(lambda : self.chutes('s'))

        self.botao_t = QtWidgets.QPushButton(Form)
        self.botao_t.setGeometry(QtCore.QRect(692, 388, 38, 36))
        self.botao_t.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_t.setText("")
        self.botao_t.setObjectName("botao_t")
        self.botao_t.clicked.connect(lambda : self.chutes('t'))
        
        self.botao_u = QtWidgets.QPushButton(Form)
        self.botao_u.setGeometry(QtCore.QRect(739, 388, 38, 36))
        self.botao_u.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_u.setText("")
        self.botao_u.setObjectName("botao_u")
        self.botao_u.clicked.connect(lambda : self.chutes('u'))

        self.botao_v = QtWidgets.QPushButton(Form)
        self.botao_v.setGeometry(QtCore.QRect(495, 432, 38, 36))
        self.botao_v.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_v.setText("")
        self.botao_v.setObjectName("botao_v")
        self.botao_v.clicked.connect(lambda : self.chutes('v'))

        self.botao_w = QtWidgets.QPushButton(Form)
        self.botao_w.setGeometry(QtCore.QRect(545, 432, 38, 36))
        self.botao_w.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_w.setText("")
        self.botao_w.setObjectName("botao_w")
        self.botao_w.clicked.connect(lambda : self.chutes('w'))

        self.botao_x = QtWidgets.QPushButton(Form)
        self.botao_x.setGeometry(QtCore.QRect(594, 432, 38, 36))
        self.botao_x.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_x.setText("")
        self.botao_x.setObjectName("botao_x")
        self.botao_x.clicked.connect(lambda : self.chutes('x'))

        self.botao_y = QtWidgets.QPushButton(Form)
        self.botao_y.setGeometry(QtCore.QRect(642, 432, 38, 36))
        self.botao_y.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_y.setText("")
        self.botao_y.setObjectName("botao_y")
        self.botao_y.clicked.connect(lambda : self.chutes('y'))

        self.botao_z = QtWidgets.QPushButton(Form)
        self.botao_z.setGeometry(QtCore.QRect(691, 432, 38, 36))
        self.botao_z.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.botao_z.setText("")
        self.botao_z.setObjectName("botao_z")
        self.botao_z.clicked.connect(lambda : self.chutes('z'))
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("HANGMAN", "HANGMAN"))


    def sortear_palavra(self):
        self.palavras = open(r'./palavras.txt', 'r', encoding='utf-8')
        self.ler_lista_palavras = self.palavras.readlines()
        self.lista_palavras = []

        for word in self.ler_lista_palavras:
            separando = word[:-1]
            self.lista_palavras.append(separando)

            self.indice_secret_word = random.randint(0, len(self.lista_palavras)-1)
            self.palavra_secreta = self.lista_palavras[self.indice_secret_word]
            self.underlines_palavra_secreta = list('_'*len(self.palavra_secreta))

        self.play_again.setDisabled(True)
        self.play_again.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
        self.label_vidas.show()
        self.palavra_sorteada.show()

        self.botao_a.setDisabled(False)
        self.botao_a.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_b.setDisabled(False)
        self.botao_b.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_c.setDisabled(False)
        self.botao_c.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_d.setDisabled(False)
        self.botao_d.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_e.setDisabled(False)
        self.botao_e.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_f.setDisabled(False)
        self.botao_f.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_g.setDisabled(False)
        self.botao_g.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_h.setDisabled(False)
        self.botao_h.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_i.setDisabled(False)
        self.botao_i.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_j.setDisabled(False)
        self.botao_j.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_k.setDisabled(False)
        self.botao_k.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_l.setDisabled(False)
        self.botao_l.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_m.setDisabled(False)
        self.botao_m.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_n.setDisabled(False)
        self.botao_n.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_o.setDisabled(False)
        self.botao_o.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_p.setDisabled(False)
        self.botao_p.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_q.setDisabled(False)
        self.botao_q.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_r.setDisabled(False)
        self.botao_r.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_s.setDisabled(False)
        self.botao_s.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_t.setDisabled(False)
        self.botao_t.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_u.setDisabled(False)
        self.botao_u.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_v.setDisabled(False)
        self.botao_v.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_w.setDisabled(False)
        self.botao_w.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_x.setDisabled(False)
        self.botao_x.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_y.setDisabled(False)
        self.botao_y.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.botao_z.setDisabled(False)
        self.botao_z.setStyleSheet("background: rgba(255, 255, 255, 0)")

        self.dica()
        self.label_chutes.show()
        

    def dica(self):
        self.dicas = open(r'./dicas.txt', 'r', encoding='utf-8')
        self.ler_lista_dicas = self.dicas.readlines()
        self.dica_palavra_secreta = self.ler_lista_dicas[self.indice_secret_word]
        print(self.dica_palavra_secreta)
        self.label_dica.setText(self.dica_palavra_secreta)
        self.label_dica.show()
        

    def verificar_letra(self, letra_escolhida):
        if letra_escolhida in self.palavra_secreta:
            for index, letra in enumerate(self.palavra_secreta):
                if letra_escolhida == letra:
                    self.underlines_palavra_secreta[index] = letra_escolhida
                    self.palavra_sorteada.setText(str(' '.join(self.underlines_palavra_secreta)))

                if ''.join(self.underlines_palavra_secreta) == self.palavra_secreta:
                    print('voce ganhou')
                    tela_vencedor.tela.show()
                    Form.close()
            
        else:
            self.vidas -= 1
            self.label_vidas.setText(str(self.vidas))
            if self.vidas == 0:
                print('voce perdeu')
                tela_perdedor.tela.show()
                Form.close()
            

    def chutes(self, letra):
        if letra == 'a':
            self.botao_a.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_a.setDisabled(True)
            self.verificar_letra('A')
        elif letra == 'b':
            self.botao_b.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_b.setDisabled(True)
            self.verificar_letra('B')
        elif letra == 'c':
            self.botao_c.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_c.setDisabled(True)
            self.verificar_letra('C')
        elif letra == 'd':
            self.botao_d.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_d.setDisabled(True)
            self.verificar_letra('D')
        elif letra == 'e':
            self.botao_e.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_e.setDisabled(True)
            self.verificar_letra('E')
        elif letra == 'f':
            self.botao_f.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_f.setDisabled(True)
            self.verificar_letra('F')
        elif letra == 'g':
            self.botao_g.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_g.setDisabled(True)
            self.verificar_letra('G')
        elif letra == 'h':
            self.botao_h.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_h.setDisabled(True)
            self.verificar_letra('H')
        elif letra == 'i':
            self.botao_i.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_i.setDisabled(True)
            self.verificar_letra('I')
        elif letra == 'j':
            self.botao_j.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_j.setDisabled(True)
            self.verificar_letra('J')
        elif letra == 'k':
            self.botao_k.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_k.setDisabled(True)
            self.verificar_letra('K')
        elif letra == 'l':
            self.botao_l.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_l.setDisabled(True)
            self.verificar_letra('L')
        elif letra == 'm':
            self.botao_m.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_m.setDisabled(True)
            self.verificar_letra('M')
        elif letra == 'n':
            self.botao_n.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_n.setDisabled(True)
            self.verificar_letra('N')
        elif letra == 'o':
            self.botao_o.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_o.setDisabled(True)
            self.verificar_letra('O')
        elif letra == 'p':
            self.botao_p.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_p.setDisabled(True)
            self.verificar_letra('P')
        elif letra == 'q':
            self.botao_q.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_q.setDisabled(True)
            self.verificar_letra('Q')
        elif letra == 'r':
            self.botao_r.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_r.setDisabled(True)
            self.verificar_letra('R')
        elif letra == 's':
            self.botao_s.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_s.setDisabled(True)
            self.verificar_letra('S')
        elif letra == 't':
            self.botao_t.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_t.setDisabled(True)
            self.verificar_letra('T')
        elif letra == 'u':
            self.botao_u.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_u.setDisabled(True)
            self.verificar_letra('U')
        elif letra == 'v':
            self.botao_v.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_v.setDisabled(True)
            self.verificar_letra('V')
        elif letra == 'w':
            self.botao_w.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_w.setDisabled(True)
            self.verificar_letra('W')
        elif letra == 'x':
            self.botao_x.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_x.setDisabled(True)
            self.verificar_letra('X')
        elif letra == 'y':
            self.botao_y.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_y.setDisabled(True)
            self.verificar_letra('Y')
        elif letra == 'z':
            self.botao_z.setStyleSheet("background: rgba(255, 255, 255, 0.5)")
            self.botao_z.setDisabled(True)
            self.verificar_letra('Z')
        
        self.lista_chutes.append(letra)
        self.label_chutes.setText(str(' '.join(self.lista_chutes).upper()))


class Tela_vencedor(Vencedor):
    def __init__(self):
        super().__init__()
        self.tela = QtWidgets.QMainWindow()
        self.setupUi(self.tela)

    def novamente(self):
        ui = Forca()
        ui.setupUi(Form)
        Form.show()
        tela_vencedor.tela.close()
    
class Tela_perdedor(Perdedor, Forca):
    def __init__(self):
        super().__init__()
        self.tela = QtWidgets.QMainWindow()
        self.setupUi(self.tela)

    def novamente(self):
        ui = Forca()
        ui.setupUi(Form)
        Form.show()
        tela_perdedor.tela.close()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    tela_vencedor = Tela_vencedor()
    tela_perdedor = Tela_perdedor()
    ui = Forca()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
