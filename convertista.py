#! /anaconda3/bin/python

# converts temperature to fahrenheit or celsius

def print_options():
    print("Options: ")
    print(" 'p' print options")
    print(" 'c' convert from celsius")
    print(" 'f' convert from fahrenheit")
    print(" 'q' quit the program")

def celsius_to_fahrenheit(temp):
    converter = 9.0/5.0
    temp = float(temp) + 32.0
    temp = temp*converter
    return temp

def fahrenheit_to_celsius(temp):
	converter = 5.0/9.0
	temp = float(temp) - 32.0
	temp = temp * converter
	return temp

print("Welcome to the Python Temperature Converter")
choice = "p"
temp = 0.0
float(temp)
while choice != "q":
    if choice == "c":
        temp = input("Celsius temperature:")
        # int(temp)
        print("Fahrenheit:", celsius_to_fahrenheit(temp))
    elif choice == "f":
        temp = input ("Fahrenheit temperature:")
        print("Celsius:", fahrenheit_to_celsius(temp))
    elif choice != "q":
        print_options()
    choice = input("option: ")
