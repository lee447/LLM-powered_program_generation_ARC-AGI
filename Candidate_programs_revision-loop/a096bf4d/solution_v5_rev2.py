from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i in range(h) if all(v == 0 for v in grid[i])]
    sep_cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    is_sep_row = [i in sep_rows for i in range(h)]
    is_sep_col = [j in sep_cols for j in range(w)]
    block_rs = [i for i in range(h) if not is_sep_row[i] and (i == 0 or is_sep_row[i-1])]
    block_cs = [j for j in range(w) if not is_sep_col[j] and (j == 0 or is_sep_col[j-1])]
    if not block_rs or not block_cs:
        return grid
    kr, kc = block_rs[0], block_cs[0]
    sub = [grid[kr+1][kc+1], grid[kr+1][kc+2], grid[kr+2][kc+1], grid[kr+2][kc+2]]
    cnt = Counter(sub)
    maj = [c for c, n in cnt.items() if n == 3]
    if not maj:
        return grid
    newc = maj[0]
    for br in block_rs:
        for bc in block_cs:
            grid[br+1][bc+2] = newc
    return grid