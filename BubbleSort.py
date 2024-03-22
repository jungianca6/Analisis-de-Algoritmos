import random
import time

#Cuadratica
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def generate_random_numbers(n):
    return [random.randint(0, 1000000000) for _ in range(n)]

def main():
    n = 10000  # Cantidad de elementos del array
    array = generate_random_numbers(n)  # Genera el array

    # start_time = time.time()  # Para medir el tiempo en segundos
    start_time = time.time_ns()  # Para medir el tiempo en nanosegundos
    bubble_sort(array)
    # end_time = time.time()  # Para medir el tiempo en segundos
    end_time = time.time_ns()  # Para medir el tiempo en nanosegundos

    # total_time = end_time - start_time  # Calcula el tiempo total de ejecución del algoritmo en segundos
    total_time = end_time - start_time  # Calcula el tiempo total de ejecución del algoritmo en nanosegundos
    print("Tiempo de ejecución:", total_time, "ns")

if __name__ == "__main__":
    main()
