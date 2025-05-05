from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    used = [[False]*w for _ in range(h)]
    
    def neigh(r, c):
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < h and 0 <= nc < w:
                yield nr, nc
                
    rects: List[Tuple[int,int,int,int]] = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not used[i][j]:
                stack = [(i, j)]
                used[i][j] = True
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for nr, nc in neigh(r, c):
                        if grid[nr][nc] == 5 and not used[nr][nc]:
                            used[nr][nc] = True
                            stack.append((nr, nc))
                rs = [r for r, _ in cells]
                cs = [c for _, c in cells]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                rects.append((r0, r1, c0, c1))
                
    out = [row[:] for row in grid]
    for r0, r1, c0, c1 in rects:
        length = (c1 - c0 + 1) + 1
        by = r0 - 1
        bx = c0 + (c1 - c0 + 1 - length)//2
        if by >= 0:
            for x in range(bx, bx + length):
                if 0 <= x < w:
                    out[by][x] = 2
    return out