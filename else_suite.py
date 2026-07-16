for i in range(5):
    print("YES")    

else:
    print("NO")    
 
print()

l = [1,2,3,4,5]
num = int(input("Enter a number : "))
for i in l:
    if num == i:
        print(f"{num} exists in list")
        break
else:
    print(f"{num} not exists in in list")