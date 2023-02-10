'''
create 35 quiz for students about capitals from local file in my pc 
1 : make dir for all quiz files to be organized
2 : open the file and get all the data into a list
3: create 26 file for each quiz and another 26 file for the answers
'''
import os ,re , random

isExist=os.path.exists(".\\quizzes")
if not isExist:
    os.makedirs(".\\quizzes")

dict={}
quizfile=open("capitals.txt","r")

for f in quizfile:
    f=re.sub(r"\n","",f)
    (key,value)=f.split(',')
    dict[key]=value

#generate quiz and answer files
for qn in range(35):
    quizfile=open(".\\quizzes\\quiz%s.txt"%(qn+1),"w")
    modelanswer=open(".\\quizzes\\quizanswer%s.txt"%(qn+1),"w")

    quizfile.write("Name:\nDate:\nClass:\n\n")
    quizfile.write((' '*20)+"governorates capitals of Egypt quiz \n\n\n")

    governoratesList=list(dict.keys())
    random.shuffle(governoratesList)

    #create the answer options 
    answers=[]
   
    for i in range(26):
        #26 number of governorates in egypt
        correctanswer=dict[governoratesList[i]];
        wronganswer=list(dict.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wronganswer=random.sample(wronganswer,3)
        answers=[correctanswer]+wronganswer
        random.shuffle(answers)


        #write questions and answers to the files 
        quizfile.write("%s.what is the capital of %s\n"%(i+1,governoratesList[i]))
        for j in range(4):
            #4 options for the answer
            quizfile.write("%s.%s\n"%('ABCD'[j],answers[j]))
        quizfile.write("\n")

        #write correct answers to the answer model 
        modelanswer.write("%s. %s\n"%(i+1,'ABCD'[answers.index(correctanswer)]))
    quizfile.close()
    modelanswer.close()
