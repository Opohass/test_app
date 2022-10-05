import json

# Enter Text Below
# <EXAMPLE> IS TO BE REPLACED
# In The format of:
# text_to_add = [
# <question string>,
# [<ANSWER_A>, True],
# [<ANSWER_B>, False],
# [<ANSWER_C>, False],
# [<ANSWER_D>, False],
# ]

text_to_add = [
    "",
    ["", True],
    ["", False],
    ["", False],
    ["", False]
]

f = open('/Users/yoavkitai/Documents/Bynet/GCP/quiz_proj/ml_questions.json', 'r')
data = json.load(f)
f.close()
for i in range(0, len(text_to_add), 5):
    next_pos = str(int(list(data["questions"].keys())[-1]) + 1)
    data["questions"][next_pos] = text_to_add[i]
    data['answers'][next_pos] = {"A":text_to_add[i+1], "B":text_to_add[i+2], "C":text_to_add[i+3], "D":text_to_add[i+4]}
f = open('/Users/yoavkitai/Documents/Bynet/GCP/quiz_proj/ml_questions.json', 'w')
json.dump(data, f, indent=4)
f.close()