from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    coords = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 8]
    if not coords:
        return []
    rs = [i for i, j in coords]
    cs = [j for i, j in coords]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    bh, bw = r1 - r0 + 1, c1 - c0 + 1
    best, best_sum = None, -1
    for i in range(h - bh + 1):
        for j in range(w - bw + 1):
            s = 0
            ok = True
            for di in range(bh):
                row = grid[i + di]
                for dj in range(bw):
                    v = row[j + dj]
                    if v == 8:
                        ok = False
                        break
                    s += v
                if not ok:
                    break
            if ok and s > best_sum:
                best_sum = s
                best = [grid[i + di][j:j + bw] for di in range(bh)]
    return best