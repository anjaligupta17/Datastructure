class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
#Traverse
    def listprint(self):
        temp=self.head
        if temp is None:
            print("is emoty")
        out=""
        while temp is not None:
            out += str(temp.data)
            print(" ")
            temp=temp.next
        print (out)
    def Atbegining(self,newdata):
        NewNode=Node(newdata)
#insertion
        NewNode.next=self.head
        self.head=NewNode
list1=LinkedList()
e1=Node("Mon")
list1.head=e1
e2=Node("Tue")
e3=Node("wed")
e4=Node("thur")

#link first node to next node

list1.head.next=e2
#link second node to third and fourth

e2.next=e3
e3.next=e4 
list1.listprint()