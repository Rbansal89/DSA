# class for creating a new node
class node:

    def __init__(self,data):
        self.data = data
        self.next = None

# Class for creating a linked list
class linkedlist:

    def __init__(self):
        self.head = None

    # function to traverse over llist
    def printList(self):
        ptr = self.head

        if ptr is None:
            print("The list is empty")
            return

        while ptr:
            print(ptr.data,"--> ",end="")
            ptr = ptr.next
        print("end",end="")
        print()

    # function to insert a node at front of linked list
    def front_inst(self,data):
        # assigning first node position to temp
        temp = self.head

        # creating a new node and assigning its position to head
        self.head = node(data)
        # Now assigning the prevous first node position to the current first node next ptr
        self.head.next = temp

    def inst_after(self,prev_node,new_data):

        new_node = node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def push(self,new_data):
        # assignng head to the pointer
        ptr = self.head
        # getting ptr to the last node
        if self.head is None:
            self.head = node(new_data)
            return
        while ptr.next:
            ptr = ptr.next

        ptr.next = node(new_data)

    def pop(self):
        ptr = self.head

        if ptr is None:
            print("The list is empty!")
            return -1
        while ptr.next:
            temp = ptr
            ptr = ptr.next
        pop_val = temp.next.data
        temp.next = None
        return pop_val

    def del_node(self,key):

        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev_node = temp
            temp = temp.next

        prev_node.next = temp.next
        temp = None

    def del_ndpos(self,pos):

        ptr = self.head

        if ptr is None:
            print("The lisked list is empty")
            return

        count = 1
        while ptr:
            if count == pos:
                break
            prev_node = ptr
            ptr = ptr.next
            count += 1
        if count > pos:
            print("position is out of range")
        else:
            prev_node.next = ptr.next
        ptr = None

    def del_list(self):
        current = self.head

        while current:
            next = current.next
            del current.data
            current = next
        self.head = None
        print("The list is now empty")

    def length(self):

        ptr = self.head

        if ptr is None:
            #print("The length of the linked list is: ",0)
            return 0

        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        #print("The length of the list is: ",count)
        return count

    def length_rec(self,head):

        if head is None:
            return 0

        return 1 + self.length_rec(head.next)

    # Wrapper function for length_rec
    def len_rec(self):
        return self.length_rec(self.head)

    def find(self,val):
        ptr = self.head

        if ptr is None:
            print("The list is empty!")
            return
        while ptr:
            if val == ptr.data:
                return True
            ptr = ptr.next
        return False

    def find_rec(self,val,head):

        if head is None:
            return False

        if val == head.data:
            return True

        return self.find_rec(val,head.next)

    # use this if u wish to not send the head while calling it
    # wrapper function for find_rec
    #def fn_rec(self,val):
       # return self.find_rec(val,self.head)

    def get_nval(self,n):

        ptr = self.head

        if ptr is None:
            print("The list is empty!")
            return
        count = 0
        while ptr:
            if count == n:
                print(f"The value at the index {n} is {ptr.data}")
                return ptr.data
            ptr = ptr.next
            count += 1

        print(f"Index {n} is out of range")

    def get_nvalrec(self,head,n,llist):
        count = 1
        if head:
            if count == n:
                print(f"The value is {head.data}")
                print(head.data)
            else:
                llist.get_nvalrec(head.next,n-1,llist)
        else:
            print(f"Index is out of range")


    def get_endn(self,n):
        ptr = self.head
        count = 0
        l = self.length()

        if n>=l:
            print("Index out of range!")
            return
        while ptr:
            if count == l-n:
                print(f"The value at index {n} is {ptr.data}")
                return ptr.data
            ptr = ptr.next
            count += 1

    def get_endnrec(self,n):
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        if self.head is not None:
            while count <n:
                if ref_ptr is None:
                    print(f"{n} is greater than the length of list!")
                    return
                ref_ptr = ref_ptr.next
                count += 1
        while ref_ptr is not None:
            #print(main_ptr.data)
            #print(ref_ptr.data)
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next

        return main_ptr.data

    def get_middle(self):

        ptr = self.head

        if ptr is None:
            print("The list is empty!")
            return None
        l = self.length()

        if l == 1:
            return ptr.data

        if l%2 == 0:
            n = l//2
        else:
            n = (l -1)//2

        for i in range(n):
            ptr = ptr.next

        return ptr.data

    def get_middle2(self):
        main_ptr = self.head
        ref_ptr = self.head

        if main_ptr is None:
            print("The list is empty!")
            return None

        while ref_ptr:
            if ref_ptr.next is None:
                break
            temp = ref_ptr.next
            if temp is None:
                main_ptr = main_ptr.next
                return main_ptr.data
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next.next

        return main_ptr.data

    def get_count(self,val):
        ptr = self.head
        count = 0
        # iterate over nodes
        while ptr:
            if ptr.data == val:
                count += 1
            ptr = ptr.next

        return count

    def get_count2(self,head,val,freq=0):

        if head is None:
            return freq

        if head.data == val:
            freq += 1

        return self.get_count2(head.next,val,freq)

    def had_loop(self):
        s = set()
        ptr = self.head
        while ptr:

            if (ptr in s):
                return True
            s.add(ptr)
            ptr = ptr.next
        return False

    def had_loop2(self):
        ptr1 = self.head
        ptr2 = self.head

        while ptr1 and ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr1 == ptr2:
                return True
        return False

    #Function to check if a singly linked list is palindrome
    def ispalindrome(self):

        ptr = self.head
        data_lst = []
        while ptr:
            data_lst.append(ptr.data)
            ptr = ptr.next
        ptr = self.head
        while ptr:
            temp = data_lst.pop()
            if ptr.data != temp:
                return False
            ptr = ptr.next
        return True

    def ispalindrome2(self):



