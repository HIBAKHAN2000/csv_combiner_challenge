# AUTHOR: Hiba Khan 
# Last Updated: 02-05-2023
# PMG CODING CHALLENGE - CSV FILE COMBINER

import sys
import pandas as pd
from pathlib import Path
 
def create_file_list(argv, list_of_files):
    # create list of file names needed to be combined 
 

    # create an iterator so we can skip the name of program on command line 
    iter_args = iter(argv)
    next(iter_args)

    # store list of file names needed to be combined 
    for x in iter_args:
            list_of_files.append(x)

# make sure the arguements provided are valid files
def check_args(argv, list_of_files):
    # check to make sure arguments are provided
    if len(list_of_files) == 0:
        print("ERROR: This program needs at least 1 file provided. Please try again!")
        exit()
    # check to make sure the arguements provided are files
    for file in list_of_files:
        if Path(file).is_file():
            continue
        else:
            print(file + " is not a valid file. Please try again with a valid file!")
            exit()
    
# Check to make sure the given files have same num of columns 
def check_columns(argv, list_of_files):
    # See how many rows are in the first file 
    # Open first file 
    cols_checker = pd.read_csv(list_of_files[0])
    # check how many rows the first file has
    cols_needed = len(cols_checker.axes[1])

    # compare the number of rows in each additional file to the first
    # if they are not all equal, throw error
    for curr_file in list_of_files:
        # Open current file 
        file_at_hand = pd.read_csv(curr_file)
        # check how many rows the current file has
        num_cols = len(file_at_hand.axes[1])
        # check if they number of rows are equal 
        if num_cols != cols_needed:
            print("ERROR: This program only supports files with the same number of columns. Please try again!")
            exit()

# function to combine the files 
def print_results(argv, list_of_files):
    # create flag to check if we are currently on first file for header purposes
    first_one = True
    # run through all files
    for curr_file in list_of_files:
        # Open current file 
        try:
            file_at_hand = open(curr_file, "r")
        except:
            print("Error opening file " +  curr_file +", please try again!")
            exit()
        # get them names of all the columns 
        headers = file_at_hand.readline()
        # print headers to output ONLY if its the first file 
        if first_one == True:
            print(headers.strip() + ", filename")
            # set to false so it won't print headers again
            first_one = False
        # read each line and print with file name appended in new column
        for line in file_at_hand:
            print(line.strip() + ", " + "\"" + curr_file + "\"")
        # when finished, close the file at hand 
        file_at_hand.close()

# call all functions in main for tester file purposes
def main(argv):
    list_of_files = []
    create_file_list(argv, list_of_files)
    check_args(argv, list_of_files)
    check_columns(argv, list_of_files)
    print_results(argv, list_of_files) 

if __name__ == "__main__":
    main(sys.argv)