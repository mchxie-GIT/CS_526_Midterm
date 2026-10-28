Problem 1: Snowfall

check_snowfall checks every three-day window. It subtracts the cumulative
total before the window from the total at its end. If twice this amount is
greater than the final total, it returns YES. Otherwise it returns NO.
Fewer than three days returns NO. The scan takes O(n) time.
main reads the input file and prints the input values with the answer.

With Python 3 installed, open a terminal in this folder and run:
python snowfall.py snowfall_input1.txt
python snowfall.py snowfall_input2.txt
python snowfall.py snowfall_input3.txt
python snowfall.py snowfall_input4.txt
python snowfall.py snowfall_input5.txt

Results, in order: YES, NO, NO, YES, YES.
