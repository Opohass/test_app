import json
import os

# Enter Text Below
# <EXAMPLE> IS TO BE REPLACED
# In The format of:
# text_to_add = [
# <question string>,
# [<ANSWER_A>, True],
# [<ANSWER_B>, False],
# [<ANSWER_C>, False],
# [<ANSWER_D>, False],
# [<ANSWER_E (You Can Leave Empty If There Is No Option)>, False],
# [<ANSWER_F (You Can Leave Empty If There Is No Option)>, False],
# [<ANSWER_G (You Can Leave Empty If There Is No Option)>, False],
# [<ANSWER_H (You Can Leave Empty If There Is No Option)>, False],
# <IMAGE NAME> or False,
# <MULTI-CHOICE> (True Or False)
# ]

text_to_add = [
    # Question 29
    # Question String
    "",
    # Options (A - G) - Only A, B, C And D Are Required
    ["", False],
    ["", False],
    ["", False],
    ["", False],
    ["", False],
    ["", False],
    ["", False],
    ["", False],
    # Image Name And quiz (i.e "developer/example.png"), If no Image Then Leave Empty
    False,
    # Is Question Multiple Choice, If It Is Then Change To True
    False
]
path = os.getcwd() + "/quiz_data/ml_questions.json"
f = open(path, 'r')
data = json.load(f)
f.close()
for i in range(0, len(text_to_add), 11):
    next_pos = str(int(list(data["questions"].keys())[-1]) + 1)
    print()
    data["questions"][next_pos] = text_to_add[i]
    data['answers'][next_pos] = {"A":text_to_add[i+1], "B":text_to_add[i+2], "C":text_to_add[i+3], "D":text_to_add[i+4]}
    if text_to_add[i+5][0] != "":
        data["answers"][next_pos]["E"] = text_to_add[i+5]
        if text_to_add[i+6][0] != "":
            data["answers"][next_pos]["F"] = text_to_add[i+6]
            if text_to_add[i+7][0] != "":
                data["answers"][next_pos]["G"] = text_to_add[i+7]
                if text_to_add[i+8][0] != "":
                    data["answers"][next_pos]["H"] = text_to_add[i+8]
        
    data["images"][next_pos] = text_to_add[i+9]
    data["multi_choice"][next_pos] = text_to_add[i+10]
        
f = open(path, 'w')
json.dump(data, f, indent=4)
f.close()