import json
data = {'cat' : 'dog'}
def ask (question):
    return (input(question+'   '))
questions = [['What is your name?','Name'],['Is water wet?','wet'],['What is your age?','Age'],['Do you sleep with socks on?','Socks'],['Do you think pineapple belongs on pizza?','Pizza'],['Do you put milk or cereal first?','Cereal'],['Name the app, program, or website that you use most frequently.','Program/App']]

while True:
    print ('\n\nStarting new survey!')
    answer={}
    for q in questions:
        answer[q[1]] = ask(q[0])
    with open('results.json') as json_file:
        data = json.load(json_file)
        data.update({answer['Name']:answer})
        with open('results.json', 'w') as outfile:
            json.dump(data, outfile)
