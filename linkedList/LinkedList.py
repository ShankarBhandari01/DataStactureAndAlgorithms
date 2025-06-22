# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# traverse and print the singly linked list
def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next


def search(head, key):
    while head:
        if head.data == key:
            return head
        # move to next node
        head = head.next
    return None


def runSearch(head, key):
    head = search(head, key)
    if head:
        print(f"Found: {head.data}")
    else:
        print("Not Found")


def main():
    # 10->20->30->40->50->None
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = None
    printList(head)
    print()
    runSearch(head, 30)
    print()
    runSearch(head, 100)


if __name__ == "__main__":
    main()
