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

print("\n Your birthday is coming soon and you need to manage your wishlist.")

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





