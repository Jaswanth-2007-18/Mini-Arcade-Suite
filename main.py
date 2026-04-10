import random


# Base Class
class Game:
    def play(self):
        pass


# Game 1: Guess the Number
class GuessNumber(Game):
    def play(self):
        number = random.randint(1, 100)
        print("\n Guess the number between 1 and 100")

        while True:
            try:
                guess = int(input("Enter your guess: "))

                if guess > number:
                    print("Too high!")
                elif guess < number:
                    print("Too low!")
                else:
                    print(" Correct! You win!")
                    break
            except ValueError:
                print("Please enter a valid number!")


#  Game 2: Tic-Tac-Toe
class TicTacToe(Game):
    def __init__(self):
        self.board = [" "] * 9

    def display(self):
        b = self.board
        print(f"""
 {b[0]} | {b[1]} | {b[2]}
-----------
 {b[3]} | {b[4]} | {b[5]}
-----------
 {b[6]} | {b[7]} | {b[8]}
""")

    def play(self):
        current = "X"

        for _ in range(9):
            self.display()
            move = int(input(f"Player {current}, choose position (1-9): ")) - 1

            if self.board[move] != " ":
                print("Invalid move! Try again.")
                continue

            self.board[move] = current

            if self.check_win(current):
                self.display()
                print(f" Player {current} wins!")
                return

            current = "O" if current == "X" else "X"

        self.display()
        print("It's a draw!")

    def check_win(self, p):
        b = self.board
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(b[i] == b[j] == b[k] == p for i, j, k in wins)


#  Game 3: Rock Paper Scissors
class RockPaperScissors(Game):
    def play(self):
        choices = ["rock", "paper", "scissors"]

        while True:
            user = input("\nEnter rock/paper/scissors (or 'q' to quit): ").lower()
            if user == 'q':
                break

            if user not in choices:
                print("Invalid choice!")
                continue

            comp = random.choice(choices)
            print("Computer:", comp)

            if user == comp:
                print("Draw!")
            elif (user == "rock" and comp == "scissors") or \
                    (user == "paper" and comp == "rock") or \
                    (user == "scissors" and comp == "paper"):
                print(" You win!")
            else:
                print("😢 You lose!")


#  Main Arcade Menu
def main():
    while True:
        print("\n======  MINI ARCADE ======")
        print("1. Guess Number")
        print("2. Tic-Tac-Toe")
        print("3. Rock Paper Scissors")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            game = GuessNumber()
        elif choice == "2":
            game = TicTacToe()
        elif choice == "3":
            game = RockPaperScissors()
        elif choice == "4":
            print(" Exiting... Bye bro!")
            break
        else:
            print("Invalid choice!")
            continue

        game.play()


# Run Program
if __name__ == "__main__":
    main()