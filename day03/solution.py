def is_palindrome(s: str) -> bool:
    """Cek apakah string s adalah palindrome."""
    s = s.lower().replace(' ', '')
    return s == s[::-1]

if __name__ == "__main__":
    test = "madam"
    print(is_palindrome(test))  # Output: True
