### **Irina Zubova**
### **March 1, 2021**
### **Foundations of Programming: Python**
### **Assignment 07**
### [https://github.com/i-zuzu/IntroToProg-Python-Mod07](https://github.com/i-zuzu/IntroToProg-Python-Mod07)




#                                                     **Exception Handling and Pickling in Python**


## **Introduction**
This page describes how I worked on Assignment07. It has some links from the web that describe how Pickling and Exception Handling work in Python. There will be 2 scripts that demonstrate how Pickling and Structured error handling work and explain what these scripts do.

## **Web Research on Exception Handling and Python**

For Exception handling I found the following webpages really helpful:
- [https://www.w3schools.com/python/python_try_except.asp](https://www.w3schools.com/python/python_try_except.asp)  (external site)
- [https://www.freecodecamp.org/news/exception-handling-python/](https://www.freecodecamp.org/news/exception-handling-python/) (external site)
- [https://www.tutorialspoint.com/python/python_exceptions.htm](https://www.tutorialspoint.com/python/python_exceptions.htm) (external site)

The first one is relatively short, it has many examples that helped me to understand how Exception works. I like starting from short, simple explanations and then build up more content on them. Then the next 2 links provide more details and descriptions. They outline at the beginning what they cover, also the third one has behind the scene diagrams showing how the program works. 

For Pickling I found these webpages really valuable:
*	[https://www.pitt.edu/~naraehan/python3/pickling.html](https://www.pitt.edu/~naraehan/python3/pickling.html) (external site)
*	[https://stackabuse.com/introduction-to-the-python-pickle-module/](https://stackabuse.com/introduction-to-the-python-pickle-module/) (external site)

Again, the first link didn’t have a lot, but it helped to understand fast the concept of pickling. Then the next link gives much more details and theory. I really liked it gave some explanations from a developer’s perspective.

## **Structured Error Demonstration Script**

I wanted to show in one script several aspects of error handling with the help of try-except block . My simple script that calculates the speed demonstrates catching several Specific exceptions and Custom errors.
Below is the simple code I wrote to test and find the name of errors that cause the program end abruptly:
```
print("You completed 100 miles race.")
distance = 100
time = int(input("Please enter your time in hours: "))
speed = 100/time
print("The speed is", str(speed),  "miles/hr")
```
In my script distance of the race = 100 miles. The program asks the user to enter time spent to finish the race in hours and then calculates the speed (speed =distance/time). And displays the result.
I identified 2 errors that could cause the error and the end of the program:
1. Division by zero (if the user enters 0 for time)
2. Unconvertible String to integer conversion (if the user enters types in “two” instead of “2” for time, it’s impossible to convert “two” to integer or float to perform calculations).

To handle these errors I applied try statement with an except clause. Here’s the one to handle the Structured Error Demonstration Script:
```
try:
    speed = 100/time
except ZeroDivisionError:
    print("You didn't race.")
else:
    print("The speed is", str(speed),  "miles/hr")
```
By using a try statement, I sectioned off the code that could potentially raise an exception. Then, I  wrote an except clause with a block of statements that are executed only if an exception is raised.
Since I specified the name of the error after try statement, this exception is only going to raise if the user enters ‘0’ for time. 
If the call to calculate speed raises an exception (as a result of the user entering 0 for time), the exception is caught and the user is informed that You didn't race. If no exception is raised, time string entered by the user converts to number and the program skips the except clause, continuing with the rest of the code.

![image](https://user-images.githubusercontent.com/79129459/109626686-b0664280-7af5-11eb-9bfc-5a471fb8bad0.png)

*Figure1. Code output when ZeroDivision Exception raised.*

Python allows to catch multiple exceptions with multiple except clauses. You can list as many except clauses as you like. So I added another one to catch the Value Error (in case the user enters unconvertible to integer string):
```
try:
        time = int(input("Please enter your time in hours: "))
        speed = round(100/time)
    except ZeroDivisionError:
        print("You didn’t race.")
    except ValueError:
        print("This was not a number.")
    else:
        print("The speed is", str(speed),  "miles/hr")
```
I also added a single else clause after my 2 except clauses in a try statement. The else block executes only if no exception is raised in the try block. So if none of the exceptions raised the user will see the message with the calculated speed.  
Python also allows to raise errors based on custom condition. I added demonstration of this to my script. My custom condition is that the time must be greater than 0 and less than 1:
```
time = float(strInput)
if 1 > time > 0 or time < 0:
    raise Exception('Time evolved should not be less than 1 hr')
speed = round(100/time)
except Exception as e:          #custom exception
    print('Seems like a wrong number. Try again.')
    print (e)
```
So for example if the user enters “-7” or “0.5” he’ll get  2 messages that something went wrong and that the time should not be less than 1 hour.

The final code to demonstrate Structured Error is below. I added while loop to allow user to test multiple exceptions without restarting the program.
```
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
        strInput = input("\n Please enter your time in hours or ‘exit’ to stop: ")
        if strInput == 'exit':
            break
        time = float(strInput)
        if 1 > time > 0 or time < 0:
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
```
The next Figure shows the code running in PyCharm:
![image](https://user-images.githubusercontent.com/79129459/109628036-228b5700-7af7-11eb-8008-14eb35c96847.png)

*Figure2. Output of Structured Error Demo script in PyCharm*


## **Pickling Demonstration Script**
This script demonstrates how to pickle, unpickle and rewrite pickled data. It also has the example of another option to handle multiple exception times by listing the in a single except clause. The script will allow the user to create a Birthday wihslist [], add some items to this list and then perform pickle features. 
My script will be pickling list [], but Python allows to pickle di
I import pickle module at the beginning: 



