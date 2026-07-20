x = int(input("Enter a number greater than 0 :"))
try:
    assert x>0
    print("you entered",x)
except AssertionError:
    print("Wrong number entered")

