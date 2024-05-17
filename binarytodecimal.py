number = 25
ans  = " "
while number > 0:
    remainder = number % 2
    ans = str(remainder)+ans
    number = number // 2
print(ans) 
print(25 & 13)
print(23 ^ 13)
print(23 | 13)
print(~ 13)
print(bin(25))
print(bin(13))