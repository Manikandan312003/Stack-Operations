class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value=0):
        self.top = None
        self.height = 0

    def push(self,value):
        if self.top==None:
            self.top=Node(value)
            return True
        newNode=Node(value)
        newNode.next=self.top
        self.top=newNode
        self.height+=1
        return True

    def pop(self):
        if self.top==None:
            return None
        temp=self.top
        self.top=self.top.next
        self.height-=1
        temp.next=None
        return temp

def main():
    books=Stack()
    while 1:
        n=int(input("1.Push into Stack\n2.Pop from Stack.\n3.Exit....\n"))
        if n==1:
            books.push(int(input()))
        if n==2:
            poppedValue=books.pop()
            print("Popped Value is "+str(poppedValue.value) if poppedValue else "Nothing in Stack")
        if n==3:
            print("------------Exiting------------")
            return 0

if __name__=='__main__':
    main()
