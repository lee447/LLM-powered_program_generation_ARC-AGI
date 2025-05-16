from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0])
    centers_by_row = {}
    for r in range(H):
        row = grid[r]
        c = 0
        centers = []
        while c < W:
            if row[c] == 7:
                start = c
                while c < W and row[c] == 7:
                    c += 1
                end = c - 1
                centers.append((start + end) // 2)
            else:
                c += 1
        if centers:
            centers_by_row[r] = centers
    out = [[0] * W for _ in range(H)]
    for r in range(H):
        if r in centers_by_row:
            centers = set(centers_by_row[r])
            for c in range(W):
                if grid[r][c] == 0:
                    out[r][c] = 0
                elif c in centers:
                    out[r][c] = 6
                else:
                    out[r][c] = 8
        else:
            centers = set()
            if r - 1 in centers_by_row:
                centers |= set(centers_by_row[r - 1])
            if r + 1 in centers_by_row:
                centers |= set(centers_by_row[r + 1])
            for c in range(W):
                if grid[r][c] == 0:
                    out[r][c] = 0
                elif c in centers:
                    out[r][c] = 6
                else:
                    out[r][c] = 8
    return out