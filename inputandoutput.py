#Input and Output
# Harrison May
# 3 May 2024
# Version 1

#ask the user for thier name
username = input("What is your name? ")
#ask the user for their favorite number (integer)
fav_num = int(input("What is your favourite number? "))
#double, halve and square the user's favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num
#greet the user
print()
print(f"Hi {username}, your favorite number is {fav_num}")

#output the results of doubling, halving
#and squaring their favourite integer
print(f"Double {fav_num} is {double}.")
print(f"Half {fav_num} is {halve}")
print(f"{fav_num} squared is {square}")
print()
print("Have a nice day.")
print()