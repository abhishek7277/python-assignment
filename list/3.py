def extract_digits_reverse(n):
   digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    return digits[::-1]
