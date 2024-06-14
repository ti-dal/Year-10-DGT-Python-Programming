# Author: Harrison May
# Date: 12/06/2024
# Version 1.0
# code contributed by ryugway industries

# Defines the conversions and conversion rates
def DistanceCalculator(value, from_unit, to_unit):
    # Creates a dictionary to define the conversion rates
    distancefactors = {
        "cm": {"m": 0.01, "mm": 10, "km": 0.000001},
        "m": {"cm": 100, "mm": 1000, "km": 0.001},
        "mm": {"cm": 0.1, "m": 0.001, "km": 1e-6},
        "km": {"cm": 100000, "m": 1000, "mm": 1e+6},
    }
    
    try:
        # Multiplies the answer to convert if an incorrect value is entered it will print "Distance Conversion Error"
        result = value * distancefactors[from_unit][to_unit]
        print(f"{result:.2f}{to_unit}")
    except ValueError:
        print("Distance Conversion Error")

# Same as the distance converter but for time
def TimeCalculator(value, from_unit, to_unit):
    timefactors = {
        "seconds": {"minute": 0.01667, "hours": 2778e-4, "days":1.1575e-05 },
        "mintues": {"seconds": 60, "hours": 0.01667, "days":6.94e-04 },
        "hours": {"seconds": 3600, "minutes": 60, "days": 0.041667},
        "days": {"seconds": 86400, "minutes": 1440, "hours":24 },
    }
    try:
        result = value * timefactors[from_unit][to_unit]
        print(f"{result:.2f}{to_unit}")
    except ValueError:
        print("Time Conversion Error")

# def MassCalculator(value, from_unit, to_unit):
#     massfactors = {
#         "mg": {"g": , "kg": , "t": },
#         "g": {"mg": , "kg": , "t": },
#         "kg": {"g": , "mg": , "t": },
#         "t": {"g": , "kg": , "mg": },
#     }


# Makes the programm run until complete is true.
complete = False
while not complete:
     # A welcome message and a question asking what the user would like to convert.
     print("Welcome to the Ultimate Conversion Calculator. ")
     print("What would you like to convert? ")
     conversionoption = str(input("For distance type: 'distance' For time type: 'time' For Weight/Mass type: 'mass' "))
     # Checks to see if the user asked to run the 'distance' calculator
     if conversionoption == "distance":
        fromunitdistance = input(str("From what unit? mm, cm, m, km"))
        tounitdistance = input(str("To what unit? mm, cm, m, km"))
        value = int(input("How many?"))
        DistanceCalculator(value, fromunitdistance, tounitdistance)
     elif conversionoption == "time":
        print("time test")
     elif conversionoption == "mass":
         print("mass test")
         
    

# conversiondistance(100, "cm","m")
