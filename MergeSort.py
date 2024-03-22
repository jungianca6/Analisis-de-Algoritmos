import random
import time

#Logaritmica lineal
def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Copia los datos a los arrays temporales L[] y R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Comprueba si quedan elementos por copiar en L[] y R[]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Función para medir el tiempo de ejecución en nanosegundos
def measure_time(func, arr):
    start_time = time.time_ns()
    func(arr)
    end_time = time.time_ns()
    return end_time - start_time


# Genera una lista de números aleatorios
def generate_random_numbers(n):
    return [random.randint(0, 1000000) for _ in range(n)]


if __name__ == "__main__":
    n = 1000000
    array = generate_random_numbers(n)

    print("Array original:")
    print(array)

    time_elapsed = measure_time(mergeSort, array)

    print("Array ordenado:")
    print(array)

    print("Tiempo de ejecución:", time_elapsed, "nanosegundos")
