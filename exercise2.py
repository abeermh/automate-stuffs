catsNames=[]

while True:
    print("enter the name of cat "+str(len(catsNames)+1)+" or enter nothing to stop :")
    name=input()
    if name=='':
        break
    catsNames+=[name]

print("the cats names are :")    
for i in catsNames:
    print(i)
