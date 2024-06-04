# Harrison May
# 10LWD
# Get Width Prgramme 1.0
# 15/05/2024

#Ask user for width and loop until they
# enter a number that is more than zero

error = "Please enter a number that is more than zero/n"

while True:

    try:
        width = float(input("Width: "))

        if width > 0:
            break
        else:
            print(error)
    except: ValueError
    print (error)
    