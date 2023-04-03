#!/usr/bin/env python3

from time import sleep

class Life:

    rules = {(1,2): 1, (1,3): 1, (0,3): 1,}
    mark = {0: "◻", 1: "◼"}

    def __init__(self, height=20, width=20, seconds=1):
        self.height = height
        self.width = width
        self.seconds = seconds
        self.grid = self._build()

    def _build(self):
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def seed(self, *vals):
        for v in vals:
            self.grid[v[0]][v[1]] = 1

    def count(self, row, col, amt=0):
        for delta_row in (self.height - 1, 0, 1):
            for delta_col in (self.width-1, 0, 1):
                if delta_row == 0 and delta_col == 0: continue
                n_row = (row+delta_row) % self.height
                n_col = (col+delta_col) % self.width
                amt += self.grid[n_row][n_col]
        return amt

    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                print(self.mark.get(self.grid[row][col]), end="")
            print()

    def next(self):
        frame = self._build()
        for row in range(self.height):
            for col in range(self.width):
                frame[row][col] = self.rules.get(\
                        (self.grid[row][col], self.count(row,col)),0)
        self.grid = frame

    def loop(self):
        while 1:
            try:
                print("\033[H \033[J")
                self.draw()
                self.next()
                sleep(self.seconds)
            except KeyboardInterrupt:
                exit()


if __name__ == "__main__":
    l = Life()

    l.seed( (1,1), (2,1), (3,1)  ) #line
    # w.seed( (0,1), (1,0), (2,0)  ) #broken line
    # w.seed( (0,0), (0,1), (1,0)  ) #l corner
    # w.seed( (0,2), (1,1), (2,0)  ) #r diag

    l.loop()
   
