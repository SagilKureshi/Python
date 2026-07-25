#recursive function to calculate factorial 
def factorial(n): 
    if n==0: 
        result=1 
    else: 
        result=n*factorial(n-1) 
        
    return result 
#find factorial values for first 10 numbers 
for i in range(1,11): 
    print("Factorial of {} is {}".format(i,factorial(i))) 