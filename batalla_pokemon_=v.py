pokemon_elegido = input("¿Contra que pokemon quieres luchar? (Bulbasaur/Charmander/Squirtle): ").upper()

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = 100

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque quieres utilizar? (Trueno / Rayo / Tackle)")

    if ataque_elegido == "Trueno":
        vida_enemigo -= 10
        print("¡La vida del enemigo disminuyo 10 puntos!")
        print("La vida de tu Pokemon es: ")
        print(vida_pikachu)
        print("La vida del enemigo es: ")
        print(vida_enemigo)
    elif ataque_elegido == "Rayo":
        vida_enemigo -= 15
        print("¡La vida del enemigo disminuyo 15 puntos!")
        print("La vida de tu Pokemon es: ")
        print(vida_pikachu)
        print("La vida del enemigo es: ")
        print(vida_enemigo)
    elif ataque_elegido == "Tackle":
        vida_enemigo -= 5
        print("¡La vida del enemigo disminuyo 5 puntos!")
        print("La vida de tu Pokemon es: ")
        print(vida_pikachu)
        print("La vida del enemigo es: ")
        print(vida_enemigo)

    if pokemon_elegido == "SQUIRTLE":
        vida_pikachu -= 8
        print("¡El enemigo te quito 8 puntos!")
    elif pokemon_elegido == "CHARMANDER":
        vida_pikachu -= 9
        print("¡El enemigo te quito 9 puntos!")
    elif pokemon_elegido == "BULBASAUR":
        vida_pikachu -= 10
        print("¡El enemigo te quito 10 puntos!")



if vida_pikachu == 0:
    print("Que pena has perdido ¡Mejor suerte para la proxima!")
elif vida_enemigo == 0:
    print("¡Felicidades, has ganado!")

print("La vida de tu Pokemon es: {}".format(vida_pikachu))
print("La vida del enemigo es: {}".format(vida_enemigo))


print("El combate a terminado")

