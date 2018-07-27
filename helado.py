apetece_helado_input = input("¿Quieres un helado? (Si / No)").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que digas Si o No >:v, no se que digiste pero ponle que digiste No :V")
    apetece_helado = False


tienes_dinero_input = input("¿Tienes dinero para el helado?  (Si / No)").upper()
heladeria_abierta_input = input("¿Esta abierta la heladeria?(Si / No)" ).upper()
esta_tia_input = input("¿Esta tu tia con dinero cerca? (Si / No)").upper()




apetece_helado = apetece_helado_input == "SI"
puedes_comprarlo = tienes_dinero_input == "SI" or esta_tia_input == "SI"
heladeria_abierta = heladeria_abierta_input == "SI"

if apetece_helado and puedes_comprarlo and heladeria_abierta:
    print("Pues compralo :V")
else:
    print("Pues nada :'v")
