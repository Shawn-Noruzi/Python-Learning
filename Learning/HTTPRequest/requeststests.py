import requests
#Extracting data from websites using requests library
params = {"#q" : "pizza"}
r = requests.get("http://www.google.com", params = params)
print("Status: ", r.status_code)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)

#get vs post
#get is put into url
#post isnt

my_data = {"name":"Nick", "email": "nick@ecample.co"}

r = requests.post("http://www.w3schools.com/php/welcome.php", data = my_data)

#posting data
#make a file called myfile thats writable too and set it to f
f = open("myfile.html", "w+")
f.write(r.text)