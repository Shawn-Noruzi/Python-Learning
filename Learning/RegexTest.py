import re 

string = "Hey, I'm a dog trapped in a man's body. Help."
print(string)
new = re.sub('[a-z, ., \', A-Z+" "]','', string )
print(new)

string = string + "6 594309 - 234"
new = re.sub('[^0-9]','@ ',string)

print(new)