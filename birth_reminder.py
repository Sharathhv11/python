import time as t
class birthday:
    result = False

    def __init__(self):
        self.dictionary = {}

    def upload(self,name,date,month,year):
        self.dictionary[name]=[date,month,year]

    def birth_date(self,user):
        global result
        for x in self.dictionary.keys():
            if user == x:
                finded_result =self.dictionary[x]
                print(f"{finded_result[0]}/{finded_result[1]}/{finded_result[2]}")
                birthday.result = True
        if birthday.result == False:
            print(f"no user with this name{user}")
    def update_birthday(self,user):
        for x in self.dictionary.keys():
            if user == x:
                update_date,update_month,update_year =  input("enter date"),input("enter month"),input("enter year")
                self.dictionary[user]= [update_date,update_month,update_year]
                print(self.dictionary)
print("enter 1 for quit")
while True:
    inp1 = int(input("enter the number>>"))
    if inp1 == 1:
        break
    else:
        a = birthday()
        b = birthday()
        a.upload("sharath___11",11,3,2005)
        a.upload("x_mayur_x",26,2,2005)
        a.upload("vikas_56",6,6,2006)
        inp1 = input("enter>>")
        start = t.time()
        a.birth_date(inp1)
        end = t.time()
        a.update_birthday("sharath___11")
        print("the time taken for searching is ",(end-start))
