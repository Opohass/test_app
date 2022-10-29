from copy import copy
import json
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
with open("quiz_data_devlop/quiz_json/Security Engineer.json") as j: 
                temp_question=json.load(j)
abc=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
quest=""
ans={}
count=len(temp_question["questions"])+1

for line in Lines:
    if  "-porat-"  in line:
        temp= input("enter answer:")
        temp=temp.upper()
        for letter in temp:
           ans[letter][1]="true"
            
        temp_question["questions"][str(count)]=copy(quest) 
        temp_question["answers"][str(count)]=copy(ans) 
        temp_question["images"][str(count)]="false"
        temp_question["multiple_choice"][str(count)]= len(temp)>1
        
        
        count+=1
        quest=""
        ans={}
    else:
        if line[0] not in abc:
            quest+=line
        else:
            
            ans[line[0]] = [line[2:],"false"]
        
    
        
print()