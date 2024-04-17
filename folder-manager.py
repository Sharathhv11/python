import os 

def arrengeFiles(folder_path)->int:
    try:
        os.chdir(folder_path)
        entities=os.listdir()
        files_inpath=[x for x in entities if os.path.isfile(x)]
        folders_inpath=[x for x in entities if os.path.isdir(x)]
        for file in files_inpath:
            file_format=file.split(".")[-1]
            if(file_format not in folders_inpath):
               
               os.mkdir(file_format)
               folders_inpath.append(file_format)

            target_path = os.path.join(file_format, file)
            if(not os.path.exists(target_path)):
                os.rename(file,target_path)
    except Exception as e :
        print(e)
        
def main():
    folder_path=input("Enter the folder path that you want to arrenge : ")
    result = arrengeFiles(folder_path)
if(__name__=="__main__"):
    main()