from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripe_row = None
    for r in range(h):
        row = grid[r]
        if any(cell > 1 for cell in row) and all(cell != 0 for cell in row):
            stripe_row = r
            break
    row = grid[stripe_row]
    L = next(i for i, cell in enumerate(row) if cell != 1)
    R = w - 1 - next(i for i, cell in enumerate(reversed(row)) if cell != 1)
    arr = row[L:R+1]
    def find_period(a):
        n = len(a)
        for p in range(1, n+1):
            if n % p: continue
            ok = True
            for i in range(n):
                if a[i] != a[i%p]:
                    ok = False
                    break
            if ok:
                return p
        return n
    p = find_period(arr)
    cycle = arr[:p]
    out = [r[:] for r in grid]
    for r in range(h):
        is_stripe = any(cell > 1 for cell in grid[r])
        for c in range(w):
            if out[r][c] == 0:
                if is_stripe and L <= c <= R:
                    out[r][c] = cycle[(c-L) % p]
                else:
                    out[r][c] = 1
    return out