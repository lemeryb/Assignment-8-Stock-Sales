from LinkedList import LinkedList

# Title: Stacks
# Date: 3/9/20
# Author: Benjamin Lemery
# This program demonstrates how to create and manipulate a stack FIFO

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push (self,data):
        self.list.insert_at_start(data)

    def pop(self,data):
        return self.list.delete_at_start()

    def display(self):
        self.list.traverse_list()





myStack = Stack()

myStack.push(20)
myStack.pop(20)
myStack.display()