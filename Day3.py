class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    l = list(gen(node))
    s = ','.join(l)
    return(s)

def deserialize(s):
    l = s.split(',')
    root = place(iter(l), None, True)
    print(root.left)
    return root

def place(l, cur, left):
    v = next(l, None)           #Default value ensures no exception.
    if v == 'n' or v == None:
        return
    if not cur:
        cur = Node(v)
    elif left:
        cur.left = Node(v)          #This would be so much easier if python let me pass by reference properly
        cur = cur.left
    else:
        cur.right = Node(v)
        cur = cur.right
    place(l, cur, True)
    place(l, cur, False)
    return cur
    
def inorder(node):
    yield from inorder(node.left) if node.left else ()
    yield node.val
    yield from inorder(node.right) if node.right else ()

def gen(node):
    yield node.val
    yield from gen(node.left) if node.left else 'n'
    yield from gen(node.right) if node.right else 'n'


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
