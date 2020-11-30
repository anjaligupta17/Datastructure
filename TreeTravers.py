#in order traversal:-left->root->right
#pre order traversal:-root->left->right
#post order traversal:-left->right->root
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
#inserting
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
#printing
    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()
#Inorder
    def inorderwork(self,root):
        res=[]
        if root:
            res=self.inorderwork(root.left)
            res.append(root.data)
            res=res+self.inorderwork(root.right)
        return res
    def Preorder(self,root):
        res=[]
        if root:
            res.append(root.data)
            res=res+self.Preorder(root.left)
            res=res+self.Preorder(root.right)
        return res
    def Postorder(self,root):
        res=[]
        if root:
            res=self.Postorder(root.left)
            res=res+self.postorder(root.right)
            res.append(root.data)
        return res
root=Node(27)
root.insert(12)
root.insert(34)
print(root.inorderwork(root))
print(root.Preorder(root))