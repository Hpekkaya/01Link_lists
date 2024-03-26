class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_link_list = LinkList(4)

print(f"Head   : {my_link_list.head.value}")
print(f"Tail   : {my_link_list.tail.value}")
print(f"Length : {my_link_list.length}")
