from collections import deque

# function to add an edge between vertices x and y
def addEdge(x, y, adj):
    adj[x].append(y)
    adj[y].append(x)

# function to print the parent of each node
def printParents(node, adj, parent):
    # current node is root, thus has no parent
    if parent == 0:
        print("{}->Root".format(node))
    else:
        print("{}->{}".format(node, parent))
    # using DFS
    for cur in adj[node]:
        if cur != parent:
            printParents(cur, adj, node)
        

def printChildren(Root, adj):
    # Queue for the BFS
    q = deque()
    # pushing the root
    q.append(Root)
    # visit arrray to keep track of nodes that have been visited
    vis = [0] * len(adj)

    #BFS
    while q:
        node = q.popleft()
        vis[node] = 1
        print("{}->".format(node))
        for cur in adj[node]:
            if vis[cur] == 0:
                print(cur),
                q.append(cur)
        print()


def printLeafNodes(Root, adj):
    # leaf nodes have only one edge and are not the root\
    for i in range(1, len(adj)):
        if len(adj[i]) == 1 and i != Root:
            print(i),

def printDegrees(Root, adj):
    for i in range(1, len(adj)):
        print(i, ":"),
        # root has no parent thus its degree is equal to the edges it is connected to
        if i == Root:
            print(len(adj[i]))
        else:
            print(len(adj[i]) - 1)