import os 
import json

class folderArranger:
    def __init__(self, _path):
        self.folder_path = _path
        self.json_path = "d:/python/folder arrengment/folder_names.json"
        os.chdir(self.folder_path)
        self.entities=os.listdir()
        self.files_inpath=[x for x in self.entities if os.path.isfile(x)]
        self.folders_inpath=[x for x in self.entities if os.path.isdir(x)]

    def arrangeFiles(self) -> None:
        """this method of folderArrenge class arrange the files in
        specified directory and stores file format name in its json object for further use"""
        try :
            #loading json data to a variable 
            with open(self.json_path,"r",encoding="utf-8") as initial:
                json_data = json.load(initial)
        except FileNotFoundError:
                print(f"file not found please replace {self.json_path} to  your local absolute url of json object ")
                return 
        except Exception as e:
            print(e)
            return
        json_update=False
        

        for file in self.files_inpath:
            file_format=file.split(".")[-1]
            current_file = json_data.get(file_format)
            if(not current_file):
                """if the formates doesnt exists in json it will input and store it ints json"""
                while(True):
                    new_file_format = input(f"i dont have this -> {file_format} <- in my json so please provide name for this format :").strip()
                    if(new_file_format):
                        json_update=True
                        json_data.update({file_format:new_file_format})
                        current_file=new_file_format
                        break
                    else:
                        print("you have entered a empty string so please reenter the name ")
            
            #folder creation is the folder dosent exists 
            folder_vaildidation = os.path.join(os.getcwd(),current_file)
            if(not os.path.exists(folder_vaildidation)):
                os.mkdir(current_file)

            # moving file from source path to destination folder 
            source_path = os.path.join(os.getcwd(),file)
            destination_path = os.path.join(os.getcwd(),current_file,file)
            try:
                if(not os.path.exists(destination_path) and os.path.exists(source_path)):
                    os.rename(source_path,destination_path)
            except FileNotFoundError:
                print("path doesnt found")

            #updating json for further use 
            if(json_update):
                with open(self.json_path,"w",encoding="utf-8") as outcome:
                    json.dump(json_data,outcome,indent=4)

    def display_files(self):
        print(self.files_inpath,self.folders_inpath,sep="\n")
        
def main():
    folder_path=input("Enter the folder path that you want to arrenge : ")
    obj1=folderArranger(folder_path)
    while(True):
        options=int(input("1-arrenge files | 2-display folders and files : "))
        match (options):
            case 1:
                obj1.arrangeFiles()
                break
            case 2:
                obj1.display_files()
                break
            case _ :
                print("please enter valid option ")
if(__name__=="__main__"):
    main()