def calcular_perimetro_e_area(lado):
    perimetro = 4 * lado
    area = lado ** 2
    return perimetro, area

try:
    lado = float(input("Digite o valor correspondente ao lado de um quadrado: "))
    perimetro, area = calcular_perimetro_e_area(lado)
    print(f"perímetro: {perimetro} - área: {area}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número válido para o lado do quadrado.")