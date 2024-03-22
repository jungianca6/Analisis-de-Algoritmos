import time
import random

def busqueda_binaria(arr, x):
    izquierda, derecha = 0, len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio] == x:
            return medio
        elif arr[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

def generar_array_ordenado(n):
    return sorted([random.randint(1, 1000) for _ in range(n)])

def main():
    n = 100000  # Tamaño del array
    array = generar_array_ordenado(n)

    # Elemento a buscar (no presente en el array)
    elemento_a_buscar = -1

    # Realizar búsqueda binaria y medir el tiempo
    inicio = time.time_ns()
    resultado = busqueda_binaria(array, elemento_a_buscar)
    fin = time.time_ns()

    tiempo_transcurrido = fin - inicio

    if resultado != -1:
        print(f"Elemento encontrado en la posición {resultado}.")
    else:
        print("Elemento no encontrado en el array.")

    print(f"Tiempo de ejecución: {tiempo_transcurrido} nanosegundos.")

if __name__ == "__main__":
    main()
