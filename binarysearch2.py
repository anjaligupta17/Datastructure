pos =-1
def binary14(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
list=[93,23,2,3,5,6,98,19]
n=23
if binary14(list,n):
    print("found",pos+1)
else:
    print("not found")