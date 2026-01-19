"""
Problem: Count the number of digits in a number

Method 1: Using digit extraction
Approach:
- Repeatedly remove last digit using integer division (//)
- Increase count by 1 until number becomes 0

Time Complexity: O(d) where d = number of digits
Space Complexity: O(1)

Method 2: Using logarithm
Approach:
- digits = floor(log10(n)) + 1

Time Complexity: O(1)
Space Complexity: O(1)
"""

from math import log10

# 1. Method Digit Extraction
def count_digits_iterative(num):
    if num == 0:
        return 1

    count = 0
    while num > 0:
        count += 1
        num //= 10

    return count


# 2. Logarithmic
def count_digits_log(num):
    if num == 0:
        return 1

    return int(log10(num)) + 1


num = int(input("Enter a number: "))

print("Count (Iterative):", count_digits_iterative(num))
print("Count (Log):", count_digits_log(num))
