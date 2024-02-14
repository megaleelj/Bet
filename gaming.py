import random

MAX_LINES = 5
MAX_BET= 50
MIN_BET = 0.5


ROWS = 5
COLS = 5

sym_cnt = {
    "A":5,
    "E":6,
    "G":3,
    "M":4,
    "4":7
}

sym_val = {
    "A":8,
    "E":3,
    "G":2,
    "M":4,
    "4":7
}

def check_wins(columns, lines, bet, val):
    wins = 0
    win_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            wins += val[symbol] * bet
            win_lines.append(line + 1)

    return wins, win_lines

    

def get_spin_machine(rows, cols, symbols):
    all_sym = []
    for symbol, sym_cnt in symbols.items():
        for _ in range(sym_cnt):
            all_sym.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_sym[:]
        for _ in range(rows):
            val = random.choice(current_symbols)
            current_symbols.remove(val)
            column.append(val)

        columns.append(column)
    return columns

def print_game(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row],  end=" | ")
        else:
            print(column[row], end="")
    
        print()
        




def deposit():
    while True:
        amount = input("how much do you want to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be above 0.")
        else:
            print("please enter a valid amount.")
        
    return amount

def get_line_numb():
    while True:
        lines = input("Eneter the the numbers of line you want to place your bet (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Eneter a valid number of line.")
        else:
            print("please enter a valid amount.")
        
    return lines

def get_bet():
    while True:
        amount = input("what will you like to bet? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be above £{MIN_BET} - £{MAX_BET}.")
        else:
            print("please enter a valid amount.")
        
    return amount

def game():
    global balance  
    lines = get_line_numb()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough money, your balance is £{balance}")
        else:
            break
    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to: £{total_bet}")

    slots = get_spin_machine(ROWS, COLS, sym_cnt)
    print_game(slots)
    wins, win_lines = check_wins(slots, lines, bet, sym_val)

    print(f"Won £{wins}.")
    if win_lines:
        print(f"You won on lines: {' '.join(map(str, win_lines))}")
    else:
        print("No winning lines.")

    balance += wins - total_bet 

def main():
    global balance 
    balance = deposit()
    
    while True:
        print(f"Balance is £{balance}")
        spin = input("Press enter to play. (s to quit).")
        if spin == "s":
            break
        game()

    print(f"Your remaining balance £{balance}")

if __name__ == "__main__":
    main()
