import re

def isStrongPassword(passw):
    allre=re.search(r"((.*\d+.*)|(\w{8}))",passw)
    print(allre)
    if(allre.group(1) and allre.group(2)):
        print("nice strong password")
    else:
        print("your password isn't strong enough")
        print("validate it has at least 8 character long \nand has at least one  lowercase character and one uppercase character and one digit")
    

    
passw=input("enter your password")   
isStrongPassword(passw)
