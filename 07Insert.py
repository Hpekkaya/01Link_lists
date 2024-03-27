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

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def get(self, inds):
        temp = self.head
        if inds < 0 or inds >= self.length:
            return None
        for i in range(inds):
            temp = temp.next
        return temp

    def set(self, inds, value):
        temp = self.get(inds)
        if temp:
            temp.value = value
            print(f"After the Set Index of {inds}  New ")
            return True
        print("Indis out of range")
        return False

    def insert(self, inds, value):
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        if inds < 0 or inds > self.length:
            return False
        elif inds == 0:
            self.prepend(value)
        elif inds == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(inds-1)
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        return True


print("\n")
my_LL = LinkList(1)
my_LL.make_empty()

# first, last, inc = 1, 5, 1
#
# for i in range(first, last+1, inc):
#     my_LL.append(i**2)

my_LL.print_list()
print("\n")

inds = 0
ins_value = 125

val = my_LL.insert(inds, ins_value)

print(f"After the Insertion of ({inds},{ins_value} )  New ")
my_LL.print_list()

print("\n")

