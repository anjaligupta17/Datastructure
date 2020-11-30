pos=-1
def linear(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False
list=[12,1,34,5,23]
n=23
if linear(list,n):
    print("found",pos+1)
else:
    ("not found")