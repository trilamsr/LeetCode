import collections

def read_input(nodes):
    cur = 0
    while cur < len(nodes):
        if nodes[cur] == ',':
            yield nodes[cur-1], nodes[cur+1]
        cur += 1

def parent_child(nodes, parent_set, child_set, address):
    error = []
    for parent, child in read_input(nodes):
        if child in address[parent]: error.append('E2')
        if child in child_set: error.append('E3')
        child_set.add(child)
        parent_set.add(parent)
        address[parent].add(child)
        if len(address[parent]) > 2: error.append('E1')
    return error

def expression(address, origin):
    left, right = '', ''
    for child in address[origin]:
        if not left:
            left = expression(address, child)
        else:
            right = expression(address, child)
    return '('+origin+ min((left, right)) + max((left,right)) + ')'
    
def sExpression(nodes):
    parent_set, child_set = set(), set()
    address = collections.defaultdict(set)
    errors = parent_child(nodes, parent_set, child_set, address)
    if errors: return min(errors)
    origin = list(parent_set-child_set)
    if len(origin) == 0: return 'E3'
    if len(origin) > 1: return 'E4'
    return expression(address, origin[0])