 # Define a function to find the length of the longest increasing subsequence in a list
def longest_increasing_subsequence(nums):
    # Get the length of the input list
    n = len(nums)
    
    # Create a list 'arr' to store the length of the longest increasing subsequence
    arr = [1] * n
    
    # Iterate over the elements in the list
    for i in range(1, n):
        # Iterate over elements before the current element 'i'
        for j in range(i):
            # Check if the current element is greater than the previous element
            if nums[i] > nums[j]:
                # Update the length of the longest increasing subsequence for the current element 'i'
                arr[i] = max(arr[i], arr[j] + 1)
    
    # Return the maximum value in the 'arr' list, which represents the length of the longest increasing subsequence
    return max(arr)

# Create a list of numbers
nums = [10, 20, 30, 40, 50, 60, 70, 50]

# Print the original list
print("Original list:")
print(nums)

# Call the longest_increasing_subsequence function and print the result
print("Length of the longest increasing sub-sequence in the said list:")
print(longest_increasing_subsequence(nums))

# Create another list of numbers
nums = [10, 20, 30, 40, 50, 30, 30, 20]

# Print the original list
print("\nOriginal list:")
print(nums)

# Call the longest_increasing_subsequence function with the second list and print the result
print("Length of the longest increasing sub-sequence in the said list:")
print(longest_increasing_subsequence(nums))

# Create a third list of negative numbers
nums = [-1, -2, -3, -4, -5, -11, -12, -13]

# Print the original list
print("\nOriginal list:")
print(nums)

# Call the longest_increasing_subsequence function with the third list and print the result
print("Length of the longest increasing sub-sequence in the said list:")
print(longest_increasing_subsequence(nums))
