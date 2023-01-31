import re

def stripLike(msg,character=None):
    if not character:
        #remove space from beginning and ending of msg
        msg=re.sub(r"(^\s+)|(\s+$)","",msg)
    else :
        #remove the character provided by the user
        msg=re.sub(character,"",msg)
    return msg    

character=input("enter the char you need to remove or nothing ")  
print(stripLike("   \n       hel \nlo\n","l"),"ghc")
