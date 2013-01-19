
from bin_tree import *
from gstack import GStack

def create_new_operator(operator_string):
    if(operator_string == '+'):
        operator = Plus()
    if(operator_string == '-'):
        operator = Minus()
    if(operator_string == '*'):
        operator = Multiply()
    if(operator_string == '/'):
        operator = Divide()
    return operator

def change_node(destination, source):
    destination.set_left(source)
    destination.set_right(source) 

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = GStack()
    eTree = Node()
    pStack.push(eTree)
    currentTree = eTree
    print fplist
    for i in fplist:
        if i == '(':
            print 'par'
            currentTree.insert_left(Node())
            pStack.push(currentTree)
            currentTree = currentTree.get_left()
        elif i not in ['+', '-', '*', '/', ')']:
            print 'number', i, pStack._data
            number = Number(i)
            change_node(number, currentTree)
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            print 'operator', i, pStack._data
            operator = create_new_operator(i)
            change_node(operator, currentTree)
            currentTree.insert_right(Node())
            pStack.push(currentTree)
            currentTree = currentTree.get_right()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")


