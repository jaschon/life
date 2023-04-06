#!/usr/bin/env python3

from time import sleep

class Life:

    rules = {(1,2): 1, (1,3): 1, (0,3): 1,}
    mark = ("◻","◼")

    def __init__(self, size=20, sec=1):
        self.size = size
        self.sec = sec
        self.grid = self._build()

    def _build(self):
        return [[0 for _w in range(self.size)] for _h in range(self.size)]

    def seed(self, *vals):
        for v in vals:
            self.grid[v[0]][v[1]] = 1

    def count(self, row, col, amt=0):
        for delta_row in (self.size - 1, 0, 1):
            for delta_col in (self.size - 1, 0, 1):
                if delta_row == 0 and delta_col == 0: continue
                n_row = (row+delta_row) % self.size
                n_col = (col+delta_col) % self.size
                amt += self.grid[n_row][n_col]
        return amt

    def draw(self):
        for row in range(self.size):
            for col in range(self.size):
                print(self.mark[self.grid[row][col]], end="")
            print()

    def next(self):
        buf = self._build()
        for row in range(self.size):
            for col in range(self.size):
                buf[row][col] = self.rules.get((self.grid[row][col], self.count(row,col)),0)
        self.grid = buf

    def loop(self):
        while 1:
            try:
                print("\033[H \033[J")
                self.draw()
                self.next()
                sleep(self.sec)
            except KeyboardInterrupt:
                exit()


if __name__ == "__main__":
    l = Life()

    # l.seed( (1,1), (2,1), (3,1)  ) #line
    # l.seed( (4,1), (5,0), (6,0)  ) #broken line
    # l.seed( (0,0), (0,1), (1,0)  ) #l corner
    # l.seed( (0,2), (1,1), (2,0)  ) #r diag

    # l.seed( (4,5), (5,4), (5,5), (5,6) ) # tetris L
    # l.seed( (2,2), (2,3), (2,4), (3,2) ) #tetris T
    # l.seed( (2,2), (2,3), (2,4), (2,5) ) #tetris I
    # l.seed( (2,2), (2,3), (3,2), (3,3) ) #tetris O
    # l.seed( (2,2), (2,3), (2,4), (3,2) ) #tetris J

    # l.seed( (10,10), (10,11), (10,12), (11,10), (12,11) ) #glider
    l.seed( (5,6), (5,7), (6,5), (6,6), (7,6) ) #F pentomino

    l.loop()
   
