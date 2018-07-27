tipo_cuenta = input("¿Que cuenta quieres realizar? (Division / Multiplicacion / Suma / Resta )").upper()

pri_numero = int(input("¿Cual es el primer numero de la cuenta? (Ej: 1, 2, 3, 78)"))
seg_numero = int(input("¿Cual es el segundo numero de la cuenta?"))
resultado = 0

if tipo_cuenta == "MULTIPLICACION":
    resultado = pri_numero * seg_numero
elif tipo_cuenta == "DIVISION":
    resultado = pri_numero / seg_numero
elif tipo_cuenta == "SUMA":
    resultado = pri_numero + seg_numero
elif tipo_cuenta == "RESTA":
    resultado = pri_numero - seg_numero

if tipo_cuenta == "MULTIPLICACION":
    print("El resultado de tu {} es {}.".format(tipo_cuenta, resultado))
elif tipo_cuenta == "DIVISION":
    print("El resultado de tu {} es {}.".format(tipo_cuenta, resultado))
elif tipo_cuenta == "SUMA":
    print("El resultado de tu {} es {}.".format(tipo_cuenta, resultado))
elif tipo_cuenta == "RESTA":
    print("El resultado de tu {} es {}.".format(tipo_cuenta, resultado))
