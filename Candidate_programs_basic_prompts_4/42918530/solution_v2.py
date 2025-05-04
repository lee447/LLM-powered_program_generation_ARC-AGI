from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    patterns = {}
    for i in range(h - 4):
        for j in range(w - 4):
            c = grid[i][j]
            if c == 0: continue
            ok = True
            for k in range(5):
                if grid[i][j+k] != c or grid[i+4][j+k] != c or grid[i+k][j] != c or grid[i+k][j+4] != c:
                    ok = False
                    break
            if not ok: continue
            if c not in patterns:
                pat = [[0]*3 for _ in range(3)]
                for dy in range(1,4):
                    for dx in range(1,4):
                        pat[dy-1][dx-1] = 1 if grid[i+dy][j+dx] == c else 0
                patterns[c] = pat
            pat = patterns[c]
            for dy in range(1,4):
                for dx in range(1,4):
                    out[i+dy][j+dx] = c if pat[dy-1][dx-1] else 0
    return out