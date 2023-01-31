def printtable(table):
    colwidth=[0]*len(table)
   
    for i in range(len(table)):
        colwidth[i]=len(max(table[i],key=len))
    
    for i in range (len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colwidth[j]),end=" ")
        print("\n")
tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]
 
printtable(tableData)
