numero_tabla = int(input("Dame el numero de la tabla: "))

n_par = [2, 4, 6, 8, 10]

for multiplo in n_par:
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))
