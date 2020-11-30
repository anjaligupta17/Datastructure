def mergesort(list):
    if len(list)>1:
        mid=len(list)//2
        left_list=list[:mid]
        right_list=list[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(left_list):
            if left_list[i]<right_list[i]:
               list[k]=left_list[i]
               i=i+1
               k=k+1
            else:
               list[k]=right_list[j]
               k=k+1
               j=j+1
        while i<len(left_list):
               list[k]=left_list[i]
               i=i+1
               k=k+1

        while j<len(left_list):
            list[k]=right_list[j]
            j=j+1
            k=k+1
num=int(input("how many element you want in list:"))
list=[int(input())for x in range(num)]
mergesort(list)
print("sorted",list)