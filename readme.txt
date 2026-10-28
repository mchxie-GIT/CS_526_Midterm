Problem 1: Snowfall

check_snowfall checks every three-day. It subtracts the cumulative
total before the window from the total at its end. If twice this amount is
greater than the final total, it returns YES. Otherwise it returns NO.
Fewer than three days returns NO.

Open a terminal in this folder and run:
python snowfall.py snowfall_input1.txt
python snowfall.py snowfall_input2.txt
python snowfall.py snowfall_input3.txt
python snowfall.py snowfall_input4.txt
python snowfall.py snowfall_input5.txt

Results, in order: YES, NO, NO, YES, YES.


Problem 2: Pandemic

The board uses 1 for infected and 0 for healthy. spread_infection checks
each healthy county's four possible neighbors. Counties with at least two
infected neighbors are collected in a list and updated after the full scan,
so all changes happen together. It repeats until no new infections heppen.
The main reads the starting counties and checks whether any 0 remains.

Open a terminal in this folder and run:
python pandemic.py pandemic_input1.txt
python pandemic.py pandemic_input2.txt

Input 1: There are healthy counties left
Input 2: There are no healthy counties left


Problem 3: Symbol Puzzle Game

is_valid uses a set to track symbols in each row, column, and square
sub-board. It returns False if a symbol repeats or isn't in the allowed
list. Empty cells (.) are skipped. If every check passes, it returns as True.
The main reads the comma-separated board and prints the result. The Checking all
cells takes O(n^2) time; the sub-board side length is sqrt(n).

Open a terminal in this folder and run:
python puzzle_game.py puzzle_game_input1.txt
python puzzle_game.py puzzle_game_input2.txt
python puzzle_game.py puzzle_game_input3.txt
python puzzle_game.py puzzle_game_input4.txt

Results, in order: valid, invalid, valid, invalid.
