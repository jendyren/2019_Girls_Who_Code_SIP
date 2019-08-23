import json
import statistics
ages = []
may = 0
december = 0
with open('results.json') as json_file:
    data = json.load(json_file)
questions = [['What is your name?','Name'],['Is water wet?','wet'],['What is your age?','Age'],['Do you sleep with socks on?','Socks'],['Do you think pineapple belongs on pizza?','Pizza'],['Do you put milk or cereal first?','Cereal'],['Name the app, program, or website that you use most frequently.','Program/App']]
for person in data:
    for question in questions:
        print (question[0]+':  '+data[person][question[1]])
        #if question[1] == 'Age' : ages.append(int(data[person][question[1]]))
        #if question[1] == 'Birthday' and data[person][question[1]] [1] == '5' : may+=1
        #if question[1] == 'Birthday' and data[person][question[1]] [0] == '1' and data[person][question[1]] [2] == '1':
            #december+=1
    print ('\n\n')
