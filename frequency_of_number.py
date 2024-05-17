def find_frequency(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
lst = [1,2,3,2,1,3,2,1,2,3]
result = find_frequency(lst)
print(f" Frequency of number is {result}")