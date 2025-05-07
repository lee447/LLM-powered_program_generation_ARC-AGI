def solve(grid):
    h=len(grid); w=len(grid[0])
    col_keep=[0]
    for j in range(1,w):
        col_j=[grid[i][j] for i in range(h)]
        col_j1=[grid[i][j-1] for i in range(h)]
        if col_j!=col_j1: col_keep.append(j)
    compressed_cols=[[row[j] for j in col_keep] for row in grid]
    result=[]
    for row in compressed_cols:
        if not result or row!=result[-1]:
            result.append(row)
    return result