list=[1,4,9,16,25,36,49,64,81,100]
x=int(input("Enter number to be searched"))
for el in list:
    if(x==el):
        print(x,"is founded")
        break
else:
    print(x,"is not present")
