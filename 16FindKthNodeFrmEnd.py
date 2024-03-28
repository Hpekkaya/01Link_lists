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

    # def find_kth_from_end(self, k):
    #     # 0 check the list is not empty
    #     if self.head == None:
    #         return None
    #     # 1. Initaize the pointers (slow and fast)
    #     slow = self.head
    #     fast = self.head
    #     # 2. Generate a loop for the fast kth end how many steps ahead of slow
    #     for _ in range(k-1):
    #         fast = fast.next
    #
    #     # 3. Generate a loop to iterate over the LL
    #     while fast.next != None:
    #         slow = slow.next
    #         fast = fast.next
    #
    #     # 4. When the fast loop complete the list return the slow
    #     return slow

def find_kth_from_end(LinkL, k):
    LL = LinkL
    # 0 check the list is not empty
    if LL.head is None:
        return None
    # 1. Initaize the pointers (slow and fast)
    slow = fast = LL.head

    # 2. Generate a loop for the fast kth end how many steps ahead of slow
    for _ in range(k-1):
        fast = fast.next
        if fast is None:
            return None


        # 3. Generate a loop to iterate over the LL
    while fast.next != None:
        slow = slow.next
        fast = fast.next

    # 4. When the fast loop complete the list return the slow
    return slow


my_linked_list = LinkedList(1)

first, last, inc = 2, 8, 1

for i in range(first, last+1, inc):
    my_linked_list.append(i)

k = 9
# result = my_linked_list.find_kth_from_end(k)
result = find_kth_from_end(my_linked_list, k)

if result is None:
    print(f"{k} is more then length")
else:
    print(result.value)  # Output: 4