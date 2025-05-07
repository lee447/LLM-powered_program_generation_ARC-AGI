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
            cnt = sum(interior[i][j] == c for i in range(3) for j in range(3))
            if cnt == 9: continue
            row_counts = [sum(interior[i][j] == c for j in range(3)) for i in range(3)]
            col_counts = [sum(interior[i][j] == c for i in range(3)) for j in range(3)]
            rows_full = [i for i in range(3) if row_counts[i] >= 2]
            cols_full = [j for j in range(3) if col_counts[j] >= 2]
            if rows_full and cols_full:
                for i in rows_full:
                    for j in range(3):
                        res[r0 + 1 + i][c0 + 1 + j] = c
                for j in cols_full:
                    for i in range(3):
                        res[r0 + 1 + i][c0 + 1 + j] = c
            elif rows_full:
                i = rows_full[0]
                for j in range(3):
                    res[r0 + 1 + i][c0 + 1 + j] = c
            elif cols_full:
                j = cols_full[0]
                for i in range(3):
                    res[r0 + 1 + i][c0 + 1 + j] = c
    return res