# Author: Harrison May
# Date: 5/06/2024
# Version: 1.2

# Ends the programme
finished = False
# The loop to let the code run indefinintely until asked to stop
while not finished:

    try:
        # Defining width, length and cost
        
        width = int(input("Width: "))
        length = int(input("Length: "))
        cost = int(input("Cost: "))
        
       
       # The code to get the perimeter and cost of the fence
        if width > 0 and length > 0 and cost > 0:
            # Adding the perimeter
            perimeter = (width+length)*2
            print(f"perimeter = {perimeter}m") # Displays the perimeter with "m" after the value for the unit of measurement
            cost = perimeter*cost
            cost = str(cost)
            print("$" + cost)
            # Asking the user if they want to continue
            end_program = input(str("Press Enter to continue or press q to quit. "))
            if end_program == "q":
                print ("Thank you for using the perimiter calculator. ")
                finished = True
            else:
                print("restart")
            
        # If the user inputs an invalid number display "Invalid value"
        else:
            print("Invalid value")

    # If the user inputs an invalid character (excluding numbers) display "Invalid input"
    except ValueError:
        print("Invalid input")


