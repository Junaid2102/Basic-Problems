'''
    Given a binary tree, find the largest value at each level
'''


class Nodes:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None


def eachnode(node, n, sol):
    if(not node):
        return
    if(n == len(sol)):
        sol.append(node.val)
    else:
        sol[n] = max(sol[n], node.val)

    eachnode(node.left, n+1, sol)
    eachnode(node.right, n+1, sol)


def getvalues(node):
    sol =[]
    eachnode(node, 0, sol)
    return sol


node = Nodes(4)
node.left = Nodes(9)
node.right = Nodes(2)
node.left.left = Nodes(3)
node.left.right = Nodes(5)
node.right.right = Nodes(7)

print(getvalues(node))