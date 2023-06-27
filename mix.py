print("enter your T and S")
T, S = map(int, input().split())

J = T**S 
print('Total variants T^S:', (format(J, "e")))
print(J)

print("your ems")
print("insert your ems, e.g. 5 4 3 2")
array1 = list(map(int, input().split()))

print("insert your ens e.g. 4 3 2 1")
print("your ens")
array2 = list(map(int, input().split()))

# Resize the arrays by filling with zeros
array1 = array1 + [0, 0, 0, 0]
array2 = array2 + [0, 0, 0, 0]

m7, m6, m5, m4 = array1[:4]
n7, n6, n5, n4 = array2[:4]

ens = int(n7) + int(n6) + int(n5) + int(n4)
kmn = int(m7) * int(n7) + int(m6) * int(n6) + int(m5) * int(n5) + int(m4) * int(n4)
Z = int(ens) + (S - kmn)
print('Your Z is:', int(Z))

import math

a = math.factorial(T)
b = math.factorial(T - Z) if T - Z >= 0 else 1  # Add check for non-negative argument
c = math.factorial(S)
d = (
    math.factorial(m7) ** n7
    * math.factorial(n7)
    * math.factorial(m6) ** n6
    * math.factorial(n6)
    * math.factorial(m5) ** n5
    * math.factorial(n5)
    * math.factorial(m4) ** n4
    * math.factorial(n4)
    * math.factorial(S - kmn) if S - kmn >= 0 else 1  # Add check for non-negative argument
)
e = int(a) / int(b)
f = int(c) / int(d)
g = int(e) * int(f)
print(format(g, "e"))
print(g)
#print(f"{g:,}")
h = int(g) / int(J)
l = h * 100
#print(l, '%')
print(l,"% from total variants T^S")