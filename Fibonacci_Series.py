def fibonacci(n):
    s = 0 
    k = 1
    n = 2
    print(s)
    print(k)
    while n < choice:
        sum = s+k
        print(sum)
        s = k
        k = sum
        n+=1

choice = int(input("Enter the number of fibonacci series : "))
fibo = fibonacci(choice)



