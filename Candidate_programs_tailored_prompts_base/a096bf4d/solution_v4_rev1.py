from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    sep_rows = [i for i in range(R) if all(grid[i][j] == 0 for j in range(C))]
    sep_cols = [j for j in range(C) if all(grid[i][j] == 0 for i in range(R))]
    row_segments = [(sep_rows[i]+1, sep_rows[i+1]-1) for i in range(len(sep_rows)-1) if sep_rows[i]+1 <= sep_rows[i+1]-1]
    col_segments = [(sep_cols[j]+1, sep_cols[j+1]-1) for j in range(len(sep_cols)-1) if sep_cols[j]+1 <= sep_cols[j+1]-1]
    out = [row[:] for row in grid]
    for r0, r1 in row_segments:
        infos = []
        for c0, c1 in col_segments:
            counts = {}
            for i in range(r0, r1+1):
                for j in range(c0, c1+1):
                    v = grid[i][j]
                    counts[v] = counts.get(v, 0) + 1
            bg = max(counts.keys(), key=lambda k: counts[k])
            anoms = []
            ac = {}
            for i in range(r0, r1+1):
                for j in range(c0, c1+1):
                    v = grid[i][j]
                    if v != bg:
                        dr, dc = i-r0, j-c0
                        anoms.append((dr, dc, v))
                        ac[v] = ac.get(v, 0) + 1
            for dr, dc, v in anoms:
                if ac[v] == 1:
                    infos.append((dr, dc, v))
                    break
        val_counts = {}
        for _, _, v in infos:
            val_counts[v] = val_counts.get(v, 0) + 1
        mode = max(val_counts.keys(), key=lambda k: (val_counts[k], -k))
        dr0, dc0 = next((dr, dc) for dr, dc, v in infos if v == mode)
        for c0, c1 in col_segments:
            out[r0+dr0][c0+dc0] = mode
    return out