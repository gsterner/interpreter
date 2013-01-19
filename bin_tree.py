

class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None

    def insert_left(self, obj):
        if(self.left == None):
            self.left = obj
            obj.parent = self
        else:
            self.left.insert_left(obj)

    def insert_right(self, obj):
        if(self.right == None):
            self.right = obj
            obj.parent = self
        else:
            self.right.insert_right(obj)
                    
    def evaluate(self):
        pass
    
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def set_right(self, obj):
        self.right = obj

    def set_left(self, obj):
        self.left = obj

    def set_parent(self, obj):
        self.parent = obj

    
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
        return self.get_left().evaluate(arg) + self.get_right().evaluate(arg)

class Minus(Node):
    def __init__(self):
        Node.__init__(self)
        
    def evaluate(self, arg):
        return self.get_left().evaluate(arg) - self.get_right().evaluate(arg)

class Multiply(Node):
    def __init__(self):
        Node.__init__(self)
        
    def evaluate(self, arg):
        return self.get_left().evaluate(arg) * self.get_right().evaluate(arg)

class Divide(Node):
    def __init__(self):
        Node.__init__(self)
        
    def evaluate(self, arg):
        return self.get_left().evaluate(arg) / self.get_right().evaluate(arg)

'''    
four = Number(4)
x = Variable()
two = Number(2)
three = Number(3)
multi = Multiply()

tree = Plus()
tree.insert_left(multi)
tree.insert_right(three)
multi.insert_left(two)
multi.insert_right(x)

print tree.evaluate(3)
'''

