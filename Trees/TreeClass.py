
# Designing a tree from scratch

class Node():
    def __init__(self,a):
        self.value = a
        self.right = None
        self.left = None

class Tree():
    def __init__(self):
        self.root = None
        self.length = 0
        
