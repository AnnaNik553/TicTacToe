from random import randint

class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 'x'  # крестик (игрок - человек)
    COMPUTER_O = 'o'  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def __check_index(self, index):
        r, c = index
        if type(r) != int or type(c) != int or not (0 <= r <= 2) or not (0 <= c <= 2):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        r, c = key
        self.pole[r][c].value = value

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def show(self):
        for row in self.pole:
            for cell in row:
                print(cell.value, end=' ')
            print()
        print('-' * 10)

    def human_go(self):
        inp = input('Введите координаты свободной клетки через пробел (отсчет с нуля (0 1)): ')
        r, c = map(int, inp.split())
        if self.pole[r][c]:
            self[r, c] = self.HUMAN_X
        else:
            print('Эта клетка занята, ставить крестик можно только в пустую клетку')

    def computer_go(self):
        print('Ход компьютера')
        while True:
            rand_r = randint(0, 2)
            rand_c = randint(0, 2)
            if self.pole[rand_r][rand_c]:
                break
        self[rand_r, rand_c] = self.COMPUTER_O

    def _get_combination(self):
        return tuple(tuple(x.value for x in row) for row in self.pole) +\
               tuple(tuple(self.pole[i][j].value for i in range(3)) for j in range(3)) +\
            tuple(tuple(self.pole[i][i].value for i in range(3)) for _ in range(1)) +\
               tuple((self.pole[0][2].value, self.pole[1][1].value, self.pole[2][0].value)for _ in range(1))

    @property
    def is_human_win(self):
        win = ('x', 'x', 'x')
        comb = self._get_combination()
        return win in comb

    @property
    def is_computer_win(self):
        win = ('o', 'o', 'o')
        comb = self._get_combination()
        return win in comb

    @property
    def is_draw(self):
        return not any(map(lambda x: bool(x), (cell for row in self.pole for cell in row)))

    def __bool__(self):
        return not self.is_computer_win and not self.is_human_win and not self.is_draw


class Cell:
    def __init__(self):
        self.value = '-'

    def __bool__(self):
        return self.value == '-'


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")