n=int(input("enter a no."))
x=0
y=1
print(x)
print(y)
i=1
while i<n/2:
    x=y+x
    y=y+x
    print(x)
    print(y)
    i+=1