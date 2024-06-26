def  fizz_buzz(n):
    for i in range(1,n+1):
        if i % 3==0 and i % 5==0:
            print("fizzbuzz")
        elif i % 3==0:
            print("fizz")
        elif i % 5==0:
            print("buzz")

fizz_buzz(15)

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


class Linkedlst:
    def __init__(self):
        self.head=None

    def traverse_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
node=Linkedlst()
node.traverse_ll()
print(node)

