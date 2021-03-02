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

![Figure](https://github.com/i-zuzu/IntroToProg-Python-Mod07/blob/main/docs/Pic1.png)####


