class Node:
    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self, words):
        self.head = Node("head")
        self.add_via_lists(words)

    def add_via_lists(self, words):
        for word in words:
            self.add(word)

    def add(self, word):
        if not word: return
        cur = self.head
        for char in word.strip():
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.is_word = True

def directions(grid):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0: continue
            yield i, j

def inbound(y, x, grid):
    return 0 <= y < len(grid) and 0<= x < len(grid[0])

def search(i, j, d_i, d_j, grid, trie_head_node, ret):
    node, word_list = trie_head_node, []
    all_d_i, all_d_j = 0, 0
    while inbound(i+all_d_i, j+all_d_j, grid):
        char = grid[i+all_d_i][j+all_d_j]
        if char not in node.children: return
        node = node.children[char]
        word_list.append(char)
        all_d_i, all_d_j = all_d_i+d_i, all_d_j+d_j
        if node.is_word:
            whole_string = ''.join(word_list)
            ret[whole_string] = (i, j)

def word_seek(grid, words):
    trie_head_node = Trie(words).head
    row, col = len(grid), len(grid[0])
    ret = {word.strip(): (-1,-1) for word in words}
    for i in range(row):
        for j in range(col):
            for d_i, d_j in directions(grid):
                search(i, j, d_i, d_j, grid, trie_head_node, ret)
    for k, v in ret.items():
        i, j = v
        print(k, i, j)

def get_input():
    ret = []
    while True:
        try:
            s = input()
            ret.append(s)
        except:
            break
    for i in range(len(ret)):
        if not ret[i]:
            return ret[:i], ret[i+1:]

grid, words = get_input()
word_seek(grid, words)



    