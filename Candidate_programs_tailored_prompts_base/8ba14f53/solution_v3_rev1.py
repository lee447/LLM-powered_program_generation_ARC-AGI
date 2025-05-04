from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_cols = [all(grid[r][c] == 0 for r in range(H)) for c in range(W)]
    regions = []
    c = 0
    while c < W:
        while c < W and zero_cols[c]:
            c += 1
        if c >= W:
            break
        start = c
        while c < W and not zero_cols[c]:
            c += 1
        regions.append((start, c))
    (a0, a1), (b0, b1) = regions[0], regions[1]
    rowsA = [r for r in range(H) if any(grid[r][c] != 0 for c in range(a0, a1))]
    rowsB = [r for r in range(H) if any(grid[r][c] != 0 for c in range(b0, b1))]
    A = [[grid[r][c] for c in range(a0, a1)] for r in rowsA]
    B = [[grid[r][c] for c in range(b0, b1)] for r in rowsB]
    Ah, Aw = len(A), len(A[0])
    Bh, Bw = len(B), len(B[0])
    def pick_A():
        if Ah > 3:
            r = next(r for r in rowsA if all(grid[r][c] != 0 for c in range(a0, a1)))
            out = [grid[r][c] for c in range(a0, min(a1, a0+3))]
        else:
            for row in A:
                if any(v == 0 for v in row):
                    out = row
                    break
            else:
                out = A[0]
        return out[:3] + [0] * max(0, 3 - len(out))
    def pick_B():
        for row in B:
            if all(v != 0 for v in row):
                out = row
                break
        else:
            out = B[-1]
        return out[:3] + [0] * max(0, 3 - len(out))
    topA = pick_A()
    midB = pick_B()
    if Bw > Aw:
        bot = midB
    elif Bw < Aw:
        bot = midB
    else:
        bot = [0, 0, 0]
    return [topA, midB, bot]