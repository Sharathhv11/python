def board(array):
    """this module presents 3x3 tic tac toe
    board on console 
      this function accepts array as input """
    try:
         print("-"*13)
         for x in range(3):
            a,b,c=array[x]
            print("| {} | {} | {} |".format(a,b,c))
            print("-" * 13)
    except :
        print("Error")

if __name__=="__main__":
    board([[' ',' ','x'],['o','x','o'],[' ',' ',' ']])
