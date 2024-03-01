#reversing string using punctuation
def string_reversing(argu:str) -> str:
    """this function takes string as an argument
    and reverse the given string based on punctuations"""
    l = argu.split()
    new_string=""
    previous=0 
    for x in l:
        #finding words that ends with panctuation
        if (x.endswith(("!",".",",")) ): #x.endswith('!','.')
            new_string+=" ".join(l[previous:(l.index(x)+1)][::-1])+" "
            previous=l.index(x)+1
    if previous < len(l):
        new_string+=" ".join(l[previous:][::-1])+" "
   
    return  new_string.strip()
          
            
print(string_reversing("hello world! this is python. and this,"))
#input : "hello world! this is python. and this"

#output : "world! hello python. is this this and"