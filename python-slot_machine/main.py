import random

class SlotMachine:
    MAX_LINES = 3
    MAX_BET = 1000
    MIN_BET = 1
    ROWS = 3
    COLS = 3

    symbol_count = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8,
    }

    symbol_value = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2,
    }

    def __init__(self):
        self.balance = self.deposit()

    def deposit(self):
        while True:
            amount = input("What would you like to deposit? $")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    return amount
                else:
                    print("Amount must be greater than zero.")
            else:
                print("Please enter a valid amount.")

    def get_number_of_lines(self):
        while True:
            lines = input(f"Enter the number of lines to bet on (1-{self.MAX_LINES})? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= self.MAX_LINES:
                    return lines
                else:
                    print("Enter a valid amount of lines.")
            else:
                print("Please enter a number.")

    def get_bet(self):
        while True:
            amount = input("What would you like to bet on each line? $")
            if amount.isdigit():
                amount = int(amount)
                if self.MIN_BET <= amount <= self.MAX_BET:
                    return amount
                else:
                    print(f"Amount must be between ${self.MIN_BET} - ${self.MAX_BET}.")
            else:
                print("Please enter a valid amount.")

    def spin(self):
        lines = self.get_number_of_lines()
        while True:
            bet = self.get_bet()
            total_bet = bet * lines

            if total_bet > self.balance:
                print(f"You do not have enough to bet that amount, your current balance is: ${self.balance}")
            else:
                break

        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

        slots = self.get_slot_machine_spin(self.ROWS, self.COLS, self.symbol_count)
        self.print_slot_machines(slots)
        winnings, winning_lines = self.check_winnings(slots, lines, bet, self.symbol_value)
        print(f"You won ${winnings}.")
        print(f"You won on lines:", *winning_lines)
        return winnings - total_bet

    def play(self):
        while True:
            print(f"Current balance is ${self.balance}")
            answer = input("Press enter to play...(q to quit).")
            if answer == "q":
                break
            self.balance += self.spin()

        print(f"You left with ${self.balance}")

    @staticmethod
    def check_winnings(columns, lines, bet, values):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
        return winnings, winning_lines

    @staticmethod
    def get_slot_machine_spin(rows, cols, symbols):
        all_symbols = []
        for symbol, symbol_count in symbols.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)

        columns = []
        for _ in range(cols):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            columns.append(column)
        return columns

    @staticmethod
    def print_slot_machines(columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end=" | ")
                else:
                    print(column[row], end="")
            print()


def main():
    slot_machine = SlotMachine()
    slot_machine.play()

main()