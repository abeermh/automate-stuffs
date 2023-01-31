theBoard={
    "tL":" ","tM":" ","tR":" ",
    "mL":" ","mM":" ","mR":" ",
    "lL":" ","lM":" ","lR":" ",
}
def printBoard(theBoard):
    print(theBoard["tL"] +"|"+theBoard["tM"] +"|"+theBoard["tR"] )
    print("-+-+-")
    print(theBoard["mL"] +"|"+theBoard["mM"] +"|"+theBoard["mR"] )
    print("-+-+-")
    print(theBoard["lL"] +"|"+theBoard["lM"] +"|"+theBoard["lR"] )

def checkWinner(turn):
    dirs={}
    for i in theBoard.keys():
        if turn==theBoard[i]:
            #for row checks
            dirs.setdefault(i[-1],0)
            dirs[i[-1]]+=1
            #for cloumn checks
            dirs.setdefault(i[0],0)
            dirs[i[0]]+=1
            #for diagonal cheeck
            dirs.setdefault(i,0)
            dirs[i]+=1
            
    if 3 in dirs.values():
        return 1
    elif 'mM' in dirs.keys() :
        if ('tL'in dirs.keys() and 'lR'in dirs.keys()) or ('tR'in dirs.keys() and 'lL'in dirs.keys()):
            return 1
        else:
            return 0
                
    else :
        return 0

turn='X'

for i in range(9):
    printBoard(theBoard)
    print(('Turn for ' + turn + '. Move on which space?'))
    dir=input()
    if dir in theBoard.keys() and theBoard[dir]==' ':
        theBoard[dir]=turn
        if i >=4 :
            if(checkWinner(turn)):
                printBoard(theBoard)
                print("the winner is "+turn)
                break
        if turn=='X':
            turn='O'
        else:
            turn='X'
        
    else:
        print("enter a valid direction")
        i-=1
