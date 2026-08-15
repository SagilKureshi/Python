# Function to check palindrome number

def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if reverse == original:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if palindrome(num):
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")