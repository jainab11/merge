lst = [1,2,3,4,5]
n1 = 0
n2 = 1
count = 0
fibo_lst = []
n = len(lst)
for i in range(n):
    nth = n1+n2
    n1 = n2
    n2 = nth
    fibo_lst.append(n1)
for j in fibo_lst:
    
    count += lst[i]
print(fibo_lst)