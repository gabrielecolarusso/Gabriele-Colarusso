#Sexo de la persona que está jugando
x = input("Hola, como estas? Indicame si eres chico o chica porfavor \n")
i = "bienvenid"
j = "viajer"

if x == "chico":
    i += "o"
    j += "o"
elif x == "chica":
    i += "a"
    j += "a"
else:
    print("Responde chico o chica")
    quit()
print(i, "al mundo de los Pokemon")


#Región de el jugador
print("\nKanto \nJohto \nHoenn \nSinnoh \nTeselia \nKalos \nAlola \nGalar \nPaldea")
r = input("Indicame de cual de las regiones eres: ")
f = "Tu región es una de mis favoritas"
g = ",un gusto en conocerte"

if r == "Kanto" or "Johto" or "Hoenn" or "Teselia" or "Kalos" or "Alola" or "Galar" or "Paldea":
    print(f, j, g)
else:
    print("escoge una de las regiones de la lista")
    quit()
    
    
#Escoger el Pokemon favorito
print("\nPikachu \nDragonite \nCharizard")
p = input("Escoge uno de los 3 Pokemones para comenzar tu viaje: ")
v = "Ya puedes comenzar tu aventura"

if r == "Pikachu" or "Dragonite" or "Charizard":
    print(v, j, ",que tengas un excelente recorrido.")
else:
    print("escoge uno de los pokemones de la lista")
    quit()