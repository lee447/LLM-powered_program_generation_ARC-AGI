from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    for r0 in range(1, h, 6):
        if r0 + 4 >= h: break
        for c0 in range(1, w, 6):
            if c0 + 4 >= w: break
            c = grid[r0][c0]
            interior = [[grid[r0 + 1 + i][c0 + 1 + j] for j in range(3)] for i in range(3)]
            cnt = sum(1 for i in range(3) for j in range(3) if interior[i][j] == c)
            if cnt <= 1 or cnt == 9:
                continue
            row_counts = [sum(1 for j in range(3) if interior[i][j] == c) for i in range(3)]
            col_counts = [sum(1 for i in range(3) if interior[i][j] == c) for j in range(3)]
            rows_full = [i for i in range(3) if row_counts[i] == 3]
            cols_full = [j for j in range(3) if col_counts[j] == 3]
            if rows_full and cols_full:
                ri = rows_full[0]
                cj = cols_full[0]
                for j in range(3):
                    res[r0 + 1 + ri][c0 + 1 + j] = c
                for i in range(3):
                    res[r0 + 1 + i][c0 + 1 + cj] = c
            elif rows_full:
                ri = rows_full[0]
                for j in range(3):
                    res[r0 + 1 + ri][c0 + 1 + j] = c
            elif cols_full:
                cj = cols_full[0]
                for i in range(3):
                    res[r0 + 1 + i][c0 + 1 + cj] = c
    return res