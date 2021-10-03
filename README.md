# Election Analysis
Charlotte Uden
October 3, 2021

## Project Overview
This project aims to generate a vote count report for Colorado election data from PyPoll. Python version 3.7.6 was used for the analysis. PyPoll.py contains a script that records the total number of votes cast, the number of votes per candidate, the percentage of votes per candidate, and the winner based on popular vote. 
The results of this report are written to election_analysis.txt (found in the Resources directory). 

## Resources
Software: Python 3.6.7, Visual Studio Code, 1.38.1

In the Resources directory you can find:
- *election_results.csv:* dataset of vote data (Ballot ID, County, and Candidate)
- *election_analysis.txt*:

## Summary 
This analysis indicates that:

  - A total of 369,711 people voted in this election
  - The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
  -The candidate results were: 
      - Charles Casper Stockham: 23.0% (85,213)
      - Diana DeGette: 73.8% (272,892)
      - Raymon Anthony Doane: 3.1% (11,606)
   - The winner of the election was:
      - Diana DeGette who recieved 73.8% of the vote and 272,892 votes. 

## Challenge Overview
The election commision would like to know the turnout and percentage of voters for each county, as well as which county saw the largest turnout. An additional script, PyPoll_Challenge.py, was written (also using Python version 3.7.6) to find these results. 

## Challenge Summary
  * The total number of votes cast in this congressional election was 369,711.
  * Jefferson County received 10.5% of voters with a turnout of 38,855 people partaking in the election. Denver received 82.8% of the total, with 306,055 people partaking. Arapahoe County saw 6.7% of the votes with 24,801 people partaking. 
  * Denver county contains the largest number of voters. 
  * Three candidates ran for this election. Charles Casper Stockham received 23.0% of the vote (85,213 votes), Diana DeGette received 73.8% of the vote (272,892 votes), and Raymon Anthony Doane received 3.1% of the vote (11,606 votes).
  * Diana DeGette won the election with 73.8% of the vote and a total of 272,892 votes. 

## Election-Audit Summary
This analysis can be used to analyze election data from anywhere. However, this script requires that the file format be a CSV and that the dataset contain three columns (the columns must be in this order for the script to execute the analysis): 
  1. Ballot ID or some unique ID for each vote
  2. County or voting district, string
  3. Candidate name, string

The python script, PyPoll_Challenge.py, could be further modified to find the distribution of votes for each candidate for each county. For example, how are votes split by candidate in Denver? Alternatively, you could find the counties from which each candidate received votes. 
