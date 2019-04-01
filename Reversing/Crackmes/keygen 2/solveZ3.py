from z3 import *

a = Int('a')
b = Int('b')
c = Int('c')
d = Int('d')
e = Int('e')
f = Int('f')
g = Int('g')
h = Int('h')
i = Int('i')
j = Int('j')
k = Int('k')
l = Int('l')
m = Int('m')
n = Int('n')
o = Int('o')
p = Int('p')

s = Solver()
s.add(a<36, b<36, c<36, d<36, e<36, f<36, g<36, h<36, i<36, j<36, k<36, l<36, m<36, n<36, o<36, p<36)
s.add(a>=0, b>=0, c>=0, d>=0, e>=0, f>=0, g>=0, h>=0, i>=0, j>=0, k>=0, l>=0, m>=0, n>=0, o>=0, p>=0)
s.add((a+b)%0x24 == 0xe)
s.add((c+d)%0x24 == 0x18)
s.add((c-a)%0x24 == 0x6)
s.add((b+d+f)%0x24 == 0x4)
s.add((c+e+g)%0x24 == 0xd)
s.add((d+e+f)%0x24 == 0x16)
s.add((g+i+k)%0x24 == 0x1f)
s.add((b+e+h)%0x24 == 0x7)
s.add((j+m+p)%0x24 == 0x14)
s.add((n+o+p)%0x24 == 0xc)
s.add((i+j+k)%0x24 == 0x1b)
s.add((h+m+n)%0x24 == 0x17)
print(s.check())
print(s.model())