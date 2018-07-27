lista_str = input("Coloca palabras o números: ")
lista_datos = None

for datos in lista_str:
    lista_datos.append(type(lista_str))

print(type(lista_datos))