#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7

genero = input('Qual é seu genero(Masculino,Feminino):').lower().strip()
altura = float(input('Qual é sua altura:'))

peso_masculino = (72.7*altura) - 58
peso_feminino = (62.7 *altura) - 58

if genero == 'masculino':
    print(f'O seu peso a parti de seu genero e sua altura é : {peso_masculino}')
elif genero == 'feminino':
    print(f'O seu peso a parti de seu genero e sua altura é : {peso_feminino}')
else:
    print('erro, genero ou altura não existente')