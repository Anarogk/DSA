# for a tree node has 2 data members:
#   1. data
#   2. children array.

from collections import deque

# this is ideally the case
# class Node:
#     def __init__(self, data_) -> None:
#         self.data = data_
#         self.children = []


# function to add an edge between two vertices x and y:
def addEdge(x, y, adj):
    adj[x].append(y) # this is undirected graph so we can add edges in both directions.
    adj[y].append(x)


# function to print the parent of each node:
def printParent(node, adj, parent):
    if parent == 0:
        print('{}->Root'.format(node))
    else:
        print('{}->{}'.format(node, parent))

    # using DFS
    for curr in adj[node]:
        if curr != parent:
            printParent(curr, adj, node)


# function to print all the children:
def printChildren(Root, adj):
    q = deque() # queue for BFS
    q.append(Root) # pushing the root

    # keep track of visited nodes in arr
    visit = [0] * len(adj)
    while q:
        node = q.popleft() # popping left most nodes and then setting them to visited list
        visit[node] = 1
        print("{}->".format(node)),

        for curr in adj[node]:
            if visit[curr] == 0:
                print(curr),
                q.append(curr)
        

            
# Function to print leaf nodes:
def printLeafNodes(Root, adj):
    # leaf nodes have only one edge and are not the root.
    for i in range(1, len(adj)):
        if len(adj[i]) == 1 and i != Root:
            print(i),

# Function to print degree:
def printDegree(Root, adj):
    for i in range(1, len(adj)):
        # if i is root its degree is equal to edges its connected to.
        if i == Root:
            print(f"{i} : {len(adj[i])}")
        # else its degree is edges -1
        else:
            print(f"{i} : {len(adj[i])-1}")

def main():
    N    = 7 # No of nodes
    Root = 1 # root data
    adj  = [[] for _ in range(N+1)] # adj array of N arrays

    addEdge(1, 2, adj) 
    addEdge(1, 3, adj)
    addEdge(1, 4, adj)
    addEdge(2, 5, adj)
    addEdge(2, 6, adj)
    addEdge(2, 7, adj)

    print(f"adjacent array is : {adj}")

    print("the parents of each node are:")
    printParent(Root, adj, 0)

    print("the children of each node are:")
    printChildren(Root, adj)

    print("the leaf Nodes of each node are:")
    printLeafNodes(Root, adj)

    print("the Degrees of each node are:")
    printDegree(Root, adj)





if __name__ == "__main__":
    main()



    