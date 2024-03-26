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

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0


    def print_list(self):
        temp = self.head
        if temp is None:
            print("There is no Link List")
            return None
        print("Link List Values :")
        while temp:
            print(f"{temp.value}", end=" ")
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1




my_LL = LinkList(1)
my_LL.make_empty()

first, last, inc = 1, 15, 2

for i in range(first, last+1, inc):
    my_LL.append(i)

my_LL.print_list()


