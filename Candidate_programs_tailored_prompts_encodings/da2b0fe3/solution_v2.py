def solve(grid):
    h=len(grid); w=len(grid[0])
    minr=h; maxr=-1; minc=w; maxc=-1
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0:
                if i<minr: minr=i
                if i>maxr: maxr=i
                if j<minc: minc=j
                if j>maxc: maxc=j
    row_axis=(minr+maxr+1)//2
    if 0<=row_axis<h and all(grid[row_axis][j]==0 for j in range(w)):
        for j in range(w): grid[row_axis][j]=3
        return grid
    col_axis=(minc+maxc+1)//2
    if 0<=col_axis<w and all(grid[i][col_axis]==0 for i in range(h)):
        for i in range(h): grid[i][col_axis]=3
        return grid
    return grid