frase_usuario = input("Escribe una frase: ")

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "Q", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

n_mayusculas = 0

for letras in frase_usuario:
    if letras in mayusculas:
        n_mayusculas += 1

print("Has puesta {} letras en mayuscula".format(n_mayusculas))
