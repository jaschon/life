#!/usr/bin/env python3

from time import sleep

class Life:

    rules = {(1,2): 1, (1,3): 1, (0,3): 1,}
    mark = ("◻","◼")

    def __init__(self, size=20, sec=1):
        """Init and set size, update time and build grid"""
        self.size = size
        self.sec = sec
        self.grid = self._build()

    def _build(self):
        """Build a blank grid size*size"""
        return [[0 for _w in range(self.size)] for _h in range(self.size)]

    def seed(self, *vals):
        """Mark a list of pairs (row from top, col from left)"""
        for v in vals:
            self.grid[v[0]][v[1]] = 1

    def count(self, row, col, amt=0):
        """Count the number of neighbors"""
        for delta_row in (self.size - 1, 0, 1):
            for delta_col in (self.size - 1, 0, 1):
                if delta_row == 0 and delta_col == 0: continue
                n_row = (row+delta_row) % self.size
                n_col = (col+delta_col) % self.size
                amt += self.grid[n_row][n_col]
        return amt

    def draw(self):
        """Output grid to screen"""
        for row in range(self.size):
            for col in range(self.size):
                print(self.mark[self.grid[row][col]], end="")
            print()

    def next(self):
        """Build next generation and swap current"""
        buf = self._build()
        for row in range(self.size):
            for col in range(self.size):
                buf[row][col] = self.rules.get((self.grid[row][col], self.count(row,col)),0)
        self.grid = buf

    def loop(self):
        """Loop animate"""
        while 1:
            try:
                print("\033[H \033[J")
                self.draw()
                self.next()
                sleep(self.sec)
            except KeyboardInterrupt:
                exit()


if __name__ == "__main__":
    pass
   
