def fun(n):
    if n == 0:
        return 1
    else:
        result = n*fun(n-1)
    return result
for i in range(1,5):
    print(f"factorial of {i} is : {fun(i)}")