# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:07:43 2015

@author: rmallermartins
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# bfs(Imagem entrada binarizada, diferença de intensidade entre rotulos)
def bfs(imagem, rotuloDif):
    rotulo = 0
    fila = []
    linhas, colunas = np.shape(imagem)
    for x in range(0, linhas):
        for y in range(0, colunas):
            p = (x, y)
            if imagem[p] == 255:
                rotulo += rotuloDif
                imagem[p] = rotulo
                fila.append(p)
            
            while fila:
                p = fila.pop(0)
                vizinhos = quatroVizinhos(p, imagem)
                for q in vizinhos:
                    if imagem[q] == 255:
                        imagem[q] = rotulo
                        fila.append(q)

# quatroVizinhos(ponto a encontrar vizinhos, imagem)
def quatroVizinhos(ponto, imagem):
    vizinhos = set()
    x, y = ponto
    tamX, tamY = np.shape(imagem)
    if (x - 1) > 0:
        vizinhos.add((x - 1, y))
    if (y - 1) > 0:
        vizinhos.add((x, y - 1))
    if (x + 1) < tamX:
        vizinhos.add((x + 1, y))
    if (y + 1) < tamY:
        vizinhos.add((x, y + 1))
    return vizinhos

# mostraHist(imagem rotulada, diferença de intensidade entre rotulos)
def mostraHist(imagem, rotuloDif):
    rotulo = 0
    
    n,bins,patches = plt.hist(imagem.ravel(), 256, [1, 255])
    for x in n:
        if x > 0:
            rotulo += rotuloDif
            plt.text(rotulo - 20, x + 10, "(" + str(rotulo) + ", " + str(x) + ")")
    plt.show()

def main():
    # Diferença de intensidade entre os rotulos
    rotuloDif = 25 
    
    a = cv2.imread('Imagens/objetos.png', 0)
    ret, b = cv2.threshold(a, 127, 255, cv2.THRESH_BINARY)
    
    cv2.imshow('threshhold', b)
    
    bfs(b, rotuloDif)
    
    cv2.imshow('rotulada', b)
    
    mostraHist(b, rotuloDif)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()