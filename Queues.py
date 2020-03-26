from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def push (self,data):
        self.list.insert_at_end(data)

    def pop(self,data):
        return self.list.delete_at_start()

    def display(self):
        self.list.traverse_list()


