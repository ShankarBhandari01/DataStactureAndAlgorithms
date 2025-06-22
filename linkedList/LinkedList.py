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


# length of the linked list
def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def search(head, key):
    while head:
        if head.data == key:
            return head
        # move to next node
        head = head.next
    return None

# delete a node from the linked list
def delete(head, key):
    checkHead(head)
    if head.data == key:
        head = head.next
        return head
    else:
        current = head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                break
            # update current
            current = current.next
        return head


def checkHead(head):
    if head is None:
        raise ValueError("List is empty")


# insert a new node at the beginning
def insert(head, key):
    checkHead(head)
    new_node = Node(key)
    new_node.next = head
    head = new_node
    return head


def insertAt(head, key, index):
    if index == 0:
        return insert(head, key)
    else:
        current = head
        for i in range(index - 1):
            if current.next is None:
                raise ValueError("Index out of range")
            current = current.next
        # Create new node
        new_node = Node(key)
        # Make next of new Node as next of current
        new_node.next = current.next
        # Make current next as new_node
        current.next = new_node
        return head


# insert a new node at the end
def insertAtEnd(head, key):
    checkHead(head)
    new_node = Node(key)

    current = head
    while current.next:
        current = current.next
    current.next = new_node

    return head

def pop(head,index):
    checkHead(head)
    for i in range(index-1):
        if head.next is None:
            raise ValueError("Index out of range")
        head = head.next
    if head.next is None:
        raise ValueError("Index out of range")
    else:
        temp = head.next # set the value
        head.next = head.next.next # update the next
        return temp # return the value

def get(head,index):
    checkHead(head)
    for i in range(index-1):
        if head.next is None:
            raise ValueError("Index out of range")
        head = head.next
    return head.data


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
    print()

    print("70 at the index 2")
    head = insertAt(head, 70, 2)
    printList(head)

    print()
    print("Length of the linked list: ", length(head))

   # print()
   # print("delete 30")
   # head = delete(head, 30)
    #printList(head)

    print()
    print("get at 2")
    print(get(head,2))

if __name__ == "__main__":
    main()
