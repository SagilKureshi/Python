# this only sorts the values, not the complete dictionary with its keys.

# my_dict = {'a': 40, 'b': 10, 'c': 30, 'd': 20}

# values = list(my_dict.values())
# values.sort()

# print("Ascending values:", values)

# values.sort(reverse=True)

# print("Descending values:", values)

my_dict = {'a': 40, 'b': 10, 'c': 30, 'd': 20}

ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Ascending Order:", ascending)
print("Descending Order:", descending)