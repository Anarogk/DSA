class Node:
    def __init__(self, data_):
        self.data  = data_
        self.left  = None
        self.right = None

class BinaryTree:
    def __init__(self, Data) -> None:
        self.Root = Node(Data)
        
    def inorder(self, Root) -> None:
        if Root:
            self.inorder(Root.left)
            print(Root.data, end= " ")
            self.inorder(Root.right)

    def preorder(self, Root) -> None:
        if Root:
            print(Root.data, end=" ")
            self.preorder(Root.left)
            self.preorder(Root.right)

    def postorder(self, Root) -> None:
        if Root:
            self.postorder(Root.left)
            self.postorder(Root.right)
            print(Root.data, end=" ")
            

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

    print("inorder:\n")
    Tree.inorder(root)
    print("\npreorder:\n")
    Tree.preorder(root)
    print("\npostorder:\n")
    Tree.postorder(root)


if __name__ == "__main__":
    main()