"""
Problem: Frequency count of elements in a list

Method 1: Manual dictionary check
Method 2: Using dictionary get() method (clean & pythonic)

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Method 1: Manual Check
def freq_count(nums):
    freq = {}
    for i in range(len(nums)):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    return freq


# Method 2: Using dict.get()
def freq_count_02(nums):
    freq = {}
    for i in range(len(nums)):
        freq[nums[i]] = freq.get(nums[i], 0) + 1
    return freq


# Driver Code
nums = list(map(int, input("Enter elements separated by spaces: ").split()))

print("Frequency (Method 1):", freq_count(nums))
print("Frequency (Method 2):", freq_count_02(nums))

  

      
