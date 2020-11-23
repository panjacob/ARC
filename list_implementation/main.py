from list_implementation.linked_list import LinkedList
from list_implementation.array_list import ArrayList

my_list = LinkedList()
my_list.push(1)
my_list.push(2)
my_list.push(3)
my_list.push(4)
my_list.push(5)
print(my_list.items())
my_list.remove(4)
print(my_list.items())
print(my_list.search(2))
my_list.insert(2, 4)
print(my_list.items())

my_list2 = ArrayList()
my_list2.push(1)
my_list2.push(2)
my_list2.push(3)
my_list2.push(4)
my_list2.push(5)
print(my_list2.items())
my_list2.remove(4)
print(my_list2.items())
print(my_list2.search(2))
my_list2.insert(2, 4)
print(my_list2.items())

my_list.merge(my_list2.items())
print(my_list.items())

my_list2.merge(my_list.items())
print(my_list2.items())
