##Hacer un programa que reciba cantidad N de valores separados por comas  y el programa debe devolver la
#suma y el promedio.
def suma_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return suma, promedio


def main():
    entrada = input("Escribe los numeros deseados para su suma y promedio separados por espacios: \n")
    numeros = [int(numero) for numero in entrada.split()]

    if len(numeros) == 0:
        print("La lista no tiene datos")
    else:
        suma, promedio = suma_promedio(numeros)
        print(f"Suma: {suma}")
        print(f"Promedio: {promedio}")

main()