# https://www.acmicpc.net/problem/1991

preorder = []
inorder = []
postorder = []

class node:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right
        
def travel(now:node):
    if not now: return
    
    preorder.append(now.node)
    travel(now.left)
    inorder.append(now.node)
    travel(now.right)
    postorder.append(now.node)

n = int(input())
nodes = [node(c,None, None) for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] + [None]
trie = {c : node for (c,node) in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ.', nodes)}

for i in range(n):
    now, left, right = input().split()
    node = trie[now]
    left = trie[left]
    right = trie[right]
    
    node.left = left
    node.right = right

travel(trie['A'])

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))