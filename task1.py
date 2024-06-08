#Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком. Реалізація однозв'язного списку

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def sorted_merge(self, other):
        dummy = Node(0)
        tail = dummy
        a = self.head
        b = other.head
        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        if a:
            tail.next = a
        else:
            tail.next = b
        self.head = dummy.next

    def insertion_sort(self):
        sorted_list = None
        curr = self.head
        while curr:
            next_node = curr.next
            if not sorted_list or sorted_list.data >= curr.data:
                curr.next = sorted_list
                sorted_list = curr
            else:
                temp = sorted_list
                while temp.next and temp.next.data < curr.data:
                    temp = temp.next
                curr.next = temp.next
                temp.next = curr
            curr = next_node
        self.head = sorted_list
# Створення однозв'язного списку
llist = LinkedList()
llist.append(3)
llist.append(1)
llist.append(2)
llist.append(5)
llist.append(4)

print("Початковий список:")
llist.print_list()

# Реверсування списку
llist.reverse()
print("Реверсований список:")
llist.print_list()

# Сортування списку
llist.insertion_sort()
print("Відсортований список:")
llist.print_list()

# Об'єднання двох відсортованих списків
llist2 = LinkedList()
llist2.append(6)
llist2.append(7)

llist.sorted_merge(llist2)
print("Об'єднаний відсортований список:")
llist.print_list()