l1 = [1,2.5,"hello"]
print(l1)

l2 = list((1,34.3,'hi'))
print(l2)

l3 = list("SMILE")
print(l3)

l4 = [1,3.14,'be happy']
print(l4[1])
print(l4[0])
print(l4[-1])

l5 = [1,3,5,6]
print(l5[1]*5)
print(l5[3]*2)

l6 = [1,2]
print(l6)
l6.insert(2,3)  #insert(index,element)
print(l6)
l6.extend([2,1]) # add multiple elements
print(l6)

l7 = [1,2,3,4,5]
print(l7)
l7[0] = 0 #update
print(l7)
l7.remove(5)
print(l7)
l7.pop() #remove last element 
print(l7) 
l7.pop(1) #remove index base on index
print(l7) 

l8 =[34,34,2]
print(l8)
del l8[0]
print(l8)
l8.clear() #remove all elements
print(l8)

l9 = ['apple','banana','cherry']
for i in l9:
    print(i)

l10 = [[1,2],[3,4]] # nested list
print([l10[0]])
print([l10[1][1]])

l11 = ['red','green','yellow']
print(l11.index('green'))

l12 = ['hello','hi','hi','bye','hi']
print(l12.count('hi'))

l13 = [5, 34, 6, 3, 2]
l13.sort()
print(l13)

l14 = ['a','b','c']
l14.reverse()
print(l14)

original = [1,3]
duplicate = original.copy()
print(original)
print(duplicate)