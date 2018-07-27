salida = False
agenda = dict()

while not salida:
    accion = input("¿Que quieres hacer? Agendar un nuevo número[A] / Consultar número[C] / Salir [S]: ")

    # Accion Añadir
    if accion == "A":
        print("Vamos a añadir un número telefonico: ")
        print("-------------------------------------")
        nombre = input("Nombre: ")
        numero = input("Número: ")
        agenda[nombre] = numero

    # Accion consultar:
    elif accion == "C":
        print("Vamos a consultar un número: ")
        print("-------------------------------------")
        nombre = input("De quiene quieres saber el número: ")
        print(agenda[nombre])
    elif accion == "S":
        salida = True
