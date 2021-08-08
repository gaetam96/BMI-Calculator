#English Standard BMI Calculator
print ("Would you like to use Metric or English Standard Measurements?")
question = input ("Standard or Metric measurements? s/m: ")
if question == "s":
    x = float (input ("What is your weight in lbs? "))
    y = float (input ("What is your height (feet)? "))
    z = float (input ("What is your height (inches)? "))
    ht = float ((y * 12) + z)

    BMI_Stndrd = (703 * x / (ht**2))
    print ("Your BMI is " + str(BMI_Stndrd))
    if BMI_Stndrd < 18.5:
        print("You are in the underweight range. ")
    elif BMI_Stndrd >= 18.5 and BMI_Stndrd <= 24.9:
        print("You are in a healthy range! ")
    elif BMI_Stndrd >= 25.0 and BMI_Stndrd <= 29.9:
        print("You are in the overweight range. ")
    elif BMI_Stndrd >= 30.0:
        print("You are in the obese range. ")
#Metric BMI Calculator
if question == "m":
    x = float (input ("What is your weight in kilograms? "))
    y = float (input ("What is your height meters? "))

    BMI_Stndrd = (x / (y**2))
    print ("Your BMI is " + str(BMI_Stndrd))
    if BMI_Stndrd < 18.5:
        print("You are in the underweight range. ")
    elif BMI_Stndrd >= 18.5 and BMI_Stndrd <= 24.9:
        print("You are in a healthy range! ")
    elif BMI_Stndrd >= 25.0 and BMI_Stndrd <= 29.9:
        print("You are in the overweight range. ")
    elif BMI_Stndrd >= 30.0:
        print("You are in the obese range. ")