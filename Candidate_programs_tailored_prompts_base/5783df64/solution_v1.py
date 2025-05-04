def solve(grid):
    n=len(grid)
    h=n//3
    out=[]
    for b in range(3):
        cells=[]
        for i in range(b*h,(b+1)*h):
            for j,v in enumerate(grid[i]):
                if v:
                    cells.append((j,v))
        cells.sort(key=lambda x:x[0])
        out.append([v for _,v in cells])
    return out