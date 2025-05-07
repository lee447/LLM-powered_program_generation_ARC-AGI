from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_rows = [i for i in range(H) if all(c == 0 for c in grid[i])]
    zero_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    row_blocks = [(zero_rows[i] + 1, zero_rows[i + 1]) for i in range(len(zero_rows) - 1) if zero_rows[i] + 1 < zero_rows[i + 1]]
    col_blocks = [(zero_cols[i] + 1, zero_cols[i + 1]) for i in range(len(zero_cols) - 1) if zero_cols[i] + 1 < zero_cols[i + 1]]
    blocks = []
    for bi, (rs, re) in enumerate(row_blocks):
        for bj, (cs, ce) in enumerate(col_blocks):
            cnt = sum(1 for r in range(rs, re) for c in range(cs, ce) if grid[r][c] == 2)
            blocks.append((bi, bj, cnt, rs, re, cs, ce))
    counts = sorted({b[2] for b in blocks}, reverse=True)
    out = [row[:] for row in grid]
    if sum(1 for b in blocks if b[2] == counts[0]) > 1:
        pals = [(bi, bj, rs, re, cs, ce) for bi, bj, cnt, rs, re, cs, ce in blocks if (bi + bj) % 2 == 1]
        pals.sort(key=lambda x: (x[0], x[1]))
        for i, (bi, bj, rs, re, cs, ce) in enumerate(pals):
            color = 8 if i < 2 else 3 if i == 2 else None
            if color is None:
                break
            for r in range(rs, re):
                for c in range(cs, ce):
                    if out[r][c] == 2:
                        out[r][c] = color
    else:
        max_cnt = counts[0]
        for bi, bj, cnt, rs, re, cs, ce in blocks:
            if cnt == max_cnt:
                for r in range(rs, re):
                    for c in range(cs, ce):
                        if out[r][c] == 2:
                            out[r][c] = 3
                break
        need = 2
        if len(counts) > 1:
            sc = counts[1]
            sec = [(bi, bj, rs, re, cs, ce) for bi, bj, cnt, rs, re, cs, ce in blocks if cnt == sc]
            sec.sort(key=lambda x: (x[1], x[0]))
            for bi, bj, rs, re, cs, ce in sec[:need]:
                for r in range(rs, re):
                    for c in range(cs, ce):
                        if out[r][c] == 2:
                            out[r][c] = 8
            need -= min(need, len(sec))
        if need > 0 and len(counts) > 2:
            tc = counts[2]
            thr = [(bi, bj, rs, re, cs, ce) for bi, bj, cnt, rs, re, cs, ce in blocks if cnt == tc]
            thr.sort(key=lambda x: (-x[1], x[0]))
            for bi, bj, rs, re, cs, ce in thr[:need]:
                for r in range(rs, re):
                    for c in range(cs, ce):
                        if out[r][c] == 2:
                            out[r][c] = 8
    return out