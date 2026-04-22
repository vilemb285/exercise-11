import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range (count)]

def selection_sort(sequence):
    sequence = sequence[:]
    count = len(sequence)

    for i in range(count):
        min = i
        for j in range(i + 1, count):
            if sequence[j] < sequence[min]:
                min = j
        sequence[i], sequence[min] = sequence[min], sequence[i]

    return sequence

def bubble_sort(sequence):
    sequence = sequence[:]
    n = len(sequence)

    for i in range(n):
        for j in range(0, n - i - 1)
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]

    return sequence







def main():
    sequence = random_numbers(count=20, low=0, high=100)
    sorted_sequence = selection_sort(sequence)
    bubble_sorted = bubble_sort(sequence)
    print(f"Serazeny: {sorted_sequence}")
    print(f"Bubble sort: {bubble_sorted}")




if __name__ == "__main__":
    main()
