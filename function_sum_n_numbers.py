n=int(input("Enter range:"))
def find_sum(num):
    summ=0
    for i in range(num+1):
        summ+=i
        i+=1
    return summ
print("Sum of numbers till",n,"is",find_sum(n))