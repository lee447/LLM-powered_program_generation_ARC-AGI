from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    main_vals = []
    for i in range(1, 5):
        for j in range(1, 5):
            v = grid[i][j]
            if v and v not in main_vals:
                main_vals.append(v)
    anchor_vals = []
    for i in range(1, 5):
        for j in range(5, 9):
            v = grid[i][j]
            if v and v not in anchor_vals:
                anchor_vals.append(v)
    if len(anchor_vals) >= 2 and len(main_vals) == 2:
        for i in range(1, 5):
            for j in range(1, 5):
                v = grid[i][j]
                k = 0 if v == main_vals[0] else 1
                res[i][j+4] = anchor_vals[k]
    # bottom quadrants
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if 1 <= i <= 8 and 1 <= j <= 8 and grid[i][j] and not (1 <= i <= 4 and 1 <= j <= 8) and not seen[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                comp = []
                while stack:
                    x,y = stack.pop()
                    if 0 <= x < h and 0 <= y < w and not seen[x][y] and grid[x][y] == col:
                        seen[x][y] = True
                        comp.append((x,y))
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            stack.append((x+dx,y+dy))
                if len(comp)>1:
                    comps.append(comp)
    mini = []
    if comps:
        comp = sorted(comps, key=lambda c: (min(x for x,y in c), min(y for x,y in c)))[0]
        for x,y in sorted(comp):
            v = grid[x][y]
            if v not in mini:
                mini.append(v)
    if mini:
        # choose colors for two blocks
        if len(mini) == 2:
            cA, cB = mini
            cC, cD = mini[1], mini[0]
        else:
            below = grid[5][4]
            cA, cB = below, mini[0]
            cC, cD = mini[1], mini[2]
        P = [[False]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                if (i+j)%2 == 0:
                    P[i][j] = True
        for bi in range(4):
            for bj in range(4):
                res[5+bi][1+bj] = cA if P[bi][bj] else cB
                res[5+bi][5+bj] = cC if P[bi][bj] else cD
    return res