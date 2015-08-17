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
    cv2.destroyWindow(nomeJanela)

def geraDisco(tamImagem, raioDisco) :
    
    DISCO = np.ones((tamImagem, tamImagem, 3), np.float32)
    
    vetorX, vetorY = np.ogrid[:tamImagem, :tamImagem]
    centroImg = tamImagem/2

    H = np.arctan2(vetorX.astype(np.float32) - centroImg, vetorY.astype(np.float32) - centroImg)
    H = np.degrees(H)
    
    discoSat = ((vetorX - centroImg) ** 2) + ((vetorY - centroImg) ** 2)
    S = discoSat.astype(np.float32)/(raioDisco ** 2)
    
    DISCO[:, :, 0] = H
    DISCO[:, :, 1] = S
    
    DISCO[discoSat > raioDisco ** 2] = [0, 0, 0]
    
    DISCO = cv2.cvtColor(DISCO, cv2.COLOR_HSV2BGR)
    
    return DISCO
    
def main() :
    disco = geraDisco(500, 200)
    mostraImg("Disco HSV", disco)

if __name__ == "__main__":
    main()