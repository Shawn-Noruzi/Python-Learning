#creates new file with writing capability
newfile = open("newfile.txt", "w+")

#we want this into it
string = "This will be written to newfile.txt"

#run the function where we write string into it.
newfile.write(string)

