class Node:
    def __init__(self, val=None, *children):
        self.val = val
        self.children = list(children)

visited = set()

def dfs(x, T):
    print("Looking at", T.val, " Children: ", [ i.val for i in T.children ])
    if T.val == x:
        return True
    for i in T.children:
        if dfs(x, i) is True:
            return True
        else: continue
    return False

if __name__ == "__main__":
    d = Node("d")
    f = Node("f", d)
    e = Node("e", f, d)
    c = Node("c", d)
    b = Node("b", f, c)
    d.children.append(b)
    a = Node("a", f, d, b)
    print(dfs("b", a))
