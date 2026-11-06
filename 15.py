#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato.
#o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:




#primeiro sabemos o salario que ganha por mes
hora = int(input('Quanto você ganha por hora:'))
hora_mes = int(input('Quantas horas voce trabalha no mes:'))
salario_bruto = hora * hora_mes
#desconto de Imposto de Renda  11%
ir0 = salario_bruto * 0.11
ir1=  salario_bruto - ir0
#desconto de  INSS 8%
inss0 = ir1 * 0.08
inss1 = ir1 - inss0
#para o sindicato 5%
s0 = inss1 * 0.05
s1 = inss1 - s0

print(f'+ Salário Bruto : R${salario_bruto}')
print(f'- IR (11%) : R${ir0}')
print(f'- INSS (8%) : R${inss0}')
print(f'- Sindicato (5%) : R${s0}')
print(f'= Salário Liquido : R${s1:.2f}')