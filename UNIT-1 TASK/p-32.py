# Function to check Armstrong number

def armstrong(num):
    original = num
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit ** 3
        num = num // 10

    if sum == original:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")