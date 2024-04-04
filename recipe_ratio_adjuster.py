#Task 1
'''
try:
    original_servings = int(input("Please enter the number of servings for the original recipe:  "))
    new_servings = int(input("Please enter the number of servings you wish to make: "))
    if original_servings < 1 or new_servings < 1:
        raise Exception("Sorry the numbers input must be greater than zero.")
except ValueError:
    print("You must enter a whole positive number.")
'''

#Task 2
'''
try:
    ratio = round(new_servings/original_servings, 2)
    print(ratio)
except ZeroDivisionError:
    print("Sorry, can't divide by zero.")
except:
    print("An unxpected error occured, please try again.")
'''


#Task 3

try:
    original_servings = int(input("Please enter the number of servings for the original recipe:  "))
    new_servings = int(input("Please enter the number of servings you wish to make: "))
    if original_servings < 1 or new_servings < 1:
        raise Exception("Sorry the numbers input must be greater than zero.")
    ratio = round(new_servings/original_servings, 2)
    print(f"You will want to multiply your ingredients by {ratio} in order to make your desired servings.")

except ValueError:
    print("You must enter a whole positive number.")
except ZeroDivisionError:
    print("Sorry, can't divide by zero.")
except:
    print("An unxpected error occured, please try again.")
finally:
    print("Enjoy your cooking!")
