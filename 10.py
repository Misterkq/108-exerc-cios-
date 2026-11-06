#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

celsius = float(input('Fale a temperatura de Celsius:'))
farenheit = (celsius*9/5) + 32
print(f'Celsius em Farenheit é : {farenheit:.2f}°F')