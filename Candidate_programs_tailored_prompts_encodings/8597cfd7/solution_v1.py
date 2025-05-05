def solve(grid):
    red_col = next(c for row in grid for c,v in enumerate(row) if v==2)
    yellow_col = next(c for row in grid for c,v in enumerate(row) if v==4)
    red_count = sum(1 for row in grid if row[red_col]==2)
    yellow_count = sum(1 for row in grid if row[yellow_col]==4)
    winner = 2 if red_count>=yellow_count else 4
    return [[winner, winner], [winner, winner]]