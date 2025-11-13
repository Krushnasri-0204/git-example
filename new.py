class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node

def insert_at_end(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

def delete_node(head, key):
    temp = head
    if temp and temp.data == key:
        return temp.next
    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next
    if temp:
        prev.next = temp.next
    return head

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

head = None
head = insert_at_beginning(head, 10)
head = insert_at_beginning(head, 20)
head = insert_at_end(head, 30)
head = insert_at_end(head, 40)
display(head)
head = delete_node(head, 20)
display(head)