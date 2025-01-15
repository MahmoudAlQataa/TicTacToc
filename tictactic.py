class Player:
    def __int__(self):
        self.name = ""
        self.symbol = ""

    def chose_name(self):
        while True:
            name = input("Enter your name (letters only) : ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name use letters only")

    def chose_symbol(self):
        while True:
            symbol = input(self.name + "choose your symbol (a single letters) : ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol use a single letter")


class Menu:

    def disply_main_menu(self):
        print("Welcome to my TicTacToc")
        print("1- Start Game")
        print("2- Quit Game")
        choise = input("enter your choise : ")
        return choise

    def disply_end_menu(self):
        print("Game Over")
        print("1- Restart Game")
        print("2- Quit Game")
        choise = input("Enter your choise : ")
        return choise


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def disply_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            print("-------")

    def update_board(self, choice, symbole):
        if self.is_valid_choise(choice):
            self.board[choice - 1] = symbole
            return True
        return False

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

    def is_valid_choise(self, choice):
        return self.board[choice - 1].isdigit()


class Game:

    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.disply_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for index, player in enumerate(self.players, 1):
            print(f"Player {index} Enter your details")
            player.chose_name()
            player.chose_symbol()
            print("-" * 15)

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                self.board.disply_board()
                if self.check_win():
                    print(f"{self.players[1-self.current_player_index].name} wins")
                else:
                    print("It's a draw")
                choice = self.menu.disply_end_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.disply_board()
        print(f"{player.name}'s turn {player.symbol}")
        while True:
            try:
                cell_choicee = int(input("choose a cell {1-9} : "))
                if 1 <= cell_choicee <= 9 and self.board.update_board(cell_choicee, player.symbol):
                    break
                else:
                    print("Invalid choice, try again")
            except ValueError as e:
                print("please enter a number betwean 1 and 9 : ")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index


    def check_win(self):
        if self.board.board[0] == self.board.board[1] == self.board.board[2]:
            return True
        elif self.board.board[3] == self.board.board[4] == self.board.board[5]:
            return True
        elif self.board.board[6] == self.board.board[7] == self.board.board[8]:
            return True
        elif self.board.board[0] == self.board.board[3] == self.board.board[6]:
            return True
        elif self.board.board[1] == self.board.board[4] == self.board.board[7]:
            return True
        elif self.board.board[2] == self.board.board[5] == self.board.board[8]:
            return True
        elif self.board.board[0] == self.board.board[4] == self.board.board[8]:
            return True
        elif self.board.board[2] == self.board.board[4] == self.board.board[6]:
            return True
        else:
            return False


    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def quit_game(self):
        print("Thank you for playing")

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()


game: Game = Game()
game.start_game()
