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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.length -= 1
        self.tail = pre
        self.tail.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True



print("\n")
my_LL = LinkList(1)
my_LL.make_empty()

first, last, inc = 1, 15, 2

for i in range(first, last+1, inc):
    my_LL.append(i)

my_LL.print_list()
print("\n")

val = "Ahmet"
my_LL.prepend(val)
print(f"Prepend : {val}")
print("After Prepend ", end=" ")
my_LL.print_list()
print("\n")

