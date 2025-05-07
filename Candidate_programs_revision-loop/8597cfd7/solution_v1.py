def solve(grid):
    stripe = next(i for i,row in enumerate(grid) if 5 in row)
    above = grid[:stripe]
    below = grid[stripe+1:]
    a2 = sum(cell==2 for row in above for cell in row)
    b2 = sum(cell==2 for row in below for cell in row)
    a4 = sum(cell==4 for row in above for cell in row)
    b4 = sum(cell==4 for row in below for cell in row)
    color = 2 if (b2-a2)>(b4-a4) else 4
    return [[color,color],[color,color]]