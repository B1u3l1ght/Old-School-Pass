print("enter your T and S")
T, S = map(int, input().split())

#T=94
#S=16

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
#print(kmn)
print('Your Z is:', int(Z))

import mpmath

# Set the desired precision
mpmath.mp.dps = 1000

a = mpmath.factorial(T)
b = mpmath.factorial(T-Z)
#print(b)
c = mpmath.factorial(S)
p = mpmath.factorial(n7)*(mpmath.factorial(m7))**n7
o = mpmath.factorial(n6)*(mpmath.factorial(m6))**n6
j = mpmath.factorial(n5)*(mpmath.factorial(m5))**n5
w = mpmath.factorial(n4)*(mpmath.factorial(m4))**n4
dum = p*o*j*w*mpmath.factorial(S-kmn)
#print(dum)
e = abs(a)/abs(b)
f = abs(c)/abs(dum)
#print(f)
g = abs(e)*abs(f)
#print(format(g, "e"))
print(int(g))
#print(f"{e:,}")
h = g/J
l = h * 100
#print(l, '%')
#print(l,"% from total variants T^S")