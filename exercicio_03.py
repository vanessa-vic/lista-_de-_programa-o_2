# -*- coding: utf-8 -*-
"""Exercicio3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RBDVFwogmUAUtUMss1_waaCbyAJ8ZJcy
"""

#valores arbitrarios para o NDVI


XNIR = 2
XRED = 5

NDVI = ((XNIR - XRED) / (XNIR + XRED))

print("O valor de NDVI é :")
print(NDVI)
    
#valores arbitrarios para o NDWI


XGREEN = 7
XNIR = 2


NDWI = ((XGREEN - XNIR) / (XGREEN + XNIR))

print("O valor de NDWI é :")
print(NDWI)
