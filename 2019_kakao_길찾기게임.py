import sys
sys.setrecursionlimit(10**6)

from queue import PriorityQueue

class Node:
    def __init__(self, data, x,left=None, right=None):
        self.data =data
        self.x = x
        self.left = left
        self.right = right
    
    def pre(self):
        tra = []
        tra.append(self.data)
        
        if self.left:
            tra += self.left.pre()
        if self.right:
            tra += self.right.pre()
        return tra
    
    def post(self):
        tra =[]
         
        if self.left :
            tra += self.left.post()
        if self.right :
            tra += self.right.post()
            
        tra.append(self.data)
        return tra
class Tree:
    def __init__(self, root):
        self.root = root
    
    def pre(self):
        if self.root:
            return self.root.pre()
        else:
            return []
        
    def post(self):
        if self.root :
            return self.root.post()
        else:
            return []
    def insert(self, data, x):
        self.root =self.ins(self.root, data, x)
        return self.root is not None
    def ins(self, node, data, x):
        if node is None:
            node = Node(data, x)
        else:
            if x < node.x :
                node.left = self.ins(node.left, data, x) 
            else :
                node.right = self.ins(node.right, data, x)
        return node

def solution(nodeinfo):
    answer = []
    
    que = PriorityQueue()
    
    MAXVALUE = 100001
    
    for idx, node in enumerate(nodeinfo):
        que.put((MAXVALUE - node[1], [node[0], idx + 1]))
    
    q =que.get()
    node = Node(q[1][1], q[1][0]) 
    
    binaryTree =Tree(node)
    
    while not que.empty():
        q = que.get()
        binaryTree.insert(q[1][1], q[1][0])
        
    answer.append(binaryTree.pre())
    answer.append(binaryTree.post())

    
    return answer
