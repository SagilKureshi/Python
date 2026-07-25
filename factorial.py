def fact(n): 

    prod=1 
    while n>=1: 
        prod*=n 
        n-=1 
    return prod 
 

for i in range(1,11): 
    print("factorial of {} is {}".format(i,fact(i)))