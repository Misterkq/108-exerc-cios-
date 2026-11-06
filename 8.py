#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input('Quanto você ganha por hora?: '))
mes_hora = float(input('Quantas horas você trabalhou no mês?: '))

calculando = hora * mes_hora

print(f'total do seu salário no referido mês é {calculando:.2f} ')


