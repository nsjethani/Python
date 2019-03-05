class Node:
    def __init__(self,data=0,nextNode=None):
        self.data = data
        self.nextNode = nextNode

class linkedList:
    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def addNode(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size += 1
        return True

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.nextNode

    def findNode(self,value):
        cur = self.head
        while cur:
            if cur.data == value:
                return True
            cur = cur.nextNode
        return False

    def deleteNode(self,value):
        cur = self.head
        prev = None
        while cur:
            if cur.data == value:
                if prev:
                    prev.nextNode = cur.nextNode
                else:
                    self.head = cur.nextNode
                return True
            prev = cur
            cur = cur.nextNode
        return False

def reverseList(list):
    prev = None
    cur = list.head
    next = cur.nextNode

    while cur:
        cur.nextNode = prev


    list.head = prev
'''
myList = linkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing")
myList.printList()
print("Size")
print(myList.size)
print(myList.findNode(5))
print(myList.findNode(7))
print(myList.deleteNode(5))
myList.printList()
print(myList.deleteNode(7))
myList.printList()
reverseList(myList)
myList.printList()
'''

# Merge two sorted list

def mergeList(L1,L2):
    dummy_head = tail = Node()
    while L1 and L2:
        if L1.data < L2.data:
            tail.nextNode, L1 = L1, L1.nextNode
        else:
            tail.nextNode, L2 = L2, L2.nextNode
        tail = tail.nextNode

    tail.nextNode = L1 or L2
    return dummy_head

def rev_subList(L1,s,f):
    dummy_head = a = Node(0,L1)
    for _ in range(1,s):
        a = a.nextNode
    b = a.nextNode

    for _ in range(f-s):
        c = b.nextNode
        b.nextNode = c.nextNode
        c.nextNode = a.nextNode
        a.nextNode = c
    list1.head = dummy_head.nextNode

list1 = linkedList()
list1.addNode(11)
list1.addNode(9)
list1.addNode(5)
list1.addNode(2)
list1.addNode(1)

list2 = linkedList()
list2.addNode(6)
list2.addNode(4)
list2.addNode(2)

list1.head = mergeList(list1.head,list2.head)
list1.printList()
'''
print("before")
list1.printList()
rev_subList(list1.head,2,4)
print("after")
list1.printList()
'''