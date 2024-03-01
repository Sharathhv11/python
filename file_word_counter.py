import threading as t 
word_counter={}
count = 5

file_content = []
def read_file(file_name):
    """this function excetract the content from yhe give file
    and store it in file  content veriable"""
    global file_content,count
    
    try:
        with open(file_name) as file:
            file_content = file.readlines()
    except FileNotFoundError as error:
        count-=1
        if (count>=1):
            print(f"this file {file_name} doesn't exists in this computer \nyou have {count} more chances")
            main()
        else:
            print("maximum attempts try later")

        
def counter(argu1,argu2):
    """this function find the frequency of each words 
    and store it in hash map format """
    global word_counter,file_content
    
    list1=[]
    
    for x in file_content[argu1:argu2]:
        operationA=x.split()
        
       
        for y in operationA:
            final_string=y.strip("'s").replace(".", "").replace(",", "")
            list1.append(final_string)
    
    for x in list1:
        word_counter[x]=word_counter.get(x,0)+1

def main():
        
    file_path = input("file name with path:")      
    read_file(file_path)

    argumemnts = (0+len(file_content))//2

    thread1=t.Thread(target=counter,args=(0,argumemnts))
    thread2=t.Thread(target=counter,args=(argumemnts,len(file_content)))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if (__name__=="__main__"):
    main()
    
