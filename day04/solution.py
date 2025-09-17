def fibonacci_sequence(n):
    """Mengembalikan list deret Fibonacci hingga n angka."""
    if n <= 0:
        return []
    sequence = [0]
    if n == 1:
        return sequence
    sequence.append(1)
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    contoh = 5
    print(fibonacci_sequence(contoh))  # Output: [0, 1, 1, 2, 3]