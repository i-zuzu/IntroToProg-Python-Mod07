# ------------------------------------------------------------------------ #
# Title: Assignment 07 Structured Error (Demo)
# Description: This script calculates the speed and
#              demonstrates how Structured error handling works
# ChangeLog (Who,When,What):
# Irina Zubova,2-27-2020, Created the script
# ------------------------------------------------------------------------ #

#---Data---

distance = 100 # total distance of the race
strInput = ""  # time to finish the race

#Input/Output and Processing---

print("You completed 100 miles race.")
while True:
    try:
        strInput = input("\n Please enter your time in hours: ")
        if strInput == 'exit':
            break
        time = float(strInput)
        if 1 > time > 0:
            raise Exception('Time evolved should not be less than 1 hr')
        speed = round(100/time)
    except ZeroDivisionError:       #2nd specific exception
        print("You didn't race.")
    except ValueError:              #1st specific exception
        print("This was not an integer number.")
    except Exception as e:          #custom exception
        print('Seems like a wrong number. Try again.')
        print (e)
    else:                           #no exception
        print("The speed is", str(speed),  "miles/hr")

