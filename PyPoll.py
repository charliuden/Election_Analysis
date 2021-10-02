#Charlotte Uden
#Module 3: PyPoll
#October 2 2021

#import the csv module
import csv
#import the os module -allows you to interact with the operating system
# and to access and open a file for which the direct path is unknown
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

