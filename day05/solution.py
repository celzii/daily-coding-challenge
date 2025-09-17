def find_maximum(nums):
    """Mengembalikan angka terbesar dari list nums."""
    if not nums:
        raise ValueError("List tidak boleh kosong")
    return max(nums)

if __name__ == "__main__":
    contoh = [1, 7, 3, 9, 2]
    print(find_maximum(contoh))  # Output: 9