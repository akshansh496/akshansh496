x=int(input("Enter a number:"))
def factorial(a):
    fact=1
    i=1
    while i in range(a+1):
        fact=fact*i
        i+=1
    return fact
def check_strong_number(num):
    n=num
    summ=0
    while n!=0:
        r=n%10
        summ=summ+factorial(r)
        n=n//10
    return summ==num
if check_strong_number(x)==True:
    print("Strong  number")
else:
    print("Not a Strong  number")
