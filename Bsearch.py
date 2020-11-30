def bsearch(list,val):
    list_index=len(list)-1
    index=0
    index1=list_index

#middle
    while index <=index1:
        mid=(index+index1)//2
        if list[mid]==val:
            return mid

#left and right
        if val>list[mid]:
            index=mid+1
        else:
            index1=mid-1
    if index>index1:
        return None
list=[1,2,3,45]
print(bsearch(list,2))
print(bsearch(list,45))

