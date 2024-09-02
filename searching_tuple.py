list=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100,)
x=int(input("Enter element to be searched:"))
i=0
while i<len(list):
    if(x==list[i]):
        print(x,"is present at index",i)
    i+=1     
