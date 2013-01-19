'''
Created on 27 nov 2012

@author: gustaf

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
        
    def set_data(self, data):
        self.data = data
        
    def pop(self):
        return self.children.pop()    
        
class Expression:
    def __init__(self):
        pass
    def evaluate(self):
        pass
    
class Number(Expression):
    def __init__(self, value):
        self.value = value
    def evaluate(self):
        return self.value
    
class Plus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
    
one = Node(Number(1))
two = Node(Number(2))

tree = Node(None)
tree.add_child(one)
tree.add_child(two)
tree.set_data(Plus(tree.pop().data, tree.pop().data))
print tree.data.evaluate()

