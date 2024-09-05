# stack is abstract data type.

# operations : push, pop , top, size, isempty

# Recursion stack

# Stack using LL
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Stack:
    def __init__(self, val=0, next=None) -> None:
        self.head = ListNode(val, next)
        self.size = 1

    def push(self, val) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def pop(self) -> int:
        temp = self.head.val
        self.head = self.head.next
        self.size -= 1
        return temp

    def sizeof(self) -> None:
        print("size is :", self.size)
        print()

    def isEmpty(self) -> bool:
        return self.size == 0

    def print_head(self) -> None:
        print("head is :", self.head.val)
        print()

    def print(self) -> None:
        head = self.head
        print("elements in stack are:")
        while head:
            print(head.val, " ")
            head = head.next
        print()


def main():
    head = Stack(1)
    head.push(3)
    head.print_head()
    head.push(4)
    head.push(7)
    head.print_head()

    head.push(9)
    head.print_head()

    head.sizeof()
    head.print()

    head.pop()
    head.pop()
    head.print_head()

    head.sizeof()
    print(head.isEmpty())
    head.pop()
    head.pop()
    head.print_head()

    head.pop()
    print(head.isEmpty())


if __name__ == "__main__":
    main()
