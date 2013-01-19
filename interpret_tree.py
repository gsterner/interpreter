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
    def __init__(self):
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
                
    def pop(self):
        return self.children.pop()    
    
    def evaluate(self):
        pass
    
    def get_children(self):
        return self.children

    
class Number(Node):
    def __init__(self, value):
        Node.__init__(self)
        self.value = value
    def evaluate(self, arg):
        return self.value

class Variable(Node):
    def __init__(self):
        Node.__init__(self)
    def evaluate(self, arg):
        return arg
    
class Plus(Node):
    def __init__(self):
        Node.__init__(self)
        
    def evaluate(self, arg):
        return self.get_children()[0].evaluate(arg) + self.get_children()[1].evaluate(arg)

class Minus(Node):
    def __init__(self):
        Node.__init__(self)
        
    def evaluate(self, arg):
        return self.get_children()[0].evaluate(arg) - self.get_children()[1].evaluate(arg)

class Multiply(Node):
    def __init__(self):
        Node.__init__(self)
        
    def evaluate(self, arg):
        return self.get_children()[0].evaluate(arg) * self.get_children()[1].evaluate(arg)

class Divide(Node):
    def __init__(self):
        Node.__init__(self)
        
    def evaluate(self, arg):
        return self.get_children()[0].evaluate(arg) / self.get_children()[1].evaluate(arg)

    
four = Number(4)
x = Variable()
two = Number(2)
three = Number(3)
multi = Multiply()

tree = Plus()
tree.add_child(multi)
tree.add_child(three)
multi.add_child(two)
multi.add_child(x)

print tree.evaluate(3)

