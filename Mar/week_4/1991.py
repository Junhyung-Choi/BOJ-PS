#BOJ 1991 - 트리 순회
import sys
input = sys.stdin.readline

def preorder(node):
    if node != None:
        print(node.value,end = "")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.value,end = "")
        inorder(node.right)


def postorder(node):
    if node != None:
        postorder(node.left)
        postorder(node.right)
        print(node.value,end = "")

class node:
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

treenodes = []
treesize = int(input())

def findNode(value):
    for idx in range(len(treenodes)):
        if value == treenodes[idx].value:
            return idx
    return -1

rootnode = node("A",None,None)
treenodes.append(rootnode)

for i in range(treesize):
    head, left, right = map(str,input().rstrip().split(" "))
    # print("head is ",head, "head index is ",findNode(head))
    # print("left is ",left, "left index is ",findNode(left))
    # print("right is ",right, "right index is ",findNode(right))
    if findNode(head) == -1:
        if left == ".":
            leftnode = None
        elif findNode(left) == -1:
            leftnode = node(left,None,None)
            treenodes.append(leftnode)
        else:
            leftnode = treenodes[findNode(left)]

        if right == ".":
            rightnode = None
        elif findNode(right) == -1:
            rightnode = node(right,None,None)
            treenodes.append(rightnode)
        else:
            rightnode = treenodes[findNode(right)]
        
        headnode = node(head,leftnode,rightnode)
        treenodes.append(headnode)
    else:
        headnode = treenodes[findNode(head)]
        if left == ".":
            leftnode = None
        elif findNode(left) == -1:
            leftnode = node(left,None,None)
            treenodes.append(leftnode)
        else:
            leftnode = treenodes[findNode(left)]
        if right == ".":
            rightnode = None
        elif findNode(right) == -1:
            rightnode = node(right,None,None)
            treenodes.append(rightnode)
        else:
            rightnode = treenodes[findNode(right)]
        headnode.left = leftnode
        headnode.right = rightnode
        treenodes[findNode(head)] = headnode
'''
for n in treenodes:
    try:
        print("Val: ", n.value, "left: ", n.left.value, "right: ",n.right.value)
    except:
        print(n.value ,"'s child has None")
'''
preorder(rootnode)
print()
inorder(rootnode)
print()
postorder(rootnode)
print()