#https://www.coderbyte.com/editor/guest:Questions%20Marks:Python

def QuestionsMarks(str): 
    no1=0
    no2=0
    for i in range(len(str)-1):
        for j in range(i,len(str)):
            if str[i].isdigit() and str[j].isdigit() and int(str[i])+int(str[j])==10:
                no1=i
                no2=j
    question=str[no1+1:no2+1]
    if question.count("?")==3:
        return "true"
    return "false"

print(QuestionsMarks("acc?7??sss?3rr1??????5"))


  
