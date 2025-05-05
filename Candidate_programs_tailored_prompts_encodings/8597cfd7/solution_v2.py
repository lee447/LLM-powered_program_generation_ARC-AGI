def solve(grid):
    rows=len(grid)
    cols=len(grid[0])
    grey_row=None
    cols2=set()
    cols4=set()
    for i,row in enumerate(grid):
        if all(v==5 for v in row):
            grey_row=i
        for j,v in enumerate(row):
            if v==2: cols2.add(j)
            elif v==4: cols4.add(j)
    col2=next(iter(cols2))
    col4=next(iter(cols4))
    red_count=sum(1 for i in range(rows) if grid[i][col2]==2)
    yellow_count=sum(1 for i in range(rows) if grid[i][col4]==4)
    c=2 if red_count>=yellow_count else 4
    return [[c,c],[c,c]]