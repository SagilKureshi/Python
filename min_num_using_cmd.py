import sys
no1 = sys.argv[1]
no2 = sys.argv[2]
no3 = sys.argv[3]

if no2 > no1 < no3:
    print(f"{no1} is minimum")
elif no1 > no2 < no3:
    print(f"{no2} is minimum")
elif no1 > no3 < no2:
    print(f"{no3} is minimum")

else:
    print("2 or more number has same value")