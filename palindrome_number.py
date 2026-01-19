"""
Problem: Whether a Number is Palindrome or not.

Approach:
- Store Original Number.
- Reversing the number.
- compare reversed and Original number.
"""

def is_palindrome(num):

  if num < 0:
    return False
    
  original_num = num
  reversed_num = 0
  
  while num > 0:
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num = num // 10
  return reversed_num == original_num

# Driver The code
number = int(input("Enter a Number: "))

if is_palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")
