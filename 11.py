#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

n3 = float(input('Digite um número real (ex: 5.5): ')) 
#primeiro ele quer saber o produto(resultado da operação X) do dobro do primeiro com a metade do segundo
primeiro = (n1 * 2) * (n2 / 2)
#a SOMA do triplo do primeiro com o terceiro
segundo = (n1 * 3) + n3
#agora so quer saber o terceiro elevado ao cubo
terceiro = n3 ** 3

print(primeiro)
print(segundo)
print(terceiro)