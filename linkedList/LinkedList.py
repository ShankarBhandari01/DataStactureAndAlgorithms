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


# insert a new node at the beginning
def insert(head,key):
    new_node = Node(key)
    new_node.next=head
    head=new_node
    return head

# insert a new node at the end
def insertAtEnd(head,key):
    if head is None:
        raise ValueError("List is empty")
    new_node = Node(key)

    current = head
    while current.next:
        current = current.next
    current.next = new_node

    return head

def runSearch(head, key):
    head = search(head, key)
    if head:
        print(f"Found: {head.data}")
    else:
        print("Not Found")


def main():
    # 10->20->30->40->50->None

    arr = [10, 20, 30, 40, 50]
    head = None
    for a in arr:
        # if head is not exist
        if head is None:
            head = Node(a)
        else:
            # if head is exist get the last node
            last = head
            while last.next:
                last = last.next
            last.next = Node(a)


    print("Before insertion: ")
    printList(head)
    print()
    # insert a new node at the beginning
    head = insert(head, 100)
    # check if the new node is inserted correctly
    print("After insertion of 100 at the beginning: ")
    printList(head)
    print()
    head = insertAtEnd(head, 60)
    print("After insertion  of 60 at the end: ")
    printList(head)


if __name__ == "__main__":
    main()
