import json

temp = {
    "questions":{
        1:"test question"
    },
    "answers":{
        1:{"A":["blah blah blah",True], "B":["blah blah blah",False], "C":["blah blah blah",False], "D":["blah blah blah",False]}
    }
}

f = open('/Users/yoavkitai/Documents/Bynet/GCP/quiz_proj/ml_questions.json', 'w')
json.dump(temp, f, indent=4)
f.close()