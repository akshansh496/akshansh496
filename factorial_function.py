x=int(input())
def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
        i+=1
    print(fact)
factorial(x)