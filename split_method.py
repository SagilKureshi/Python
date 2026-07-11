data = "apple,banana,cherry,orange"
result = data.split(",")
print(result)


a,b,c = [int(x) for x in input("Enter three Numbers : ").split(",")]
print("sum = ",a+b+c)