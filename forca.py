#-*- coding: utf-8 -*-

#Importações
import random

#Tabuleiro
tabuleiro = ['''
>>>>>>>>>> Jogo da Forca <<<<<<<<<<

 +----+
 |    |
      |
      |
      |
      |
==========
==========
''',
'''

 +----+
 |    |
 0    |
      |
      |
      |
==========
==========

''',
'''

 +----+
 |    |
 0    |
 |    |
      |
      |
==========
==========

''',
'''

 +----+
 |    |
 0    |
/|    |
      |
      |
==========
==========

''',
'''

 +----+
 |    |
 0    |
/|\   |
      |
      |
==========
==========

''',
'''

 +----+
 |    |
 0    |
/|\   |
/     |
      |
==========
==========

''',
'''

 +----+
 |    |
 0    |
/|\   |
/ \   |
      |
==========
==========

'''
]

#Classe

class Forca:
    certas=[]
    erros = 0
    tentativas=[]
    #Método Construtor
    def __init__(self, palavra, tabuleiro):
        self.palavra = palavra

    #Método para adivinhar a letra
    def adivinhar(self, letra):
        self.tentativas.append(letra)
        if letra in self.palavra:
            self.certas.append(letra)
            return True
        else:
            self.erros+=1
            return False

    #Método para verificar se o jogo terminou
    def verificar_fim(self):
        if self.erros == 6:
            return True
        else:
            return False

    #Método para verificar se o jogador venceu
    def verificar_vitoria(self):
        for i in self.palavra:
            if i in self.certas:
                None
            else:
                return False
        return True

    #Método para não mostrar a letra no tabuleiro
    def esconder(self):
        imprimir=''
        for i in self.palavra:
            if i in self.certas:
                imprimir += i
            else:
                imprimir += '_'
        print('Tentativas: ')
        for l in self.tentativas:
            print(l)
        print(imprimir)

    #Método para verificar o estado do jogo e imprimir na tela
    def print_tabuleiro(self):
        print(tabuleiro[self.erros])

#Função para ler uma palavra aleatória do banco de palavras
def palavra_aleatoria():
    with open('palavras.txt', 'r') as a:
        palavras = a.readlines()
    return palavras[random.randint(0, len(palavras))].strip()

#Função principal
def main():
    #Objeto
    jogo = Forca(palavra_aleatoria(), tabuleiro)

    while True:
        jogo.print_tabuleiro()

        if jogo.verificar_fim():
            print('Você perdeu! FIM DE JOGO!!!')
            print('A palavra era: %s' %(jogo.palavra))
            break

        if jogo.verificar_vitoria():
            print('Você venceu! PARABÉNS!!!')
            break

        jogo.esconder()

        jogo.adivinhar(input('Digite uma letra: '))


# Executa o programa
if __name__ == "__main__":
    main()



