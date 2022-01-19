import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border("|", "|", "-", "-", "+", "+", "+", "+")

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""

        thegrid = self.life.curr_generation
        for i in range(len(thegrid)):
            for j in range(len(thegrid[0])):
                if thegrid[i][j] == 0:
                    square = " "
                else:
                    square = "*"
                screen.addch(i + 1, j + 1, square)

    def run(self) -> None:
        screen = curses.initscr()
        curses.resizeterm(self.life.rows + 2, self.life.cols + 2)
        while self.life.is_changing and not self.life.is_max_generations_exceeded:
            self.life.step()
            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.refresh()
            curses.napms(5000)
        curses.endwin()


life = GameOfLife((24, 80), max_generations=50)
ui = Console(life)
ui.run()
