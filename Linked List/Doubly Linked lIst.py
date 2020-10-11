class Node:

    def __init__(self,data,next = None,prev = None):
        self.prev = prev
        self.data = data
        self.next = next

class dlinkedlist:

    def __init__(self):
        self.head = None

    def printlist(self):
        ptr = self.head

        if ptr is None:
            print("The list is empty!")
            return
        while ptr:
            print(ptr.data,end='--->')
            ptr = ptr.next
        print("end")
        return

    def insertatbeg(self,data):

        ptr = self.head

        if ptr is None:
            self.head = Node(data)
            return

        new_Node = Node(data)
        new_Node.next = ptr
        new_Node.next.prev = new_Node
        self.head = new_Node
        return
    

if __name__ == '__main__':

    dlist = dlinkedlist()
    dlist.printlist()
    dlist.insertatbeg(10)
    dlist.insertatbeg(20)

    dlist.printlist()