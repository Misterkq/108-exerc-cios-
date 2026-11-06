'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''


import math

def calcular_tinta():
    try:
        # Entrada de dados
        area = float(input("Digite o tamanho da área a ser pintada (m²): "))
        
        if area <= 0:
            print("A área deve ser maior que zero.")
            return

        # Definições constantes
        COBERTURA_POR_LITRO = 3
        LITROS_POR_LATA = 18
        PRECO_LATA = 80.00

        # Cálculo da quantidade de tinta necessária
        litros_necessarios = area / COBERTURA_POR_LITRO
        latas_necessarias = math.ceil(litros_necessarios / LITROS_POR_LATA)
        preco_total = latas_necessarias * PRECO_LATA

        # Exibição do resultado
        print("-" * 30)
        print(f"Área a pintar: {area:.2f} m²")
        print(f"Litros necessários: {litros_necessarios:.2f} L")
        print(f"Quantidade de latas a comprar: {latas_necessarias}")
        print(f"Preço total: R$ {preco_total:.2f}")
        print("-" * 30)

    except ValueError:
        print("Erro: Por favor, digite um número válido para a área.")

if __name__ == "__main__":
    calcular_tinta()
