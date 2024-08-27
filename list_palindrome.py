list=[]
list.append(input("enter a element"))
list.append(input("enter a element"))
list.append(input("enter a element"))
list.append(input("enter a element"))
list.append(input("enter a element"))
l=len(list)
list2=list.copy()
list2.reverse()
if(list==list2):
    print("palindrome")
else:
    print("not palindrome")
