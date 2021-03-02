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
I import pickle module at the beginning. Then the script offers the user Menu of choice to choose the pickling feature to test and manage the wishlist:
```
import pickle
while(True):
    print("""
    Menu of Options
    1) Show current wishlist (pickled data)
    2) Add new data to your wishlist (pickled list)
    3) Rewrite wishlist (current pickled data will be deleted)
    4) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
```

If the user chooses option 1 then the program opens binary "BirthdayWishList.dat" file and unpickles the data using function the load() function. Then it displays the content of the file to the user. I also called the exception to handle 2 types of error: FileNotFoundError (if program can’t find the file, it doesn’t exist) and EOFError (there’s no data in the file). These 2 errors are listed in a single except clause as a comma-separated group enclosed in a set of parentheses. If the program gets to one of these errors the message "You haven't pickled your Wishlist data yet." Will be displayed to the user.
Below is a piece of code to execute option 1:
```
if strChoice == '1':
    try:
        objFile = open("BirthdayWishList.dat", "rb")
        lstWishitem = pickle.load(objFile)
        print("Here's your current wishlist (unpickled): ")
        print(lstWishitem)
        objFile.close()
    except (FileNotFoundError, EOFError):  # exception in case the file with pickled data doesn't exist
        print("You haven't pickled your Wishlist data yet.")
        continue
```

Now let’s look at option 2 that allows user to add data to pickled list. First I open the binary file and load the data. Then I get the input from the user and add it to lstWishitem list [].  And the program adds this list to a binary file (pickles it) using dump() function. And I also added try – except statement to handle the exceptions.
Below is a piece of code to execute option 2:
```
elif strChoice == '2':
    strItem = input("Enter the wish item you want to add to your wishlist: ")
    try:
        objFile = open("BirthdayWishList.dat", "rb")
        lstWishitem = pickle.load(objFile)
        objFile.close()
    except ((FileNotFoundError, EOFError)): # exception in case there were no pickled data
        lstWishitem = []
        print("I created a list to add your desired gifts to it.")
    lstWishitem.append(strItem)
    objFile = open("BirthdayWishList.dat", "wb")
    pickle.dump(lstWishitem, objFile)
    objFile.close()
```
Now about Option 3 that allows to rewrite pickled data. 
If the user chooses Option 3, then the new binary file opened in write binary mode (“wb”).If the file exists, its content will be overwritten, if the file doesn’t exist it will be created. And the user can add data to the file using option 2 from the menu. Below is the piece of code for option 3:
```
elif strChoice == '3':
    objFile = open("BirthdayWishList.dat", "wb")
    objFile.close()
    print("You can start adding items to a new list. If you had the data in the file before, it is deleted. ")
```
Below is my Pickle Demonstration Script:
```
# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: This script demonstrates how Pickling works.
#              It allows you to create a list that contains gifts you'd like to receive
#              You can also pickle,unpickle and rewrite pickled data in your Birthday Wishlist.
#
# ChangeLog (Who,When,What):
# Irina Zubova,2-28-2020, Created the script
# ------------------------------------------------------------------------ #

import pickle

# -- Data -- #
# declare variables and constants
strChoice = "" # Captures the user option selection for menu options
objFile = "BirthdayWishlist.dat"   # An object that represents a file
lstWishitem = []
strYorN = "" # Captures the user option selection to exit or continue

print("\n Your birthday is coming up and you need to manage your wishlist.")

while(True):
    print("""
    Menu of Options
    1) Show current wishlist (pickled data)
    2) Add new data to your wishlist (pickled list)
    3) Rewrite wishlist (current pickled data will be deleted)
    4) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line for looks

# -- Input/Output and Processing -- #
    # 1.Unpickle and display data
    if strChoice == '1':
        try:
            objFile = open("BirthdayWishList.dat", "rb")
            lstWishitem = pickle.load(objFile)
            print("Here's your current wishlist (unpickled): ")
            print(lstWishitem)
            objFile.close()
        except (FileNotFoundError, EOFError):  # exception in case the file with pickled data doesn't exist
            print("You haven't pickled your Wishlist data yet.")
            continue

    # 2. Pickle the data
    elif strChoice == '2':
        strItem = input("Enter the wish item you want to add to your wishlist: ")
        try:
            objFile = open("BirthdayWishList.dat", "rb")
            lstWishitem = pickle.load(objFile)
            objFile.close()
        except ((FileNotFoundError, EOFError)): # exception in case there were no pickled data
            lstWishitem = []
            print("I created a list to add your desired gifts to it.")
        lstWishitem.append(strItem)
        objFile = open("BirthdayWishList.dat", "wb")
        pickle.dump(lstWishitem, objFile)
        objFile.close()

        print ("Item added")

    # 3. Rewrite Pickled data
    elif strChoice == '3':
        objFile = open("BirthdayWishList.dat", "wb")
        objFile.close()
        print("You can start adding items to a new list. If you had the data in the file before, it is deleted. ")

    # 4. Exit the Program
    elif strChoice == '4':
        strYorN = input("Are you sure you want to exit? [Y or N] ").upper()
        if strYorN == "Y":
            break  # and Exit the program
    else:
        print(strChoice, "is not in the Menu of Options.")
```
 The next picture shows pickling file running in Terminal and the binary file created.
 ![image](https://user-images.githubusercontent.com/79129459/109699479-7c1a7280-7b45-11eb-8a30-0f779e376091.png)

 *Figure3. Pickling demo script running in Terminal and binary file*

## Summary
In this assignment I practiced in creating and developing my own code. I learned and practiced how to save data to files through pickling and how to manage a pickled objects in a binary file. I got the knowledge on how to handle exceptions raised during the execution of a program and how to trap for specific exceptions and how to write code to deal with them. 






