# Write a program that converts and prints user given measurement in inches into
# 1. foot(12 inches)
# 2. yard(36 inches)
# 3. centimetres(2.54 inches)
# 4. meter(39.37 inches)

import sys

def convert_inches():
    INCHES_IN_FOOT = 12
    INCHES_IN_YARD = 36
    CM_PER_INCH = 2.54
    INCHES_IN_METER = 39.37

    print("--- Inches Unit Converter ---")

    try:
        inches_input = input("Please enter the measurement in inches: ")
        
        if not inches_input:
            print("Error: Input cannot be empty.")
            return
            
        inches = float(inches_input)
        
        if inches < 0:
            print("Error: Please enter a non-negative measurement.")
            return

    except ValueError:
        print(f"Error: '{inches_input}' is not a valid number. Please enter a numeric value.")
        return

    feet = inches / INCHES_IN_FOOT
    yards = inches / INCHES_IN_YARD
    centimetres = inches * CM_PER_INCH
    meters = inches / INCHES_IN_METER
    
    print(f"1. Feet:         {feet:.4f} ft")
    print(f"2. Yards:        {yards:.4f} yd")
    print(f"3. Centimeters:  {centimetres:.4f} cm")
    print(f"4. Meters:       {meters:.4f} m")

if __name__ == "__main__":
    convert_inches()