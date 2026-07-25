# NO Argument NO return

# def fun(): 
#     print("Hello from UDF function")

# fun() 

# NO argument with return

# def fun(): 
#     return "retun something"

# print(fun()) 

# With Argumnets NO return

# def sum(a,b): 
#     c=a+b 
#     print(c)
# sum(5,10)

# With argument with return

# def sum(a,b): 
#     return a+b  

# res=sum(5,10) 
# print('the result is',res) 

#a function to test whether a number is odd or even 

# def even_odd(num): 
#     if num%2==0: 
#         print(num," is even") 
#     else: 
#         print(num," is odd") 

# even_odd(10) 
# even_odd(13) 

# a function that returns multiple results 

# def sum_sub_mul_div(a,b): 
#     c=a+b 
#     d=a-b 
#     e=a*b 
#     f=a/b 
#     return c,d,e,f 
 
# #get resuts from sum_sub_mul_div() function and store into t 
# t=sum_sub_mul_div(10,5) 
 
# #display the results using for loop 
# print("The results are") 
# for i in t: 
#     print(i,end=", ")

# a function to calculate factorial value 
# def fact(n): 

#     prod=1 
#     while n>=1: 
#         prod*=n 
#         n-=1 
#     return prod 
 

# for i in range(1,11): 
#     print("factorial of {} is {}".format(i,fact(i)))