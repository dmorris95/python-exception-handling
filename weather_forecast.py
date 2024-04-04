#Task 1
'''
temp = "1"
try:
    while temp != "":
        temp = int(input("Enter the temperature in Fahrenheit: "))

except ValueError:
    print("Sorry, only numbers can be entered.")
'''

#Task 2
'''
def temp_converter(f_temp):
    try:
        return (f_temp - 32) * (5/9)
    except ZeroDivisionError:
        print("Sorry no dividing by zero here.")
    except OverflowError:
        print("Too many numbers we might overflow the system.")    

temp = "1"
try:
    while temp != "":
        temp = int(input("Enter the temperature in Fahrenheit: "))
        print(f"{temp_converter(temp)} is the temperature in celsius.")
except ValueError:
    print("Sorry, only numbers can be entered.")
'''

#Task 3


def temp_converter(f_temp):
    try:
        c_temp = (f_temp - 32) * (5/9)
    except ZeroDivisionError:
        print("Sorry no dividing by zero here.")
    except OverflowError:
        print("Too many numbers we might overflow the system.")    
    else:
        c_temp = round(c_temp, 2)
        print(f"The temperature in Celsius is {c_temp}")
    finally:
        print("Thank you for using the weather application.")
temp = "1"
try:
    temp = int(input("Enter the temperature in Fahrenheit: "))
    temp_converter(temp)
except ValueError:
    print("Sorry, only numbers can be entered.")
