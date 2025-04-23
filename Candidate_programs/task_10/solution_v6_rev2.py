from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 8]
    r0, r1 = min(r for r, _ in pts), max(r for r, _ in pts)
    c0, c1 = min(c for _, c in pts), max(c for _, c in pts)
    ph, pw = r1 - r0 + 1, c1 - c0 + 1
    pat = [[1 if grid[r0 + i][c0 + j] == 8 else 0 for j in range(pw)] for i in range(ph)]
    base = [[0 if grid[i][j] == 8 else grid[i][j] for j in range(W)] for i in range(H)]
    for i in range(H - ph + 1):
        for j in range(W - pw + 1):
            ok = True
            for di in range(ph):
                for dj in range(pw):
                    if pat[di][dj] == 1 and grid[i + di][j + dj] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                for di in range(ph):
                    for dj in range(pw):
                        if pat[di][dj] == 1:
                            base[i + di][j + dj] = 8
    return base