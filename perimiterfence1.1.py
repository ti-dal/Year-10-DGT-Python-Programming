# Author: Harrison May
# Date: 22/05/2024
# Version: 1.1

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
            twinkie_bar = input(str("Press Enter to continue or press q to quit."))
            if twinkie_bar == "q":
                finished = True
            else:
                print("restart")
            
        # If the user inputs an invalid number display "Invalid value"
        else:
            print("Invalid value")

    # If the user inputs an invalid character (excluding numbers) display "Invalid input"
    except ValueError:
        print("Invalid input")


