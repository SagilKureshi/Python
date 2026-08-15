def calculate(a, b):
    sum = a + b
    difference = a - b
    product = a * b
    return sum, difference, product

x, y, z = calculate(10, 5)

print("Sum =", x)
print("Difference =", y)
print("Product =", z)