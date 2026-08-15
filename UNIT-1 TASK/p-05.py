a = 10
b = 3

print("Arithmetic Operation :- \n")

print("a = ", a)
print("b = ", b)

print("a+b = ", a+b)
print("a-b = ", a-b)
print("a*b = ", a*b)
print("a/b = ", a/b)
print("a**b = ", a**b)
print("a//b = ", a//b)
print("a%b = ", a%b)

print("\nRelational Operation :- \n")

print("a==b = ", a==b)
print("a!=b = ", a!=b)
print("a>b = ", a>b)
print("a<b = ", a<b)
print("a>=b = ", a>=b)
print("a<=b = ", a<=b)

print("\nAssignment Operation :- \n")

c = a
print("c = ", c)

c += b
print("c+=b = ", c)

c -= b
print("c-=b = ", c)

c *= b
print("c*=b = ", c)

c /= b
print("c/=b = ", c)

c %= b
print("c%=b = ", c)

print("\nLogical Operation :- \n")

print("a>5 and b<5 = ", a>5 and b<5)
print("a>15 or b<5 = ", a>15 or b<5)
print("not(a>b) = ", not(a>b))

print("\nBitwise Operation :- \n")

print("a&b = ", a&b)
print("a|b = ", a|b)
print("a^b = ", a^b)
print("~a = ", ~a)
print("a<<1 = ", a<<1)
print("a>>1 = ", a>>1)

print("\nTernary Operation :- \n")

c = a if a > b else b
print("Greater value = ", c)