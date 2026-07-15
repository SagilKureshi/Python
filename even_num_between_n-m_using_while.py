n = int(input("Enter staring number : "))
m = int(input("Enter ending number : "))
x = n
while x >= n and x <= m:
    if( x % 2 == 0):
        print(x,"is even")
    else:
        print(x,"is odd")
    x += 1