start = 0
end = 50
for i in range(start,end):
    if i%3 == 0 and i%5 ==0:
        print(f" {i} fizz buzz")
    elif i%3 == 0:
        print(f" {i} fizz")
    elif i%5 == 0:
        print(f"{i} buzz")
    # else:
        # print("not a fizz not a buzz and not fizzbuzz")