#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input('Qual o peso do peixe que voce pescou: '))

if peso_peixe > 50:
    excesso = peso_peixe - 50
    multa = excesso * 4.00
    print(f'Voce passou do limite de quilos. Excesso: {excesso} kg. Devera pagar uma multa de R$ {multa:.2f}')
else:
    excesso = 0
    multa = 0
    print('Peso dentro do limite. Nenhuma multa.')

print('Tenha um bom dia!')