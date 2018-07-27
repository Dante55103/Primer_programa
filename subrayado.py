frase_usuario = input("Escribe una frase: ")

cantidad_espacios = 0


espacios = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "Q", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    "a", "b", "c", "d", "e", "f", "g", "Hh", "i", "j", "q", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "Vv", "w", "x", "y", "z", ",", ".", " "]

for espacios in frase_usuario:
    cantidad_espacios =+ 1

print(frase_usuario)
print("-" * cantidad_espacios)
