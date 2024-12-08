# python_challenge
This Python project reads election results(pyPoll),and financial data(pyBank) from a CSV file, processes the data, and outputs the results in a formatted text file.

## Project Overview

The program is designed to:

1. **Read election data or financial data** from a CSV file containing candidate names, their percentage of votes, and the number of votes they received or dates, profit/lossess
2. **Process the data** by extracting relevant details (candidate names, vote percentages, total votes, dates, profit/losses).
3. **Output the election results** to a text file in a readable and structured format.

### Output CSV Format

The output txt file should have the following:

xXXXXX-Election Results
.........................
Total Votes: 369711
.........................
Charles Casper Stockham:  23.049%  (85213)
Diana DeGette:  73.812%  (272892)
Raymon Anthony Doane:  3.139%  (11606)
.........................
Winner: Diana DeGette
...............................

Financial Analysis
..................
Total Months: 86
Total: $22564198
Average Change: -8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)


- **Candidate Name**: Name of the candidate.
- **Percent Votes**: Percentage of total votes received by the candidate.
- **Number of Votes**: The actual number of votes received by the candidate.

- **Total months**: total months in the csv file
-**Total**: tottal money
-**Average Change**:sum of netchange/ len(netchnage)

### Output Text File Format

The election results are saved in the following format in the output text file:
Where each line contains:
- The candidate's name.
- The percentage of votes they received.
- The total number of votes they received.
- Who the winner is

## How It Works

1. **Read CSV File**: The program reads the election results from a CSV file using Python's built-in CSV module.
2. **Process Data**: The data is parsed, and for each candidate, the formatted result is generated.
3. **Write to Text File**: The results are written to a text file in a clean and structured format using Python's file handling methods.

## Requirements

- Python 3.x
- No external libraries required (Python's built-in libraries are sufficient).

## Installation

1. Clone or download the repository.
2. Place your election results CSV file in the same directory as the script.
3. Run the Python script.

## Usage

To execute the script:

1. Ensure you have the CSV file containing the election results (e.g., "election_data.csv" or "budget_data.csv").
2. Run the Python script:
3. run in an inetgrated terminal
  ```bash
4. python main.py
5. output to a txt.file 