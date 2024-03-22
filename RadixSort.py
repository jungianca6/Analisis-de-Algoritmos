import random
import time

#Lineal
def radix_sort(arr):
    def count_sort(arr, exp):
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            count[(arr[i] // exp) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            output[count[(arr[i] // exp) % 10] - 1] = arr[i]
            count[(arr[i] // exp) % 10] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    def get_max(arr):
        mx = arr[0]
        for i in range(1, n):
            if arr[i] > mx:
                mx = arr[i]
        return mx

    n = len(arr)
    m = get_max(arr)

    exp = 1
    while m // exp > 0:
        count_sort(arr, exp)
        exp *= 10


def generate_random_numbers(n):
    return [random.randint(0, 10000) for _ in range(n)]


def main():
    n = 100  # Cantidad de elementos del array
    array = generate_random_numbers(n)  # Genera el array

    print("Array original:")
    print(array)

    start_time = time.time_ns()
    radix_sort(array)
    end_time = time.time_ns()

    print("Array ordenado:")
    print(array)

    total_time = end_time - start_time  # Calcula el tiempo total de ejecución del algoritmo en nanosegundos
    print("Tiempo de ejecución:", total_time, "ns")


if __name__ == "__main__":
    main()
