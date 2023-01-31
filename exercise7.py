
import re

def isPhoneNumber(number):
    try:
        reg=re.compile(r"\d{3}-\d{3}-\d{4}")
        mo=re.search(reg,number)
        print(mo.group() )
    except:
        print("sorry no number in it")
    
isPhoneNumber("here is the phone number 265-56-3545 feel free to connet")   
