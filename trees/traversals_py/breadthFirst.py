

class Node: 
    def __init__(self, data_) -> None:
        self.data = data_
        self.left  = None
        self.right = None


class BinaryTree:
    def __init__(self, Root) -> None:
        self.Root = Node(Root)
        self.Root.data = Root

    def level_order(self, Root) -> None:
        if Root is None:
            return
        q = []
        q.append(Root)

        while len(q)>0:
            print(q[0].data, end=" ")
            node = q.pop(0)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


def main():
    Tree = BinaryTree(0)
    root = Tree.Root
    # print(Tree.Root.data)
    Tree.Root.left = Node(1)
    Tree.Root.left.left = Node(2)
    Tree.Root.left.right = Node(4)
    Tree.Root.left.left.left = Node(3)
    Tree.Root.right = Node(5)
    Tree.Root.right.left = Node(6)
    Tree.Root.right.right = Node(7)
    Tree.Root.right.right.right = Node(8)

    Tree.level_order(root)



if __name__ == "__main__":
    main()

    