
# x = int(input('Enter a number greater than 0 : ')) 
# assert x>0,"Wrong input entered" 
# print("You entered : ",x) 

x2 = int(input('Enter a number greater than 0:')) 
try: 
    assert(x2>0)   
    print("u entered : ",x2) 
except AssertionError: 
    print("wrong input entered") 