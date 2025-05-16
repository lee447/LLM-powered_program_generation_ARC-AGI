from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    c = next(color for row in grid for color in row if color not in (0,7))
    cells = [(i,j) for i,row in enumerate(grid) for j,v in enumerate(row) if v==c]
    center = None
    for i,j in cells:
        neigh4 = sum((i+di,j+dj) in cells for di,dj in ((1,0),(-1,0),(0,1),(0,-1)))
        diag4 = sum((i+di,j+dj) in cells for di,dj in ((1,1),(1,-1),(-1,1),(-1,-1)))
        if neigh4==4 or diag4==4:
            center = (i,j); break
    is_x = sum((center[0]+di,center[1]+dj) in cells for di,dj in ((1,1),(1,-1),(-1,1),(-1,-1)))==4
    inner = [row[1:-1] for row in grid[1:-1]]
    m = len(inner)
    ts = m
    R = m*ts
    out = [[0]*R for _ in range(R)]
    for bi in range(m):
        for bj in range(m):
            col = inner[bi][bj]
            for di in range(ts):
                for dj in range(ts):
                    i = bi*ts+di; j = bj*ts+dj
                    if col==7:
                        if is_x:
                            out[i][j] = 7 if (di==dj or di+dj==ts-1) else 0
                        else:
                            out[i][j] = 7 if (1<=di<ts-1 and 1<=dj<ts-1) else 0
                    else:
                        if is_x:
                            out[i][j] = 9 if (di==dj or di+dj==ts-1) else 7
                        else:
                            out[i][j] = 9 if (1<=di<ts-1 and 1<=dj<ts-1) else 7
    return out