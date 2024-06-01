class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SingleList:
    def __init__(self):
        self.head = None

    def displayList(self):
        if self.head is None:
            print("empty List")
        else:
            temp = self.head
            while temp:
                print(temp.data,end="--->>>>")
                temp = temp.next


linkedList = SingleList()
node1 = Node(12)
linkedList.head = node1
node2 = Node(23)
node1.next = node2
linkedList.displayList()