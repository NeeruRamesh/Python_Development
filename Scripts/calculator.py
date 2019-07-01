print("Welcome to Calcy\n")
print("You can perform almost all the operations.\nJust keep evaluating results continuously.\nIf you want to calculate new set of results,\nclear the old results by typing 'Clear'\n");
print("Type 'QUIT' to exit\n")

prev = 0
run = True

def calculate():
    global run
    global prev
    try:
        eqn = ""     
        if prev == 0:
            eqn = input("Enter the expression:\t")
        else:
            eqn = input(str(prev))
            print(" ")

     
        if eqn == 'QUIT' or eqn == 'quit' or eqn == 'Quit':
           print("\nGoodbye :)")
           run = False

        if prev == 0:
           prev = eval(eqn)

        else:   
            prev = eval(str(prev)+eqn)   
          
    except:
        if eqn == 'clear' or eqn == 'Clear' or eqn == 'CLEAR':
            eqn = ""
            prev = 0
            calculate()
            
        elif eqn == 'QUIT' or eqn == 'quit' or eqn == 'Quit':
            print("\nGoodbye :)")
            run = False

        else:
            print("\n***Please Enter a valid expression***\n\nType 'Clear' to Clear previous results\n\nType 'QUIT' to exit\n")
while(run):
    calculate()
