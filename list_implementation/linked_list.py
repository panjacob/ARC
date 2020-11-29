from list_implementation.my_list import MyList
from list_implementation.singleton import singleton


@singleton
class MyNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(MyList):
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = MyNode(value)
        self.length += 1
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, value):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.value == value:
                if prev_node is not None:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
                current_node = None
                self.length -= 1
                break
            prev_node = current_node
            current_node = current_node.next

    def insert(self, index, value):
        if index >= self.length:
            return
        self.length += 1
        current_node = self.head
        prev_node = None
        new_node = MyNode(value)
        i = 0

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.length - 1:
            self.tail.next = new_node
            self.tail = new_node
        else:
            while current_node is not None:
                if i == index:
                    prev_node.next = new_node
                    new_node.next = current_node
                    break
                prev_node = current_node
                current_node = current_node.next
                i += 1

    def search(self, value):
        current_node = self.head
        i = 0

        while current_node is not None:
            if current_node.value == value:
                return i
            current_node = current_node.next
            i += 1

        return -1

    def merge(self, new_list):
        for i in new_list:
            self.push(i)

    def items(self):
        current_node = self.head
        result = []

        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next

        return result

    def even(self):
        current_node = self.head
        result = []

        while current_node is not None:
            if current_node.value % 2 == 0:
                result.append(current_node.value)
            current_node = current_node.next

        return result

    def odd(self):
        current_node = self.head
        result = []

        while current_node is not None:
            if current_node.value % 2 == 1:
                result.append(current_node.value)
            current_node = current_node.next

        return result
