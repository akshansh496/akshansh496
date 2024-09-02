x=int(input("Enter a number"))
fact=1
for i in range(x,0,-1):
    fact*=i
    i+=1
print(fact)