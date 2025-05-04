from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    zeros = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 0]
    def pick_shift(pos, dim):
        best = None
        for s in range(dim):
            shifted = [(p + s) % dim for p in pos]
            m = min(shifted)
            cnt = shifted.count(m)
            key = (m, -cnt)
            if best is None or key < best[0]:
                best = (key, s)
        return best[1]
    rows = [r for r, _ in zeros]
    cols = [c for _, c in zeros]
    vshift = pick_shift(rows, n)
    hshift = pick_shift(cols, n)
    out = [[None]*(2*n) for _ in range(2*n)]
    for bi in range(2):
        for bj in range(2):
            sr = vshift if bi else 0
            sc = hshift if bj else 0
            for r in range(n):
                for c in range(n):
                    vr = (r + sr) % n + bi*n
                    vc = (c + sc) % n + bj*n
                    out[vr][vc] = grid[r][c]
    return out