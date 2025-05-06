def solve(grid):
    X=None
    for row in grid:
        for v in row:
            if v!=0:
                X=v
                break
        if X is not None:
            break
    m={3:1,5:4,8:2}
    N=m[X]
    return [[0 if v==X else N for v in row] for row in grid]