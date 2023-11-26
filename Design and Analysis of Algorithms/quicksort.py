import random
import time

def quicksort(arr, low, high, randomized=False):
    comparisons = 0
    swaps = 0

    def partition(arr, low, high):
        nonlocal comparisons, swaps

        pivot_index = low

        # Partition the array around the pivot

        for i in range(low + 1, high + 1):
            if arr[i] <= arr[pivot_index]:
                comparisons += 1
                arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                swaps += 1
                pivot_index += 1

        return pivot_index, comparisons, swaps

    if low < high:
        if randomized:
            # Randomized partition by shuffling elements
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        pivot_index, partition_comparisons, partition_swaps = partition(arr, low, high)
        comparisons += partition_comparisons
        swaps += partition_swaps

        left_comparisons, left_swaps = quicksort(arr, low, pivot_index - 1, randomized)
        right_comparisons, right_swaps = quicksort(arr, pivot_index + 1, high, randomized)

        comparisons += left_comparisons + right_comparisons
        swaps += left_swaps + right_swaps

    return comparisons, swaps

def main():
    random.seed(42)  # For reproducibility, you can change the seed
    while True:
        try:
            n = int(input("Enter the number of elements: "))
            arr = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
            break
        except ValueError:
            print("Please enter a valid integer.")

    print("Select the sorting method:")
    print("1. Deterministic Quick Sort")
    print("2. Randomized Quick Sort")

    choice = int(input("Enter your choice (1/2): "))
    if choice == 1:
        randomized = False
    elif choice == 2:
        randomized = True
    else:
        print("Invalid choice. Using deterministic Quick Sort by default.")
        randomized = False

    start_time = time.time()
    comparisons, swaps = quicksort(arr, 0, n - 1, randomized)
    end_time = time.time()

    print("Sorted array:", arr)
    print(f"Total comparisons: {comparisons}")
    print(f"Total swaps: {swaps}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()