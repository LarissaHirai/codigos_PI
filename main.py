"""
Universidade Federal do Tocantins - Campus Palmas
Discilina: Processamento de Imagens
Professora: Glenda Botelho
Alunas: Fernanda Plessim e Larissa Hirai
Curso: Ciêmcias da Computação
"""
# Atividade 1
# Biblioteca numpy está sendo importada
import numpy as np
# Bibliotecas PIL e matplotlib sendo importadas
from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import math
"""
Para baixar as bibliotecas basta colocar o seguinte código no terminal python do VsCode:
pip install numpy
pip install matplotlib
(Com esse comando a biblioteca PIL vai ser instalada no mesmo pacote)
"""

def reduzir_vizinho(imagem):
    altura=len(imagem)     # procura o número de linhas
    largura=len(imagem[0])  # procura o número de coluna

    resultado = [[0 for i in range(0,altura,2)] for j in range(0,largura,2)] # cria uma matriz

    x=0
    y=0
    for i in range(0, altura,2):
        for j in range(0,largura,2):
            resultado[x][y]=imagem[i][j]
            y=y+1
        y=0
        x=x+1

    np_array= np.array(resultado) # transforma o array em um numpy array

    nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem

    return nova_img


def ampliar_vizinho(imagem):
    altura = len(imagem)    # procura por número de linhas
    largura = len(imagem[0])    # procura por número de colunas
    resultado = [[0 for i in range(0,(altura + math.ceil(altura/2)))] for j in range(0,(largura + math.ceil(largura/2)))] # cria uma matriz
    x=0
    y=0
    for i in range(0, altura,2):
        for j in range(0,largura,2):
            for k in range(x, x+2):
                for l in range(y, y+2):
                    resultado[k][l]=imagem[i][j]
        y=0
        x=x+1
    np_array= np.array(resultado) # transforma o array em um numpy array

    nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem

    return nova_img

def ampliar_bilinear(imagem):
    altura = len(imagem)    # procura por número de linhas
    largura = len(imagem[0])    # procura por número de colunas
    resultado = [[0 for i in range(0,(altura + math.ceil(altura/2)))] for j in range(0,(largura + math.ceil(largura/2)))] # cria uma matriz
    x=0
    y=0
    for i in range(0, altura,2):
        for j in range(0,largura,2):
            num1 = imagem[i][j]
            num2 = imagem[i][j+1]
            num3 = imagem[i+1][j]
            num4 = imagem[i+1][j+1]
            a = int(round((num1 + num2) / 2))
            e = int(round((num3 + num4) / 2))
            b = int(round((num1 + num3) / 2))
            d = int(round((num2 + num4) / 2))
            c = int(round(((num1 + num2) + (num3 + num4)) / 4))
            resultado[x][y] = num1
            resultado[x][y+1] = a
            resultado[x][y+2] = num2
            resultado[x+1][y] = b
            resultado[x+1][y+1] = c
            resultado[x+1][y+2] = d
            resultado[x+2][y] = num3
            resultado[x+2][y+1] = e
            resultado[x+2][y+2] = num4
        y=0
        x=x+1
    np_array= np.array(resultado) # transforma o array em um numpy array

    nova_img = Image.fromarray(np_array) # transforma o numpy array em uma imagem

    return nova_img
# def main():
# Primeiramente transformar imagem colorida em tons de cinza
# abre a imagem colorida
imagem = Image.open('./img/imagem_colorida.jpeg')

 # converte a imagem para o modo L (escala de cinza)
img_escala_de_cinza = imagem.convert('L')

 # salva a nova imagem
img_escala_de_cinza.save('./img/imagem_tons_cinza.jpeg')

 # transforma a imagem em matriz
data = image.imread('./img/imagem_tons_cinza.jpeg')
print("Imagem -> Matriz")

imagem = data

 # pega a opção que o cliente quer fazer com a imagem
op = int(input("O que deseja fazer com a sua imagem? 1-Ampliar 2-Redizir"))

 # pega o tipo de interpolação que o cliente deseja
op2 = int(input("1-Imterpolação por vizinho mais próximo 2-Interpolação bilinear"))

 # esrutura condicional que define a função para ser executada de acordo com as opções do cliente
if op == 1:
    if op2 == 1:
        # Amplia a imagem original com vizinho + proximo
        img_ampliada = ampliar_vizinho(imagem)
        # Salva a nova imagem ampliada
        img_ampliada.save("./img/imagem_ampliada_vizinho.png")
    elif op2 == 2:
        # Amplia a imagem original com interpolação bilinear
        img_ampliada = ampliar_bilinear(imagem)
        # Salva a nova imagem reduzida
        img_ampliada.save("./img/imagem_ampliada_bilinear.png")
elif op == 2:
    if op2 == 1:
        # Reduz a imagem original com vizinho + proximo
        img_reduzida = reduzir_vizinho(imagem)
        # Salva a nova imagem ampliada
        img_reduzida.save("./img/imagem_reduzida_vizinho.png")
    elif op2 == 2:
        # Reduz a imagem original com interpolação bilinear
        img_reduzida = reduzir_bilinear(imagem)
        # Salva a nova imagem reduzida
        img_reduzida.save("./img/imagem_reduzida_bilinear.png")
