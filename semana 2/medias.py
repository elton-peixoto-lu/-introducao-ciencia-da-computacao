def calcular_media(notas):
    total_notas = sum(notas)
    quantidade_notas = len(notas)
    media = total_notas / quantidade_notas
    return media

try:
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)

    media_aritmetica = calcular_media(notas)
    print(f"A média aritmética é {media_aritmetica:.1f}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números válidos para as notas.")