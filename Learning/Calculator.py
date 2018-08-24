import re 
print("Calculator 2018 - Shawn Noruzi")
print("Type Quit to Exit \n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation=""
    if previous == 0:
        equation = input('Enter Equation: ')
    else: 
        equation = input(str(previous))

    if equation == 'quit':
       print('goodbye!')
       run = False 
    else:
        equation = re.sub('[a-zA-z,.:()" "]','',equation) #important to prevent script kiddies from hacking my calculator. 

        if previous==0 :
          previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print(previous)

while run: 
    performMath()