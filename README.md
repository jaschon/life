# life
Quick Game of Life in Python

```
    l = Life(width=20, height=20, seconds=1)
    l.seed( (1,1), (2,1), (3,1)  ) #seed with a list of tuples (col [from top], row [left to right])
    l.loop()
```

## Example Shapes
```
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
    # l.seed( (5,6), (5,7), (6,5), (6,6), (7,6) ) #F pentomino
 ```
