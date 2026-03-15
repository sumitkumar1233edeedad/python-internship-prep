n = 100
l = []
for i in range(2,n):
    
    prime = True
    for p in range(2, i):
        if i%p == 0:
            prime = False
       
    if prime:
        l.append(i)
print(l)