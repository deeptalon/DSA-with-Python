"""
Problem: Find all factors of a number

Method 1: Naive approach
- Check all numbers from 1 to n

Time Complexity: O(n)
Space Complexity: O(k)

Method 2: Half-range optimization
- Check numbers from 1 to n//2

Time Complexity: O(n)
Space Complexity: O(k)

Method 3: Square-root optimization (INTERVIEW METHOD)
- Check numbers from 1 to sqrt(n)
- Add factor pairs (i, n//i)

Time Complexity: O(sqrt(n))
Space Complexity: O(k)
"""

import math

# Method 1: Naive 
def find_factors_naive(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


# Method 2: Half Range
def find_factors_half(num):
    factors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
    return factors


# Method 3: Square Root (Best)
def find_factors_sqrt(num):
    factors = []

    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:   # avoid duplicate for perfect square
                factors.append(num // i)

    return sorted(factors)


num = int(input("Enter a number: "))

print("Naive Method :", find_factors_naive(num))
print("Half Method  :", find_factors_half(num))
print("Sqrt Method  :", find_factors_sqrt(num))
