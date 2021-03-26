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
source_dir = input("What is your staring directory?: ")
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
#elif("n"):
    num = input("How many files would you like to move?: ")
    exit(0)
