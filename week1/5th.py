n = 8
a, b = 0, 1
l = []
for i in range(n):
    l.append(a)
    a, b = b, a+b
    
print(l)