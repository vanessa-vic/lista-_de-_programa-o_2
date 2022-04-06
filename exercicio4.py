# -*- coding: utf-8 -*-
"""Exercicio4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DGUXxD0wHHCX8EQpNmP6bxTiyqV-9hi6
"""

#Importar biblioteca math.

from math import radians, cos,sin, sqrt, asin

#ler a entrada/input como um float.

print("Input coordenadas de entrada de dois pontos:")
plat = radians(float(input("Latitude inicial: ")))
plon = radians(float(input("Longitude final: ")))
qlat = radians(float(input("Latitude inicial: ")))
qlon = radians(float(input("Longitude final: ")))

dlon = qlon - plon
dlat = qlat - plat

#calcule a distância entre dois pontos usando a fórmula de Haversine.

a = sin(dlat / 2) ** 2 + cos(plat) * cos(qlat) * sin(dlon / 2) ** 2
print(2 * 6371 * asin(sqrt(a)))