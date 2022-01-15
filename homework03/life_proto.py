import copy
import typing as tp
from typing import Any, List

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    grid: List[List[Any]]

    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        # делаем гридушку
        self.grid = [[]]
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.draw_lines()

            # Отрисовка списка клеток

            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE
            self.get_next_generation()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.QUIT()

    def create_grid(self, randomize) -> Grid:

        """
        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """

        grid = []
        for i in range(self.cell_height):
            row = []
            for j in range(self.cell_width):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        grid = self.create_grid(self)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rect = (self.cell_size * j, self.cell_size * i, self.cell_size, self.cell_size)
                pygame.draw.rect(
                    self.screen,
                    pygame.Color("green") if self.grid[i][j] == 1 else pygame.Color("white"),
                    rect,
                )

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """

        cells = []
        x = cell[0]
        y = cell[1]
        if x - 1 >= 0:
            if y - 1 >= 0:
                cells.append(self.grid[x - 1][y - 1])
            cells.append(self.grid[x - 1][y])
            if y + 1 < self.cell_width:
                cells.append(self.grid[x - 1][y + 1])
        if y - 1 >= 0:
            cells.append(self.grid[x][y - 1])
        if y + 1 < self.cell_width:
            cells.append(self.grid[x][y + 1])
        if x + 1 < self.cell_height:
            if y - 1 >= 0:
                cells.append(self.grid[x + 1][y - 1])
            cells.append(self.grid[x + 1][y])
            if y + 1 < self.cell_width:
                cells.append(self.grid[x + 1][y + 1])
            print(cells)
        return cells

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """

        nextgengrid = copy.deepcopy(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                sosedi = self.get_neighbours((i, j))
                if self.grid[i][j] == 1:
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


from pprint import pprint as pp

game = GameOfLife(320, 240, 40, 1)

game.run()
