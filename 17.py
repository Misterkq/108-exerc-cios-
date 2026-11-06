'''Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima,
    isto é, considere latas cheias.'''

import math


def calcular_tinta():
  try:
    area = float(
        input("Digite o tamanho da área a ser pintada (m²): ")
    )  #[cite: 1]
  except ValueError:
    print("Digite um número válido!")  #[cite: 1]
    return

  if area <= 0:  #[cite: 1]
    print("A área deve ser maior que zero.")  #[cite: 1]
    return  #[cite: 1]

  cobertura_por_litro = 6  #[cite: 1, 2]
  litros_por_lata = 18  #[cite: 1, 2]
  preco_lata = 80.00  #[cite: 1, 2]

  litros_por_galao = 3.6  #[cite: 1, 2]
  preco_galao = 25.00  #[cite: 1, 2]

  # Litros necessários considerando os 10% de folga[cite: 2]
  litros_necessarios = (area / cobertura_por_litro) * 1.10  #[cite: 1, 2]

  print("\n[1] - Comprar apenas latas de 18 litros")  #[cite: 1, 2]
  print("[2] - Comprar apenas galões de 3,6 litros")  #[cite: 1, 2]
  print("[3] - Misturar latas e galões, de forma que o preço seja o menor.")  #[cite: 1, 2]

  try:
    opc = int(input("Escolha a opção: "))  #[cite: 1]
  except ValueError:
    print("Opção inválida!")
    return

  print("-" * 30)  #[cite: 1]
  print(f"Área a pintar: {area:.2f} m²")  #[cite: 1]
  print(f"Litros necessários (com 10% folga): {litros_necessarios:.2f} L")  #[cite: 1, 2]

  match opc:  #[cite: 1]
    case 1:
      latas = math.ceil(
          litros_necessarios / litros_por_lata
      )  #[cite: 1, 2]
      preco_total = latas * preco_lata  #[cite: 1, 2]
      print(f"Quantidade de latas (18L): {latas}")
      print(f"Preço total: R$ {preco_total:.2f}")  #[cite: 1]

    case 2:
      galoes = math.ceil(
          litros_necessarios / litros_por_galao
      )  #[cite: 1, 2]
      preco_total = galoes * preco_galao  #[cite: 1, 2]
      print(f"Quantidade de galões (3,6L): {galoes}")
      print(f"Preço total: R$ {preco_total:.2f}")  #[cite: 1]

    case 3:
      # Pega o número inteiro de latas de 18L
      latas = int(litros_necessarios // litros_por_lata)
      # Pega a sobra em litros
      sobra_litros = litros_necessarios % litros_por_lata
      # Arredonda a sobra para galões de 3.6L
      galoes = math.ceil(sobra_litros / litros_por_galao)

      preco_total = (latas * preco_lata) + (galoes * preco_galao)

      print(f"Mistura ideal: {latas} lata(s) de 18L e {galoes} galão(ões) de 3,6L")
      print(f"Preço total: R$ {preco_total:.2f}")

    case _:
      print("Opção inválida")  #[cite: 1]

  print("-" * 30)  #[cite: 1]


calcular_tinta()  #[cite: 1]