# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
#
# class LinkedList:
#     def __init__(self, value):
#         new_node=Node(value)
#         self.head=new_node
#         self.tail=new_node
#         self.length=1
#
# my_linked_list=LinkedList(4)
# print(my_linked_list.head.value)
#
# #print the list
# def print_list(self):
#     temp=self.head
#     while temp is not None:
#         print(temp.value)
#         temp=temp.next
#
#
# #append to list
# #
# # def append_list(self,value):
# #     new_node=Node(value)
# #     if self.head is None:
# #         self.head=new_node
# #         self.tail=new_node
# #     else:
# #         self.tail.next=new_node
# #         self.tail=new_node
# #     self.length+=1
# #     return True
# #
# # my_linked_list.append_list(2)
#
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def pop(self):
#         if self.head is None:
#             print("Linked list is empty. Cannot pop.")
#             return None
#         popped_data = self.head.data
#         self.head = self.head.next
#         return popped_data
#
#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=" -> ")
#             current_node = current_node.next
#         print("None")
#
# # Example usage:
# my_linked_list = LinkedList()
# my_linked_list.push(3)
# my_linked_list.push(2)
# my_linked_list.push(1)
#
# print("Original linked list:")
# my_linked_list.print_list()
#
# popped_element = my_linked_list.pop()
# if popped_element is not None:
#     print("Popped element:", popped_element)
#
# print("Updated linked list:")
# my_linked_list.print_list()

#
#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
#
# class Linked_ll:
#     def __init__(self):
#         self.head=None
#
#     def print_ll(self):
#         if self.head is None:
#             print("linked list empty")
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data)
#                 n=n.ref
#
#
#
#
#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
#
# class Linked_LL:
#     def __init__(self):
#         self.head=None
#
#     def print_ll(self):
#         if self.head is None:
#             print("node is empty")
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data)
#                 n=n.ref

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
#
# class Linked_ll:
#     def __init__(self):
#         self.head=None
#
#     def traverse_data(self):
#         if self.head is None:
#             print("empty list")
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data)
#                 n=n.ref
#
#     def add_begin(self, data):
#         new_node=Node(data)
#         new_node.ref=self.head
#         self.head=new_node
#
# ll1=Linked_ll()
# ll1.traverse_data()
# ll1.add_begin(10)

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def delete_begin(self):
        if self.head is None:
            print("empty list")
        else:
            self.head=self.head.ref

ll1=LinkedList()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)

# ll1.delete_begin()

ll1.print_LL()