if __name__ == '__main__':

    llist = linkedlist()

    # creating nodes of llist
    llist.head = node(10)
    second = node(20)
    third = node(30)

    # linking the list by giving address of the next
    # node to the next pointer of the current node
    llist.head.next = second
    second.next = third

    # traversing over the linked list
    llist.printList()

    # inserting in the front
    llist.front_inst(5)
    llist.printList()

    # inserting node after a given node
    llist.inst_after(second,89)
    llist.printList()

    #inserting node at the end
    llist.push(899)
    llist.printList()

    #deleting a node with value
    llist.del_node(20)
    llist.printList()


    # deleting a node given its position
    llist.push(6)
    llist.push(7)
    llist.push(8)
    llist.push(9)
    llist.printList()
    llist.del_ndpos(5)
    llist.printList()

    #deleting the list
    llist.del_list()

    #length of the list
    llist.length()
    llist.push(10)
    llist.push(20)
    llist.push(44)
    llist.push(54)
    llist.printList()
    llist.length()

    #length of recurcive
    print("using recursive function")
    print("The length of the lsit is: ",llist.len_rec())

    #find an element in the list iterative func
    print(llist.find(44))
    print(llist.find(89))

    #find an element in the list recursive func
    print("using recursive function")
    print(llist.find_rec(44,llist.head))
    print(llist.find_rec(89,llist.head))

    #get nth index value
    llist.printList()
    x = llist.get_nval(3)
    llist.get_nval(5)
    print(x)

    #with recursive func
    llist.get_nvalrec(llist.head,4,llist)



    #nth node from end of list
    llist.push(89)
    llist.push(100)
    llist.push(120)
    llist.push(150)
    llist.printList()
    llist.get_endn(3)

    # two pointer method used
    print(llist.get_endnrec(3))

    #find middle element
    print("middle elements\n",llist.get_middle(),sep = "")
    llist.pop()
    llist.printList()
    print(llist.get_middle())

    #two pointer method
    print(llist.get_middle2())
    llist.pop()
    llist.printList()
    print(llist.get_middle2())
    llist.pop()
    llist.printList()
    print(llist.get_middle2())

    #couting a value in list
    print(llist.get_count(44))
    llist.push(20)
    llist.front_inst(20)
    llist.front_inst(20)
    llist.printList()
    print(llist.get_count(20))
    print(llist.get_count(200))

    #count using recursion
    print(llist.get_count2(llist.head,20))
    print(llist.get_count2(llist.head,10))

    #detecting loop
    #creating a liked list with loop
    llist2 = linkedlist()
    llist2.push(1)
    llist2.push(2)
    llist2.push(3)
    llist2.push(4)
    llist2.push(5)
    llist2.printList()
    llist2.head.next.next.next.next.next = llist2.head

    print(llist2.had_loop())
    print(llist.had_loop())

    #method 2 Floyd's cycle finding algorithm
    print("Using floyd's cycle algorithm")
    print(llist2.had_loop2())
    print(llist.had_loop2())

    #check if the linked list is palindrome
    print("")
    llist3 = linkedlist()
    llist3.push('R')
    llist3.push('A')
    llist3.push('R')
    llist3.printList()
    print(llist3.ispalindrome())
    llist.printList()
    print(llist.ispalindrome())

    #check palindrome maethod 2
