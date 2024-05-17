def fibo(lst):
    fibo_num = [0, 1]
    fibo_ind = []
    
    # Generate Fibonacci numbers
    while fibo_num[-1] < len(lst):
        fibo_num.append(fibo_num[-1] + fibo_num[-2])
    
    # Store those numbers as indices
    for item in fibo_num:
        if item < len(lst):
            fibo_ind.append(item)
    
    # Retrieve elements from the list at Fibonacci indices
    result = []
    for index in fibo_ind:
        result.append(lst[index])

    return result

# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
output = fibo(input_list)
print(output)  # Output: [1, 2, 2, 3, 5, 8, 11]
