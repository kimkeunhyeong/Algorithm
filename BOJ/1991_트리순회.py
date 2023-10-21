from sys import stdin

def preorder(root):
    if root == ".":
        return ""
    result = root
    result += preorder(Tree[root][0])
    result += preorder(Tree[root][1])

    return result

def inorder(root):
    if root == ".":
        return ""
    result = inorder(Tree[root][0])
    result += root
    result += inorder(Tree[root][1])

    return result

def postorder(root):
    if root == ".":
        return ""
    result = postorder(Tree[root][0])
    result += postorder(Tree[root][1])
    result += root

    return result

input = stdin.readline
N = int(input())

Tree = dict()
for i in range(N):
    root, left, right = input().rstrip().split()
    Tree[root] = (left, right)

print(preorder("A"), inorder("A"), postorder("A"), sep = "\n")