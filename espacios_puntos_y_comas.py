frase_usuario = input("Escribe una frase: ")

espacios = [" "]
puntos = ["."]
comas = [","]

n_espacios = 0
n_comas = 0
n_puntos = 0

for letras in frase_usuario:
    if letras in espacios:
        n_espacios += 1
    if letras in puntos:
        n_puntos += 1
    if letras in comas:
        n_comas += 1

print("El numero de espacios es {}, el de comas es {} y hay {} puntos".format(n_espacios, n_comas, n_puntos))




