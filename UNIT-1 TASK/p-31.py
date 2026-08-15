# Function to reverse a value

def reverse_value(value):
    return value[::-1]

value = input("Enter a value: ")

result = reverse_value(value)

print("Reversed value:", result)