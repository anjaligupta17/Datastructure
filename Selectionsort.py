def SelectionSort(list1,k):
    for i in range((k)):
        minpos=i
        for j in range(i,(k)):
           if list1[j]<list1[minpos]:
                minpos=j
        temp=list1[i]
        list1[i]=list1[minpos]
        list1[minpos]=temp
num=int(input())
list1=[int(input()) for i in range(num)]
SelectionSort(list1,num)
print(list1)