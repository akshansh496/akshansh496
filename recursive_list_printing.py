def print_lis(list,idx=0):
    if(idx==len(list)):
        return
    else:
        print(list[idx])
        print_lis(list,idx+1)
list1=[1,2,3,4,5,5,4]
print_lis(list1)
