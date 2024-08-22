
## Importance for Tree Data Structure:
1. One reason to use trees might be because you want to `store information that naturally forms a hierarchy`. For example, the file system on a computer like file system.
2. Trees (with some ordering e.g., BST) provide `moderate access/search (quicker than Linked List and slower than arrays)`. 
3. Trees provide moderate `insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists)`. 
4. Like Linked Lists and unlike Arrays, Trees `don’t have an upper limit on the number of nodes as nodes are linked using pointers`.





## Properties of Tree Data Structure:
- Number of edges: An edge can be defined as the connection between two nodes. If a tree has N nodes then it will have `(N-1)` edges. There is only one path from each node to any other node of the tree.
- Depth of a node: The depth of a node is defined as the `length of the path from the root to that node`. Each edge adds 1 unit of length to the path. So, it can also be defined as the number of edges in the path from the root of the tree to the node.
- Height of a node: The height of a node can be defined as the `length of the longest path from the node to a leaf node of the tree`.
- Height of the Tree: The height of a tree is the `length of the longest path from the root of the tree to a leaf node of the tree`.
- Degree of a Node: The `total count of subtrees attached to that node` is called the degree of the node. The degree of a leaf node must be 0. `The degree of a tree is the maximum degree of a node among all the nodes in the tree`.


## Advantages of Tree Data Structure:
- Tree offer Efficient Searching Depending on the type of tree, with `average search times of O(log n) for balanced trees like AVL`. 
- Trees provide a hierarchical representation of data, making it easy to organize and navigate large amounts of information.
- The recursive nature of trees makes them `easy to traverse and manipulate` using recursive algorithms.
