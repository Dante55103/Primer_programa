frase_usuario = input("Escribe una frase: ")

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

n_vocales = 0

for letras in frase_usuario:
    if letras in vocales:
        n_vocales += 1

print("Has colocado {} vocales en tu frase. ".format(n_vocales))
