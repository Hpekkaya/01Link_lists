class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    # def find_middle_node(self):
    #     if self.head == None:
    #         return None
    #     else:
    #         temp = self.head
    #         mid = temp
    #         while temp != self.tail:
    #             mid = mid.next
    #             temp = temp.next
    #             if temp != self.tail:
    #                 temp = temp.next
    #
    #         return mid

    def find_middle_node(self):
        if self.head == None:
            return None
        else:
            slow = self.head
            fast = slow
            while (fast != None) and (fast.next != None):
                slow = slow.next
                fast = fast.next.next
            return slow


my_linked_list = LinkedList(1)

first, last, inc = 2, 13, 1

for i in range(first, last+1, inc):
    my_linked_list.append(i)

val = my_linked_list.find_middle_node().value

print(f"Middle Value is : {val}")