#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi

raio = float(input("Digite o valor do raio do circulo:"))

area = pi * (raio ** 2)

print(f'A area do circulo com raio {raio} : {area:.2f}')