import math

print("-------------Unit Converter---------------\n")

print("Length | Area | Speed | Pressure | Temprature\n")

user = input("Enter: ")
if user == "Length":
    print("press 1 to convert metre in kilometres \n"
               "Press 2 to convert meters in to centimeters \n"
               "Press 3 to convert meters in to Foot \n"
               "Press 4 to convert meters in to Yards \n"
               "Press 5 to convert meters in to Yards ")

    MK = input("Enter Choice: ")

    if MK == "1":
        metre = int(input("Enter meters: "))
        result1 = metre / 1000
        print("Your distance is",result1, "Kilometers")

    if MK == "2":
        metre = int(input("Enter meters: "))
        result2 = metre * 100
        print(result2, "Centimeters")
    
    if MK == "3":
        metre = int(input("Enter meters: "))
        result3 = metre * 3.281
        print(result3, "Foots")
    
    if MK == "4":
        metre = int(input("Enter meters: "))
        result4 = metre * 1.094
        print(result4, "Yards")

    if MK == "5":
        metre = int(input("Enter meters: "))
        result5 = metre / 1609
        print(result5, "Miles")



if user == "Area":
    print("Press 1 to convert square Kilometer to square meter: \n"
               "Press 2 to convert square Kilometer to square MILES: \n"
               "Press 3 to convert square Kilometer to square YARDS: \n"
               "Press 4 to convert square Kilometer to square FOOT: \n"
               "Press 5 to convert square Kilometer to square ACRES \n")
               
    Sk = input("Enter Choice: ")
   
    if Sk == "1":
        Sk = int(input("Enter Square kilometer: "))
        result6 = Sk / 10**6
        print(result6, "Square Kilometers:")

    if Sk == "2":
        Smk= int(input("Enter Square kilometer: "))
        result7 = Sk / 2.59e6
        print(result7, "Square MILES:")

    if Sk == "3":
        Sk = int(input("Enter Square kilometer: "))
        result8 = Sk * 1.196
        print(result8, "Square Yards:")

    if Sk == "4":
        Sk = int(input("Enter Square kilometer: "))
        result9 = Sk * 10.764
        print(result9, "Square foots:")
    
    if Sk == "5":
        Sk = int(input("Enter Square kilometer: "))
        result10 = Sk / 4047
        print(result10, "Square Acres:")
        


if user == "Speed":
    print("Press 1 to convert Meter/second to MPH: \n"
               "Press 2 to convert M/S to Foot/Sec: \n"
               "Press 3 to convert M/S to KPH: \n"
               "Press 4 to convert M/S to Knot: \n")    
    
    SP = input("Enter Choice: ")

    if SP == "1":
        SP = int(input("Enter meter per second: "))
        result11 = SP * 2.237
        print(result11, "MPH")

    if SP == "2":
        SP = int(input("Enter meter per second: "))
        result11 = SP * 3.281
        print(result11, "Foot Per Second")
        
    if SP == "3":
        SP = int(input("Enter meter per second: "))
        result11 = SP * 3.6
        print(result11, "KmPH")
    
    if SP == "4":
        SP = int(input("Enter meter per second: "))
        result11 = SP * 1.944
        print(result11, "Knots")


if user == "Pressure":
    print("press 1 to convert pascals in Torr: \n"
               "Press 2 to convert pascals in standard atmosphere: \n")
    
    PS = input("Enter Choice: ")
    if PS == "1":
        PS = int(input("Enter Pascal: "))
        result12 = PS / 133.3
        print(result12, "Torrs")

    if PS == "2":
        PS = int(input("Enter Pascal: "))
        result12 = PS / 101300
        print(result12, "Standard Atmosphere")

if user == "Temprature":
    print("press 1 to convert Degree in Farenhiet: \n"
               "Press 2 to conver degree in kelvin")
    
    TP = input("Enter Choice:")
    if TP == "1":
        TP = int(input("Enter Degrees: "))
        result13 = (TP * 9/5) + 32
        print(result13, "Farenhiets")

    if TP == "2":
        TP = int(input("Enter Degrees: "))
        result14 = TP + 273.15
        print(result14, "Kelvins")
