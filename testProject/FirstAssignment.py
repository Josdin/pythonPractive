# Program for finding the BMI and to provide advice to user about body weight and height expectations.
import datetime

# Welcome message to the user
# Variables used:
# bodyHeight_345 for storing the height of the user, data type : float
# bodyWeight_345 for storing the weight of the user, data type : float
# calculated_BMI_345 for storing the BMI calculated  for the user, data type : float
# userName_345 for storing user's name to use in program.
# Author : Josdin Jose
# Student ID : 500209345
# Finding current date

currentDate_345 = str(datetime.date.today());

print("*************************************************************")
print("Welcome to program for finding BMI,  Created by : Josdin Jose")
print("*************************************************************")
# Reading user's name through console input and storing it in userName_345 variable .
userName_345 = input("Please enter your name to continue using the BMI program :\n")
print("Thank you for providing your name " + userName_345)

# Reading user's height through console input and storing it in bodyHeight_345 variable .
bodyHeight_345 = float(input("Please enter your height in inch for calculating the BMI :"))

# Reading user's weight through console input and storing it in bodyWeight_345 variable .
bodyWeight_345 = float(input("Please enter your weight in pound for calculating the BMI :"))

# validating user input
if 0 >= bodyWeight_345 or 0 >= bodyHeight_345:
    print("Entered values are not eligible for calculating BMI , Please start over")
    exit(0)

# Completed reading the user inputs
# Calculation phase begins.

calculated_BMI_345 = (bodyWeight_345 / (bodyHeight_345 * bodyHeight_345)) * 703
# Rounding off calculated BMI to 2 decimal places
calculated_BMI_345 = round(calculated_BMI_345, 2)
# printing user's BMI to console for user to see.
print("Hi " + userName_345 + " your calculated BMI is : " + str(calculated_BMI_345))

# BMI Standards
# BMI > 18.5 and BMI < 25 = Optimal
# BMI < 18.5 = Underweight
# BMI > 25 = Overweight
# Finding the health advice with the calculated BMI
if calculated_BMI_345 > 25:
    print("You are overweight as on :" + currentDate_345 + " consider changing your diet")
elif calculated_BMI_345 < 18:
    print("You are underweight as on :" + currentDate_345 + " consider changing your diet")
else:
    print("Your weight is optimal as on" + currentDate_345 + " keep up the good work")

print("Thanks " + userName_345 + " for using the BMI Calculation program")
