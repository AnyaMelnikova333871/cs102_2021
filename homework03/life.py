import copy
import pathlib
import random
import typing as tp

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:

        cells = []
        x = cell[0]
        y = cell[1]
        if x - 1 >= 0:
            if y - 1 >= 0:
                cells.append(self.curr_generation[x - 1][y - 1])
            cells.append(self.curr_generation[x - 1][y])
            if y + 1 < self.cols:
                cells.append(self.curr_generation[x - 1][y + 1])
        if y - 1 >= 0:
            cells.append(self.curr_generation[x][y - 1])
        if y + 1 < self.cols:
            cells.append(self.curr_generation[x][y + 1])
        if x + 1 < self.rows:
            if y - 1 >= 0:
                cells.append(self.curr_generation[x + 1][y - 1])
            cells.append(self.curr_generation[x + 1][y])
            if y + 1 < self.cols:
                cells.append(self.curr_generation[x + 1][y + 1])
            print(cells)
        return cells

    def get_next_generation(self) -> Grid:
        nextgengrid = copy.deepcopy(self.curr_generation)
        for i in range(len(self.curr_generation)):
            for j in range(len(self.curr_generation[0])):
                sosedi = self.get_neighbours((i, j))
                if self.curr_generation[i][j] == 1:
                    if sosedi.count(1) == 3 or sosedi.count(1) == 2:
                        nextgengrid[i][j] = 1
                    else:
                        nextgengrid[i][j] = 0
                else:
                    if sosedi.count(1) == 3:
                        nextgengrid[i][j] = 1
                    else:
                        nextgengrid[i][j] = 0
        self.grid = nextgengrid
        return self.grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """

        self.prev_generation = copy.deepcopy(self.curr_generation)
        nextgen = self.get_next_generation()
        self.curr_generation = nextgen
        self.generations = self.generations + 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations and self.generations >= self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.prev_generation != self.curr_generation:
            return True
        else:
            return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, encoding="utf-8") as p:
            thegrid = [[int(cell) for cell in row.strip()] for row in p]
            gol = GameOfLife((len(thegrid), len(thegrid[0])))
            gol.curr_generation = thegrid
            return gol

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w", encoding="utf-8") as p:
            string = ""
            for i in range(len(self.curr_generation)):
                for j in range(len(self.curr_generation[0])):
                    string += str(self.curr_generation[i][j])
                    string += str("\n")
