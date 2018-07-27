mi_lista = []
input_usuario = input("¿Que necitas comprar? (Escribe FIN para terminar ): ")
indice_actual = 0

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("¿Que necitas comprar? (Escribe FIN para terminar ): ")

for item in mi_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))

print("Esta es la lista de la compra.")
