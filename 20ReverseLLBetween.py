class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    # def reverse_between(self, first, second):
    #     if not self.head:
    #         return None
    #
    #     current = self.head
    #     i = 0
    #     while current:
    #         if i == first:
    #             temp1 = current.value
    #             before = current
    #
    #         if i == second:
    #             temp2 = current.value
    #             current.value = temp1
    #             before.value = temp2
    #
    #
    #         i += 1
    #         current = current.next

    def reverse_between(self, start, end):
        if not self.head:
            return None

        temp = Node(0)
        temp.next = self.head

        previous = temp

        for i in range(start):
            previous = previous.next

        current = previous.next

        for i in range(end-start):
            to_move = current.next
            current.next = to_move.next
            to_move.next = previous.next
            previous.next = to_move

        self.head = temp.next




linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


