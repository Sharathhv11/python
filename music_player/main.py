from music_player import *

class Node:
    """defining the node structure that contains pointers and data feilds"""
    def __init__(self,path,name):
        self.pointer1= None
        self.pointer2=None
        self.path = path
        self.name=name
        
class DoubleLinklist:
    def __init__(self) -> None:
        self.head = None
        # self.tail=None

    def insert_end(self, path, name):
        node1 = Node(path, name)
        if self.head is None:
            self.head = node1
            
        else:
            current = self.head
            while (current.pointer2):
                current=current.pointer2
            current.pointer2=node1
            node1.pointer1=current
        # print(node1.pointer2,node1.pointer1,self.head,sep="\n")
    
    def insert_begining(self,path,name):
        node1 = Node(path, name)
        if self.head is None:
            self.head = node1
        else:
            self.head.pointer1=node1
            node1.pointer2=self.head
            self.head=node1
    def display(self):
        if self.head is None:
            print("no music is added")
        else :
            current = self.head
            while current:
                print(current.name)
                current=current.pointer2
    def search(self,find : str):
        if self.head is None:
            print("no music is added")
        else :
            current = self.head
            while current:
                if(current.name.lower() == find.lower()):
                    return current.path,current.name
                else:
                    current=current.pointer2

    def music_play(self,name):
        a=self.search(name)[0]
        print(a)
        music_obj = music(a)
        music_manage = music_manager(music_obj)
        while(True):
            inp = int(input("enter 1-play , 2 - pause , 3 - stop , 4 - unpause :5-next music 6-previous music "))
            if(inp>0 and inp<=4):
                music_manage.music_status(inp)
            elif(inp>4 and inp<=6):
                pass
        



def value_input():
    inp1 = input("Enter song path :")
    inp2 = input("enter alias name for song :")
    return inp1,inp2
def main():
    obj = DoubleLinklist()
    
    while (True):
        inp = int(input("1 - begin 2- end 3-display 4-play_music  5-search_music : "))
        match(inp):
            case 1:
                obj.insert_begining(*value_input())
            case 2:
                obj.insert_end(*value_input())
            case 3:
                obj.display()
            case 4:
                obj.music_play(input("play song name :"))
            case 5:
                print(obj.search(input("Find : ")))
            case _:
                print("you have entered a wrong choice!")
        
    


if __name__=="__main__":
    main()