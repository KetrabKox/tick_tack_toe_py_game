import random

class Rules:
    def __init__(self, board, player, computer):
        self.board = board
        self.player = player
        self.computer = computer
        self.winner = None

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