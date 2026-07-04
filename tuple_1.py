t1 = ()
print(t1)

t2 = (1,34.3,'hi')
print(t2)

l = [1,34,64,3]
t3 = tuple(l) #using list
print(t3)

t4 = (  53,34,34,5)
#t4[0] = 4  immutable
for i in t4:
    print(i,end=" ")

t5 = tuple("Belive in your self")
print("\n")
print(t5[0])
print(t5[1:3])
print(t5[:3])
print(t5[:])
print(t5[1::2])
print(t5[:10:2])

t6 = (1,2,3)
a,b,c, = t6
print(a,b,c)

t7 = (1,2,3,4,5,6,7,8,9)
x,*y,z = t7
print(x,y,z)

tup1 = ('Hello')
tup2 = ('Universe')
tup3 = tup1 +" "+ tup2
print(tup3)

t8 = (1,3,5)
print(t8)
del t8
#print(t8) # give error because it is deleted