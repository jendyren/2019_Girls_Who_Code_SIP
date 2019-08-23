#this prgram will print out all of the text data from our
#twitter JSON file.

import json

#open the json file
tweetFile = open("./data.json", "r")

#get data from the opened file
tweetData = json.load(tweetFile)

#close the file because we already have the data stored
tweetFile.close()

print("Tweet id: ", tweetData[0]["id"])

print("Tweet text: ", tweetData[0]["text"])

for idx in range(len(tweetData)):
    print("Tweet id: ", tweetData[idx]["id"])

for tweet in tweetData:
    print("Tweet text: ", tweet["text"])
