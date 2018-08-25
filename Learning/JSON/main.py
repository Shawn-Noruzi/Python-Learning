import json
import os

#creation of files, converting b/w json and python objs, read/write, array


#if file exists and file size is not 0.
if os.path.isfile("ages.json") and os.stat("ages.json").st_size != 0:
    with open("ages.json", "r+") as filehandle:
        data = json.load(filehandle)
        filehandle.seek(0)
        print("Current age is", data["age"], "-- adding a year.")
        data["age"] = data["age"] + 1
        print("new age is ", data["age"])
        json.dump(data,filehandle)

else: 
    with open('ages.json','w') as outfile:
        data = { "name": "Nick", "age" : 25 }
        print("No file found, setting default age to ", data["age"])
        json.dump(data,outfile)
