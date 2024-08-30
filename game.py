# Создать игровое поле - объект класса Board.
from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def save_result(text):
    with open('result.txt', 'a') as r:
        r.write(text + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    # Тут пользователь вводит координаты ячейки.
    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError

                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError

                if game.board[row][column] != ' ':
                    raise CellOccupiedError

            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )

                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break
        # В метод make_move передаются
        # те координаты, которые ввёл пользователь.
        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            print('Our winner: ', current_player)
            text_of_winner = f'Our winner is {current_player}'
            save_result(text_of_winner)
            running = False
        elif game.is_board_full():
            print('We do not have Winner YOOOOO: ')
            text_of_broth = 'Ничья!'
            save_result(text_of_broth)
            running = False
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
