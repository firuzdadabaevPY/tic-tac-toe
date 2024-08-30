class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 12)

    def is_board_full(self):

        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False

    def check_win(self, player):

        for i in range(3):
            if (all(self.board[i][j] == player for j in range(3)) or
                    all(self.board[j][i] == player for j in range(3))):
                return True

            if (
                self.board[0][0] == self.board[1][1]
                == self.board[2][2] == player
                or
                self.board[2][0] == self.board[1][1]
                == self.board[0][2] == player
            ):
                return True
        return False

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
