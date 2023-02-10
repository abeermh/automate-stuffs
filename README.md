# automate-stuffs
this Repo is practical guide for "automate the boring stuff with python " book 
________________________________________________________________________________

# intruduction 

Al Sweigart is a software developer and tech book author
His books are freely available on his website :
https://inventwithpython.com/

## Part 1
### ********* chapter 1 ( Python Basics ) *********

- operators
- data types
- string concatination  (+)
- string repeating (*)
- valid variable naming
- program for say hello and print name and age ,use casting 
- can use the conditon of comparing int and floating point values , integer can be equal to a
floating point (42==42.00 will return true )

### ********* chapter 2 ( Flow Control ) *********

- comparison operators
- boolean operators
- flow control statement (if , while , break , continue , for )
- importing modules
- end program using sys.exit()
- round and abs

### ********* chapter 3 ( Functions ) *********

- return value from function
- None value 
- print without newline and change seperator in it
- global and local scope
- 'global' in function to change in global variables
```
	def spam():
	    print(eggs) # ERROR!
	    eggs = 'spam local'
	eggs = 'global'
	spam()
```
error because print(eggs) is executed before eggs is assigned anything, the local variable eggs doesn’t exist. Python will not fall back to using
the global eggs variable 

-handling exception

- [project about collatz sequence](https://github.com/abeermh/automate-stuffs/blob/main/exercise1.py)

### ********* chapter 4 ( Lists ) *********

- negative index to get the values from the end
- sublist by slice the list
- list concatination (+) list replication (*)
- revmove list items (del)


- [program to print cats names to practice list](https://github.com/abeermh/automate-stuffs/blob/main/exercise2.py)

- 'in' and 'not in' operators
- multiple assignment trick :
	cat = ['fat', 'black', 'loud']
	size, color, disposition = cat
- methods : is like a function except it is called on a value 
- list like types : string , tuple (used to display a list of options that can't be change)
- list is mutable (change it , assign on it or remove from it ), string and tuple is immutable
- practice projects

* convert list to comma seperated string 
```
def tostr(list):
    str=''
    str=", ".join(list[item] for item in range (len(list)-1))
    str+=(' and '+list[-1])      
    print(str)
    
spam = ['apples', 'bananas', 'tofu', 'cats']
tostr(spam)
```

* [rotate list of lists](https://github.com/abeermh/automate-stuffs/blob/main/exercise3.py)

### ********* chapter 5  ( Dictionaries and Structuring Data ) *********

dictionaries : unordered , key value pairs
- dict methods : keys , values , items , get ,setdefault
- set default exercise:

- [pprint format](https://github.com/abeermh/automate-stuffs/blob/main/exercise4.py)
- [A Tic-Tac-Toe Board ](https://github.com/abeermh/automate-stuffs/blob/main/exercise5.py) 

### ********* chapter 6 ( Manipulating Strings  ) *********
 
- string methods
	isalnum , isspace , isdecimal ,istitle , startswith , endswith , join , split , rjust
	ljust , center ,strip, rstrip, lstrip

- [rotate list of lists]:(https://github.com/abeermh/automate-stuffs/blob/main/exercise6.py)


##Part 2 :
### ********* chapter 7( Pattern Matching With Regular Expressions  ) *********


- regular expression : regexes
- greedy vs non greedy matching 
- '?' prevent greedy 

- [project to check number in text](https://github.com/abeermh/automate-stuffs/blob/main/exercise7.py)

- [project to check strong password](https://github.com/abeermh/automate-stuffs/blob/main/exercise8.py)

- [project like strip function using regexes](https://github.com/abeermh/automate-stuffs/blob/main/exercise9.py)


### ********* chapter 8 ( Reading and Writing Files ) *********

-files and directories
-makedirs , abspath , isabs ,getcwd, chdir , 
path = dirname + basename (use split with any path to get them)
-getsize , listdir , exist ,isdir , isfile
-read and write in files :
	* read , readlines , write
	
- save data with shelve files like dictionaries (key value pairs)	

### ********* chapter 9 ( Organizing Files ) *********

- file reading and writing process
```
 from pathlib import Path
 p = Path('spam.txt')
 p.write_text('Hello, world!')	#for writing
 print(p.read_text())		# for reading 
```
- shelve module 
- pprint.pformat()
- [random quiz files creation]()
- [Updatable Multi-Clipboar]()
-  [keywords replacement in txt file]()
-  [regex search]()

### ********* chapter 10 ( Debugging ) *********

### ********* chapter 11 ( Web Scraping ) *********

### ********* chapter 12 ( Working With Excel Spreadsheets ) *********

### ********* chapter 13 ( Working With PDF & Work Documents ) *********

### ********* chapter 14 ( Working With CSV Files & JSON Data ) *********

### ********* chapter 15 ( Keeping Time Scheduling Tasks & Launching Programs ) *********

### ********* chapter 16 ( Sending Email & Text Messages ) *********

### ********* chapter 17 ( Manipulating Images ) *********

### ********* chapter 18 ( Controling the keyboard & Mouse With GUI Automation  ) *********

