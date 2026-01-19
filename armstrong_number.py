"""
Problem: Check whether a number is an Armstrong number

Approach:
- Count number of digits (d)
- Extract each digit
- Raise digit to power d and add
- Compare with original number

Time Complexity: O(d)
Space Complexity: O(1)
"""

def count_digits(num):
    if num == 0:
        return 1

    count = 0
    while num > 0:
        count += 1
        num //= 10

    return count


def is_armstrong(num):
    if num < 0:
        return False

    original = num
    digits = count_digits(num)
    armstrong_sum = 0

    while num > 0:
        digit = num % 10
        armstrong_sum += digit ** digits
        num //= 10

    return armstrong_sum == original


# Driver Code
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
