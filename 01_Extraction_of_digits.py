"""
Problem: Extration of digits from a number 
Approach:
- Repearedly extract last digit using modulo (%)
- Remove last digit using floor division (//)

Time complexity: O(d) where d = number of digits
"""

num = int(input("Enter a Number: "))

if num == 0:
  print(0)
  
while num > 0:
  last_digit = num % 10
  print(last_digit)
  num = num // 10
