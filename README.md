# Python Slot Machine (OOP)

This is a command-line based slot machine game implemented in Python using Object-Oriented Programming (OOP). The game is encapsulated in classes and methods, providing a clear structure and making the code more maintainable and reusable.

## Table of Contents

1. How to Play
2. Game Rules
3. Code Structure
4. Installation
5. Usage
6. Contributing

## How to Play

1. Run the script in your Python environment.
2. You will be prompted to deposit an amount of money to play.
3. You will then be asked to choose the number of lines to bet on (1-3).
4. Next, you will be asked to place a bet on each line. The bet amount must be between $1 and $1000.
5. The slot machine will spin, and the result will be printed on the console.
6. If the symbols on your bet lines match, you win! The amount you win depends on the symbol that matched.

## Game Rules

- The slot machine has 3 rows and 3 columns.
- There are 4 types of symbols: A, B, C, and D. The count of each symbol in the machine is 2, 4, 6, and 8 respectively.
- The value of each symbol is as follows: A = 5, B = 4, C = 3, D = 2. This value is multiplied by your bet to calculate your winnings.

## Code Structure

The code is structured into several classes and methods, each responsible for a specific part of the game:

- `check_winnings(columns, lines, bet, values)`: Checks the winnings for the current spin.
- `get_slot_machine_spin(rows, cols, symbols)`: Generates a random spin of the slot machine.
- `print_slot_machines(columns)`: Prints the current state of the slot machine.
- `deposit()`: Handles the player's deposit.
- `get_number_of_lines()`: Prompts the player to enter the number of lines to bet on.
- `get_bet()`: Prompts the player to enter their bet.
- `spin(balance)`: Executes a single spin of the slot machine.
- `main()`: The main game loop.

## Installation

To install the game, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/slot-machine.git
```

Then navigate to the directory and install the required packages:
```bash
cd slot-machine
pip install -r requirements.txt
```
## Usage

To start the game, run the following command in your terminal:
```bash
python main.py
```
## Contributing

Contributions are welcome! Please read the contributing guidelines before getting started.
