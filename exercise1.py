def collatz(number):
    if number%2==0:
        #even
        print(number//2)
        return number//2
    else:
        #odd
        print(3*number+1)
        return(3*number+1)
try:
    print("enter a number : ")
    number=int(input())
    while(number!=1 ):
        number=collatz(number)
        if number==0:
            break
    
except:
    print("error , you must enter an integer")


