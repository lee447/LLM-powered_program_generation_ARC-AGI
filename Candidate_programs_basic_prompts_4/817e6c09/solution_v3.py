def solve(grid):
    h=len(grid); w=len(grid[0])
    squares=[]
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                squares.append((r,c))
    cols={}
    for r,c in squares:
        cols.setdefault(c,[]).append(r)
    selected_cols=sorted(cols.keys(),reverse=True)
    to_color=set()
    for i,c in enumerate(selected_cols):
        if i%2==0:
            r=min(cols[c])
            to_color.add((r,c))
    res=[row[:] for row in grid]
    for r,c in to_color:
        res[r][c]=8; res[r][c+1]=8; res[r+1][c]=8; res[r+1][c+1]=8
    return res