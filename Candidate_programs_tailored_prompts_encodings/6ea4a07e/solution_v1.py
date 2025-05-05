def solve(grid):
    mapping={8:2,3:1,5:4}
    c=next((v for row in grid for v in row if v),None)
    fill=mapping[c]
    return [[0 if cell else fill for cell in row] for row in grid]