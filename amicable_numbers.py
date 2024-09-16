x=int(input("Enter a number"))
y=int(input("Enter a number"))
def check_amiable_numbers(num1,num2):
    summ=0
    i=1
    s=0
    while i in range(num1):
        if num1%i==0:
            summ+=i
        i+=1
    i=1
    while i in range(num2):
        if num2%i==0:
            s+=i
        i+=1
    return summ==num2 and s==num1
if check_amiable_numbers(x,y)==True:
    print("amiable")
else:
    print("not amiable")
