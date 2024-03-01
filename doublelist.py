def sort_decorator(func):
    def wrapper(self):
        print("The data will be sorted and will not be in the normal form.")
        choice = input("Do you want to continue? (1: Continue, 2: Break) ")
        
        if choice == "1":
            func(self)  # Call the original sort() method
        elif choice == "2":
            print("Sorting process aborted.")
        else:
            print("Invalid choice. Sorting process aborted.")
    return wrapper

class node:
    def __init__(self,data) -> None:
        self.prev= None
        self.data=data
        self.next=None
class linkdouble:
    def __init__(self) -> None:
        self.head = None
        self.total=0
    
    def insert_b(self,data):
        new = node(data)
        self.total +=1 
        if self.head is None:
            self.head = new  
        else:
            cu = self.head
            while cu.next:
                cu=cu.next
            cu.next=new
            new.prev=cu
    def insert_e(self,data):
        new = node(data)
        self.total+=1
        if self.head is None:
            self.head =new
        else:
            cu = self.head
            while cu.next:
                cu=cu.next
            cu.next=new
            new.prev = cu
    def display(self):
        if self.head is None:
            raise ValueError("list is empty")
            return 
        current=self.head
        while(current):
            print(current.data,end=" ")
            current=current.next
        print()
    def address(self):
        current= self.head
        print("address stored in head \n{}".format(self.head))
        print("address stored in next")
        while current:
            print(current.next,end=" ")
            current=current.next
        current=self.head
        print()
        print("address stored in prev ")
        while current:
            print(current.prev,end=" ")
            current=current.next
        print()
    def search(self,data):
        if self.head is None:
            raise ValueError("list is empty")
        else:
            current= self.head
            while current:
                if (current.data==data):
                    print("data exists")
                    break
                current=current.next
            else:
                print("data not exists")
    def delete_b(self):
        if self.head is None:
            raise ValueError("list is empty")
            return
        self.total-=1
        self.head=self.head.next
        self.head.prev =None 
    def delete_e(self):
        if self.head is None:
            raise ValueError("list is empty")
        elif self.head.next is None:
            self.total-=1
            self.head =None
        else:
            current=self.head
            self.total-=1
            while current.next :
                current=current.next
            current=current.prev
            current.next.prev=None
            current.next=None
    def insert_inbetween(self,data):
        new = node(data)
        self.total+=1
        if self.head is None:
            self.head = new
            return
        inp = input("after which data >>")
        if self.head is not None:
            current=self.head
            while current.next is not None:
                current=current.next
            if current.data==inp:
                current.next=new
                new.prev=current
                return
        
        current= self.head
        next_node=None
        while current:
            if current.data==inp:
                
                next_node=current.next
                current.next=new
                new.next=next_node
                next_node.prev = new
                new.prev = current
                break
            current=current.next
    def display_reverse(self):
        if self.head is None:
            raise ValueError("list is empty")
            return
        current=self.head
        while current.next is not None:
            current=current.next
        while current is not None:
            print(current.data,end=" ")
            current=current.prev
        print()
    #sorting the linklist
    #@sort_decorator
    def sort(self):
        print(self.total)
        for x in range(self.total):
            current = self.head
            while current.next:
                if current.data>current.next.data:
                    current.data,current.next.data=current.next.data,current.data
                current=current.next
            current=self.head
        self.display()
    def totalNodes(self):
        print("total node:"+str(self.total))
def value() ->str:
    inp=input("enter data:")
    return inp

if __name__=="__main__":
    link =linkdouble()
    try:
        while True:
            inp=int(input("enter 1-insert_b 2-end 3-address 4-search 5-delete_b 6-delete_e 7-display 8-insert_inbetween 9-display_reversse 11-node count  10-sort>>>"))
            match inp:
                case 1:
                    link.insert_b(value())
                    link.display()
                case 2:
                    link.insert_e(value())
                    link.display()
                case 3:
                    link.address()
                case 4:
                    link.search(value())
                case 5:
                    link.delete_b()
                    link.display()
                case 6:
                    link.delete_e()
                case 7:
                    link.display()
                case 8:
                    link.insert_inbetween(value())
                    link.display()
                case 9:
                    link.display_reverse()
                case 10:
                    link.sort()
                case 11:
                    link.totalNodes()
                case _:
                    raise ValueError(f"{inp } unnvalid option!!")
    except ValueError as e:
        print("ERROR : "+str(e))
list = [90,67,45,23,12]
print(sorted(list))