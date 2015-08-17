# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 08:17:09 2015

@author: Rodrigo Maller Martins
"""

import numpy as np
import cv2

def mostraImg(nomeJanela, Imagem) :
    
    cv2.imshow(nomeJanela, Imagem)
    cv2.waitKey()
    cv2.destroyWindows(nomeJanela)

def geraDisco(tamImagem, raioDisco) :
    
    DISCO = np.ones((tamImagem, tamImagem, 3), np.float32)
    
    vetorX, vetorY = np.ogrid[:tamImagem, :tamImagem]
    
    centroX = tamImagem/2
    centroY = tamImagem/2
    
    discoSat = ((vetorX - centroX) ** 2) + ((vetorY - centroY) ** 2)
    
    H = np.arctan2(vetorX.astype(np.float32) - centroX, vetorY.astype(np.float32) - centroY)
    H = np.degrees(H) + 90
    
    S = np.ones((tamImagem, tamImagem), np.float32)
    S = discoSat.astype(np.float32)/(raioDisco**2)   
    
    V = np.ones((tamImagem, tamImagem), np.float32)
    
    DISCO[:, :, 0] = H
    DISCO[:, :, 1] = S
    DISCO[:, :, 2] = V
    
    DISCO[discoSat > raioDisco ** 2] = [0, 0, 0]
    
    DISCO = cv2.cvtColor(DISCO, cv2.COLOR_HSV2BGR)
    
    return DISCO
    
def main() :
    disco = geraDisco(500, 200)
    mostraImg("Disco HSV", disco)

if __name__ == "__main__":
    main()