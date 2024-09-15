x=int(input("Enter a no."))
count=0
i=1
for i in range(x):
    n=i+1
    if x%n==0:
        count=count+1
if count==2:
    print("Prime no.")
else:
    print("Not prime")