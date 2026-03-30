class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None


    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
        return cur.val


    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        # Fringe case handling
        # Invalid index checking
        if index >= self.length:
            return False
        # If LinkedList is self.length == 1
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return True
        
        # Main Logic
        cur = self.head
        # Go to node at index - 1
        for i in range(index-1):
            cur = cur.next
        # If the next node is the tail
        if cur.next == self.tail:
            cur.next = None
            self.tail = cur
        else:
            cur.next = cur.next.next
        self.length -= 1
        return True


    def getValues(self) -> List[int]:
        cur = self.head
        value_list = []
        for i in range(self.length):
            value_list.append(cur.val)
            cur = cur.next
        return value_list