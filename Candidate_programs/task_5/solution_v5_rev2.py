import numpy as np
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    arr = np.array(grid)
    h, w = arr.shape
    out = arr.copy()
    for r in range(h):
        row = arr[r]
        c = 0
        while c < w:
            if row[c] == 6:
                start = c
                while c < w and row[c] == 6:
                    c += 1
                end = c - 1
                segs = []
                i = 0
                while i < w:
                    if row[i] != 6:
                        j = i
                        while j+1 < w and row[j+1] == row[i]:
                            j += 1
                        segs.append((i, j, row[i]))
                        i = j+1
                    else:
                        i += 1
                best = max(segs, key=lambda x: x[1]-x[0]+1)
                col = best[2]
                out[r,start:end+1] = col
            else:
                c += 1
    return out.tolist()