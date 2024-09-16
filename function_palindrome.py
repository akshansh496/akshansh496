n=int(input("Enter a number"))
def is_palindrome(num):
    num1=num
    rev=0
    while num!=0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev==num1
if(is_palindrome(n)==True):
    print(n,"is palindrome number")
else:
    print(n,"is not a palindrome number")


