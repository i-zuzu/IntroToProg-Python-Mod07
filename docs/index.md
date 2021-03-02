### **Irina Zubova**
### **March 1, 2021**
### **Foundations of Programming: Python**
### **Assignment 07**
### https://github.com/i-zuzu/IntroToProg-Python-Mod07




#                                                     **Exception Handling and Pickling in Python**


## **Introduction**
This page describes how I worked on Assignment07. It has some links from the web that describe how Pickling and Exception Handling work in Python. There will be 2 scripts that demonstrate how Pickling and Structured error handling work and explain what these scripts do.

## **Web Research on Exception Handling and Python**

For Exception handling I found the following webpages really helpful:
- [https://www.w3schools.com/python/python_try_except.asp] (external site)
- (https://www.freecodecamp.org/news/exception-handling-python/) (external site)
- (https://www.tutorialspoint.com/python/python_exceptions.htm) (external site)

The first one is relatively short, it has many examples that helped me to understand how Exception works. I like starting from short, simple explanations and then build up more content on them. Then the next 2 links provide more details and descriptions. They outline at the beginning what they cover, also the third one has behind the scene diagrams showing how the program works. 

For Pickling I found these webpages really valuable:
*	(https://www.pitt.edu/~naraehan/python3/pickling.html) (external site)
*	(https://stackabuse.com/introduction-to-the-python-pickle-module/) (external site)

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

