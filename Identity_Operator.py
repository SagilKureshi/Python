s = 10
k = 10

print("s = ",s)
print("k = ",k)

# is operator & is not Operator

print(f"\ns == k : {s == k}")
print(f"s is k : {s is k}")
print(f"s is not k : {s is not k}")

s = [1,2,3]
k = [1,2,3]

print("\ns = ",s)
print("k = ",k)

print(f"\ns == k : {s == k}")
print(f"s is k : {s is k}")
print(f"s is not k : {s is not k}")

s = (1,2,3)
k = (1,2,3)

print("\ns = ",s)
print("k = ",k)

print(f"\ns == k : {s == k}")
print(f"s is k : {s is k}")
print(f"s is not k : {s is not k}")

s = {1,2,3}
k = {1,2,3}

print("\ns = ",s)
print("k = ",k)

print(f"\ns == k : {s == k}")
print(f"s is k : {s is k}")
print(f"s is not k : {s is not k}\n")

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(id(list_a))  # Output example: 140231920803264
print(id(list_b))  # Output example: 140231920805120 (Different address)
print(id(list_c))  # Output example: 140231920803264 (Same address as list_a)

# Identity checks
print(list_a is list_b)  # False
print(list_a is list_c)  # True


