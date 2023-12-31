import random

MAX_LINES = 3
MAX_BET = 100
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
            winnings = +values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)
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


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a number greater than zero.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"How many lines would you like to play? (1-{MAX_LINES}) : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and", MAX_LINES)
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        bet = input(
            f"How much would you like to bet on each line? (${MIN_BET}-${MAX_BET}) : $"
        )
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a number between $ {MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet


def spin(balance):
    lines = get_number_of_lines()
    print(f"You have ${balance} and are playing {lines} lines.")
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You don't have enough money to bet ${bet} on each of {lines} lines for a total bet of ${total_bet}."
            )
            continue
        else:
            print(
                f"Yo are betting ${bet} on each of {lines} lines for a total bet of ${total_bet}"
            )
            break

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings} on lines ", *winning_lines, sep=", ")
    return winnings - total_bet


def main():
    print("Welcome to the Slot Machine!")
    print("You have $0 and are playing 1 line.")
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Would you like to play? (y/n) : ")
        if answer.lower() == "n":
            break
        balance += spin(balance)

    print(f"Thank you for playing. Your final balance is ${balance}.")


main()
