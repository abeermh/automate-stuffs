'''
reads in text files and lets the user add 
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file
'''
import re

print("enter the file name(remember to include the extension \'.txt\']): ")
filename="story.txt"
fin=open(filename,"r")
data=fin.read()
fin.close()
adj=input("enter the adjective : ")
noun=input("enter the noun : ")
verb=input("enter the verb : ")
adverb=input("enter the adverb : ")

data=re.sub("ADJECTIVE",adj, data)
data=re.sub("NOUN",noun, data)
data=re.sub("VERB",verb, data)
data=re.sub("ADVERB",adverb, data)
print(data)
fout=open(filename,"w") 
fout.write(data)

fout.close()
print("done")
