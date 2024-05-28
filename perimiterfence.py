# Author: Harrison May
# Date: 22/05/2024
# Version: 1.0

# The loop to let the code run indefinintely
while True:

    try:
        # Defining width and length
        width = int(input("Width: "))
        length = int(input("Length: "))
        cost = int(input("Cost: "))
        squareunits = (" square units.")
       
       # The code to get the perimeter and cost of the fence
        if width > 0 and length > 0 and cost > 0:
            perimeter = width+length
            perimeter += perimeter
            print(f"perimeter = {perimeter}m")
            cost = perimeter*cost
            print(cost)
        

            

        else:
            print("Invalid value")

    except ValueError:
        print("placeholder")
