class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insertbeg(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def insertpos(self,data,key):
        newnode = node(data)
        lastnode = self.head
        if self.head==None:
            print("list is empty")
        else:
            while lastnode.next != None:
                if lastnode.data==key:
                   break
                lastnode = lastnode.next
            newnode.next=lastnode.next
            lastnode.next=newnode
    def insertend(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
    def printlist(self):
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
singlylinkedlist=SLL()
while True:
    print("1.insert at beginnig \n2.insert at position \n3.insert at end \n4.display list")
    ch=int(input("enter your choice:"))
    if ch==1:
        data=input("enter the element to insert:")
        singlylinkedlist.insertbeg(data)
    elif ch==2:
        data=input("enter the element to insert:")
        key=input("enter the element after insertion:")
        singlylinkedlist.insertpos(data,key)
    elif ch==3:
        data=input("enter the element to insert:")
        singlylinkedlist.insertend(data)
    elif ch==4:
        singlylinkedlist.printlist()
    else:
        print("invalid input")









