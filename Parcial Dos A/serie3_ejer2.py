cadena_de_texto = input("Escriba la cadena de texto deseada \n")
letra_repetida_min = "e"
letra_rep_may = "E"
contador_letra_min = 0
contador_letra_may = 0
for vocal in cadena_de_texto:
    if vocal == letra_repetida_min:
        contador_letra_min += 1

for vocal2 in cadena_de_texto:
    if vocal2 == letra_rep_may:
        contador_letra_may += 1

print(f"la letra {letra_repetida_min} se repite {contador_letra_min} de veces")
print(f"la letra {letra_rep_may} se repite {contador_letra_may} de veces")