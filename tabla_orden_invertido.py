numero_tabla = int(input("Dame el numero de la tabla: "))

orden = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for multiplo in orden:
    print("{} x {} = {} ".format(numero_tabla, multiplo, numero_tabla * multiplo))
