import re
print("print 'quit' to exit \n")

prevoius=0
run=True

def performMath():
    global run
    equation= input("enter equation:")
    print("entered values", eval(str(equation)))

    if equation == 'quit':
        print("Good bye")
        run=False

while run:
    performMath()