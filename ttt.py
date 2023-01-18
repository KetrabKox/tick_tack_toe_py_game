import random
from rules import Rules
class Game:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player = 'X'
        self.computer = 'O'
        self.winner = None
        self.rules = Rules(self.board, self.player, self.computer)
        
    def print_board(self):
        for row in self.board:
            print('|'.join(row))

    def is_valid(self, row, col):
        return self.rules.is_valid(row, col)

    def is_full(self):
        return self.rules.is_full()

    def is_win(self, user):
        return self.rules.is_win(user)

    def is_tie(self):
        return self.rules.is_tie()

    def is_over(self):
        return self.rules.is_over()
    
    def who_start(self):
        return self.rules.who_start()

    def another_game(self):
        return self.rules.another_game()
        
    def clear_board(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.winner = None

    def make_move(self, row, col):
        if self.is_valid(row, col):
            self.board[row][col] = self.player
            return True
        else:
            print('Nieprawidłowy ruch!\nSpróbuj ponownie.')
            return False

    def computer_move(self):
        if self.is_win(self.computer):
            return
        elif self.is_win(self.player):
            return
        elif self.is_full():
            return
        else:
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if self.is_valid(row, col):
                    self.board[row][col] = self.computer
                    break
        
    def play(self):
        print('Witaj w grze kółko i krzyżyk!')
        start=self.who_start()
        print(f'Zaczyna {start}!')
        if start == 'gracz':
            while not self.is_over():
                self.print_board()
                row = int(input('Wpisz wiersz: '))
                col = int(input('Wpisz kolumnę: '))
                move=self.make_move(row, col)
                if move:
                    self.computer_move()
        else:
            while not self.is_over():
                self.computer_move()
                if not self.is_over():
                    self.print_board()
                    row = int(input('Wpisz wiersz: '))
                    col = int(input('Wpisz kolumnę: '))
                    move=self.make_move(row, col)
                    while not move:
                        self.print_board()
                        row = int(input('Wpisz wiersz: '))
                        col = int(input('Wpisz kolumnę: '))
                        move=self.make_move(row, col)
        if self.is_win(self.player):
            print('Wygrałeś!')
        elif self.is_win(self.computer):
            print('Przegrałeś!')
        elif self.is_tie():
            print('Remis!')
        self.print_board()

        if self.another_game()==True:
            self.clear_board()
            self.play()
        else:
            print('Dziękujemy za grę!')

if __name__ == '__main__':
    game = Game()
    game.play()