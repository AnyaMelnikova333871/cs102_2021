import random
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


homework04_new
def create_grid(rows: int = 15, cols: int = 15):

def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:



def remove_wall(
    grid: List[List[Union[str, int]]], coord: Tuple[int, int]
) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param coord:
    :return:
    """

    thechoice = ["up", "right"]
    i, j = coord[0], coord[1]
    route = random.choice(thechoice)
    if route == "up":
        if i != 1:
            grid[i - 1][j] = " "
        elif j + 2 != len(grid[0]):
            grid[i][j + 1] = " "
    else:
        if j + 2 != len(grid[0]):
            grid[i][j + 1] = " "
        elif i != 1:
            grid[i - 1][j] = " "
    return grid



def bin_tree_maze(
    rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:
    """
    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки


    for i in empty_cells:
        grid = remove_wall(grid, i)


    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """
    :param grid:
    :return:
    """

    pass


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param k:
    :return:
    """

    pass


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """
    :param grid:
    :param exit_coord:
    :return:
    """
    pass


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """
    :param grid:
    :param coord:
    :return:
    """

    pass


def solve_maze(

    grid,
):

    lnx = len(grid)
    lny = len(grid[0])
    coordinate = get_exits(grid)
    if len(coordinate) == 1:
        return grid, coordinate[0]
    if not encircled_exit(grid, coordinate[0]) and not encircled_exit(grid, coordinate[1]):
        for x in range(lnx):
            for y in range(lny):
                if grid[x][y] == " ":
                    grid[x][y] = 0
        grid[coordinate[0][0]][coordinate[0][1]] = 1
        grid[coordinate[1][0]][coordinate[1][1]] = 0
        m = 1
        while grid[coordinate[1][0]][coordinate[1][1]] == 0:
            grid = make_step(grid, m)
            m += 1
        route = shortest_path(grid, coordinate[1])
        for x in range(lnx):
            for y in range(lny):
                if grid[x][y] != " " and grid[x][y] != "■":
                    grid[x][y] = " "
        return grid, route
    return grid, None

  



def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
