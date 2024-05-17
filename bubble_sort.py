def bubble_sort(num):
    n = len(num)
    for i in range(n-1):
        for j in range(i+1,n):
            if num[i] > num[j]:
                num[i],num[j] = num[j],num[i]
    return num

lst = [23,34,63,63,63,6,54,2]
sorty = bubble_sort(lst) 
print(sorty)           