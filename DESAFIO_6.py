def ordenar_burbuja(arreglo):
    n = len(arreglo)
    for pasada in range(n - 1):
        for i in range(n - 1 - pasada):
            if arreglo[i] > arreglo[i + 1]:
                arreglo[i + 1], arreglo[i] = arreglo[i], arreglo[i + 1]
        print(f"Pasada {pasada + 1}: {arreglo}")
numeros = [2, 7, 9, 13, 18]
ordenar_burbuja(numeros)
print("Arreglo final ordenado:", numeros)
