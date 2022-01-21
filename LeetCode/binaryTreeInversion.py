from logging import root
from traceback import print_tb
from turtle import right
from binarytree import Node


        
head = Node(1, 
            Node(2, 
                 Node(3), 
                 Node(4)), 
            Node(2, 
                 Node(4), 
                 Node(3)))



print(head)
def symetric(root):
    roota, rootb = root.right, root.left
    
    def preorderTraverse(root, l = []):
        if root:
            l.append(root.val)
            preorderTraverse(root.right)
            preorderTraverse(root.left)
            return root, l
    
    def invert(rootb):
        if rootb == None:
            return rootb
        right = invert(rootb.right)
        left = invert(rootb.left)
        rootb.right = left
        rootb.left = right
        return rootb
    rootb = invert(rootb)
    
    x,la = preorderTraverse(roota)
    x,lb = preorderTraverse(rootb)
    print(f"la: {la}\nlb: {lb}")
    return la == lb


def preorderTraverse(root, l = []):
    if root == None:
        return root
    l.append(root.val)
    preorderTraverse(root.left)
    preorderTraverse(root.right)
    return root, l

print(head)
print(symetric(head))