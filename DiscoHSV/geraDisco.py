# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 08:17:09 2015

@author: Rodrigo
"""

import numpy as np
import cv2

def geraDisco(tamImagem, raioDisco) :
    
    IMG = np.ones((tamImagem, tamImagem, 3), np.float32)
    
    vectorX, vectorY = np.ogrid[:tamImagem, :tamImagem]
    
    centerX = tamImagem/2
    centerY = tamImagem/2
    
    DISC = ((vectorX - centerX) ** 2) + ((vectorY - centerY) ** 2)
    
    H = np.arctan2(vectorX.astype(np.float32) - centerX, vectorY.astype(np.float32) - centerY)
    H = np.degrees(H) + 90
    
    S = np.ones((tamImagem, tamImagem), np.float32)
    S = DISC.astype(np.float32)/(raioDisco**2)    
    
    V = np.ones((tamImagem, tamImagem), np.float32)
    
    IMG[:, :, 0] = H
    IMG[:, :, 1] = S
    IMG[:, :, 2] = V
    
    IMG[DISC > raioDisco ** 2] = [0, 0, 0]
    
    IMG = cv2.cvtColor(IMG, cv2.COLOR_HSV2BGR)
    
    cv2.imshow("Disco", IMG)
    cv2.waitKey()
    cv2.destroyWindow("Disco")
    
geraDisco(600, 250)