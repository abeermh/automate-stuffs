
'''
a program that opens all .txt files in a folder and searches for any 
line that matches a user-supplied regular expression. The results should 
be printed to the screen. 
'''

import os,re

regex="user input"
files=[f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  data=open(f).read()
  matches=re.findall(regex,data)
  print(matches)