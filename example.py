import json
Data = []


'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''

for i in range (0,1):
    print ("\nHello user. You will be asked a series of questions that you must answer truthfully. Get ready.")
    print ("Start")
    user1= input("\nWhat is your name? ")
    user1 = {}
    user_age = input("\nWhat is your age? ")
    user1["Age"] = user_age
    user_waterwet = input("\nDo you believe water is wet? ")
    user1["Is water wet?"] = user_waterwet
    user_socks = input("\nDo you sleep with your socks on? ")
    user1["Sleep with socks?"] = user_socks
    user_pizza = input("\nDo you agree with pineapple on pizza? ")
    user1["Pinapple on pizza?"] = user_pizza
    user_breakfast = input("\nMilk or Cereal first? ")
    user1["Start with?"] = user_breakfast
    user_saying = input("\nWhat is a saying you say a lot? ")
    user1["Saying"] = user_saying
    print(user1)
    Data.append(user1)
print (Data)

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

# Example
data = {}
data['key'] = 'value'

writeToJSONFile('./','file-name',data)
# './' represents the current directory so the directory save-file.py is in
# 'test' is my file name

#"Do you think water is wet?"
#"Do you sleep with your socks on?"
#"Do you agree with pineapples on pizza?"
# Print the context of the dictionary.

import json
data = {'cat' : 'dog'}
def ask (question):
    return (input(questions+'   '))
questions = [['What is your name?', 'Name'],['What is your age?', 'Age'],['Do you believe water is wet?', 'Answer'],['Do you sleep with your socks on?', 'Answer2'],['Do you agree with pineapple on pizza?','Answer3'],['What is a saying you say alot?', 'saying']]

while True:
    print ('\n\nStarting new survey!')
    answer = {}
    for q in questions:
        answer[q[1]] = ask(q[0])
    with open('results.json') as json_file:
        data = json.load(json_file)
        data.update({answer['Name']:answer})
        with open('results.json', 'w') as outfile:
            json.dump(data, outfile)
