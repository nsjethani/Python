class Node:
    def __init__(self,data=0,nextNode=None):
        self.data = data
        self.nextNode = nextNode

class linkedList:
    def __init__(self,head=None):
        self.head = head
        self.size = 0

def hasCycle(head):
    def getlen(end,step=0):
        start = end
        while True:
            step+=1
            start = start.nextNode
            if start is end:
                return step

    slow = fast = head
    while fast and fast.nextNode and fast.nextNode.nextNode:
        slow, fast = slow.nextNode , fast.nextNode.nextNode
        if slow is fast:
            l = getlen(slow)
            b = head
            for _ in range(l):
                b = b.nextNode
            a = head
            while a is not b:
                a = a.nextNode
                b = b.nextNode
                return a
    return None


node1 = Node(1,None)
node2 = Node(2,None)
node3 = Node(3,None)
node4 = Node(4,None)
node5 = Node(5,None)
node6 = Node(6,None)
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node2
list1 = linkedList(node1)
print(hasCycle(list1.head).data)