# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact (n-1)

    
def find_factorial(num):
    if num == 0:
        return 1
    else:
        return num*find_factorial(num - 1)
    
    
number = 5
result = find_factorial(number)
print(f" Factorial of a {number} is {result }")

        