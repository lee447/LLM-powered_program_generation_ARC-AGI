from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    shape_map = {
        1: [(0,1,2,'g'),(-1,0,1,'e')],
        2: [(0,-1,3,'g'),(0,-1,1,'e')],
        3: [(1,0,2,'g'),(1,0,1,'e')],
        6: [(-1,0,5,'g'),(-1,0,1,'e')]
    }
    res = [[0]*w for _ in range(h)]
    pts = [(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] in shape_map]
    for r, c, col in pts:
        res[r][c] = col
        for dr, dc, steps, typ in shape_map[col]:
            for k in range(1, steps+1):
                nr, nc = r + dr*k, c + dc*k
                if not (0 <= nr < h and 0 <= nc < w):
                    break
                if typ == 'g':
                    if res[nr][nc] == 5:
                        res[nr][nc] = 4
                    elif res[nr][nc] == 0:
                        res[nr][nc] = 5
                else:
                    res[nr][nc] = col
    return res