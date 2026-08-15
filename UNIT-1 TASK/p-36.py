# list1 = [10, 20, 30, 40, 50, 60, 70]

# new_list = [value for index, value in enumerate(list1)
#             if index not in (0, 2, 3, 5)]

# print("Original list:", list1)
# print("List after removing the 0th, 2nd, 3rd and 5th elements:", new_list)

list1 = [10, 20, 30, 40, 50, 60, 70]
print("Original list:", list1)

list1.pop(5)
list1.pop(3)
list1.pop(2)
list1.pop(0)

print("List after removing the 0th, 2nd, 3rd and 5th elements:", list1)