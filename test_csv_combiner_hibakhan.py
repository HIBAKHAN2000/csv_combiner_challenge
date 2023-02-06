import sys
import os
import csv_combiner_hibakhan


if __name__ == "__main__":

    # TEST 1: NO ARGUEMENTS PASSED
    os.system("python csv_combiner_hibakhan.py > test_1.csv")

    # TEST 2: 1 ARGUEMENT PASSED
    os.system("python csv_combiner_hibakhan.py ex1.txt > test_2.csv")

    # TEST 3: 2 ARGUEMENTS PASSED
    os.system("python csv_combiner_hibakhan.py ex1.txt ex2.txt > test_3.csv")

    # TEST 4: 3 ARGUEMENTS PASSED
    os.system("python csv_combiner_hibakhan.py ex1.txt ex2.txt ex3.txt > test_4.csv")

    # TEST 5: 4 ARGUEMENTS PASSED
    os.system("python csv_combiner_hibakhan.py ex1.txt ex2.txt ex3.txt ex4.txt > test_5.csv")

    # TEST 6: FILES PASSED WITH UNEQUAL NUMBER OF COLUMNS
    os.system("python csv_combiner_hibakhan.py ex1.txt unequal-cols.txt > test_6.csv")

    # TEST 7: ARGUEMENT PASSED IS NOT A VALID FILE 
    os.system("python csv_combiner_hibakhan.py abc > test_7.csv")
  
    # TEST 8: USING CSV FILES PROVIDED BY PMG 
    os.system("python csv_combiner_hibakhan.py accessories.csv clothing.csv household_cleaners.csv > test_8.csv")