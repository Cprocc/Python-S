import os
s = input( ).split( )
l = float(s[0])
k = float(s[1])
a = float(s[2])
b = float(s[3])
if (a==b):
    print(0)
    os._exit(0)
kt = l/a
rt = k/(a-b)
s = (l-kt*b)
if (s>k  and (l-a*2*rt)>k):
    print(round(2*rt-kt,2))
else:
    print(round(l/b-kt,2))