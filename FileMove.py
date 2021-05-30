import shutil
import os

##
# @Author: Ed Ardolino
# @Version 1.0
# @Creation Date: 3-26-2021
##

##
#
# Python program to move files from one specified location to another specified location
#
##

# User enters the source directory 
source_dir = input("What is your source directory?: ")
# User enters the target directory
target_dir = input("What is your end directory?: ")
# User is asked if they would like to move all of the files in the directory
# If yes, all the files will be moved
# If no, the user will be asked how many files they would like to be moved (Currently a work in progress)
move_all = input("Do you want to move all the files from this directory? (y/n): ")
if move_all == ("y"):

    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
    print("In progress")
    print("Done")
    exit(0)
# Work in progress
elif("n"):
    # Prints a list of all of the current folders/files in the source directory
    print(os.listdir(source_dir))
    # num takes the input for how many files the user would like to move
    num = input("How many files would you like to move?: ")
    if num == ('all'):
        print("Why didnt you say yes in the first place dumbass?")
        exit(0)
    # numExact asks the user which files they would like to move to the target directory
    numExact = input("Which files would you like to move?: ")
    exit(0)
