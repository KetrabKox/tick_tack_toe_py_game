import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player = 'X'
        self.computer = 'O'
        self.winner = None
        
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
    
    def is_valid(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        elif self.board[row][col] != ' ':
            return False
        else:
            return True

    def is_full(self):
        for row in self.board:
            for col in row:
                if col == ' ':
                    return False
        return True

    def is_win(self, user):
        # check rows
        for row in self.board:
            if row.count(user) == 3:
                return True
        # check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == user:
                return True
        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == user:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == user:
            return True
        return False

    def is_tie(self):
        return self.is_full() and not self.is_win(self.player) and not self.is_win(self.computer)

    def is_over(self):
        return self.is_win(self.player) or self.is_win(self.computer) or self.is_tie()
    
    def who_start(self):
        if random.randint(0, 1) == 0:
            return 'gracz'
        else:
            return 'komputer'

    def another_game(self):
        ans=input('Czy chcesz zagrać ponownie? (t/n)\n')
        if ans.lower()=='t':
            return True
        else:
            return False
        
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
    game = TicTacToe()
    game.play()