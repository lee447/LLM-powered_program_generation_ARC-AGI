from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_rows = [i for i in range(H) if all(c == 0 for c in grid[i])]
    row_blocks = [(zero_rows[i] + 1, zero_rows[i + 1]) for i in range(len(zero_rows) - 1) if zero_rows[i] + 1 < zero_rows[i + 1]]
    zero_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    col_blocks = [(zero_cols[i] + 1, zero_cols[i + 1]) for i in range(len(zero_cols) - 1) if zero_cols[i] + 1 < zero_cols[i + 1]]
    blocks = []
    for bi, (rs, re) in enumerate(row_blocks):
        for bj, (cs, ce) in enumerate(col_blocks):
            cnt = 0
            for r in range(rs, re):
                for c in range(cs, ce):
                    if grid[r][c] == 2:
                        cnt += 1
            blocks.append((bi, bj, cnt, rs, re, cs, ce))
    counts = sorted({b[2] for b in blocks}, reverse=True)
    out = [row[:] for row in grid]
    n8 = 2
    if len([b for b in blocks if b[2] == counts[0]]) > 1:
        # fallback parity rule when no unique max
        pals = [(bi, bj) for bi, bj, cnt, *rest in blocks if (bi + bj) % 2 == 1]
        pals.sort()
        for i, (bi, bj) in enumerate(pals):
            color = 8 if i < 2 else 3 if i == 2 else None
            if color is None:
                break
            rs, re = row_blocks[bi]
            cs, ce = col_blocks[bj]
            for r in range(rs, re):
                for c in range(cs, ce):
                    if out[r][c] == 2:
                        out[r][c] = color
    else:
        # main rule: unique max -> color3; then two next-highest ->8
        # color3
        max_cnt = counts[0]
        for bi, bj, cnt, rs, re, cs, ce in blocks:
            if cnt == max_cnt:
                for r in range(rs, re):
                    for c in range(cs, ce):
                        if out[r][c] == 2:
                            out[r][c] = 3
                break
        # color8
        need = 2
        # second-highest
        if len(counts) > 1:
            sc = counts[1]
            sec = [(bi, bj) for bi, bj, cnt, *rest in blocks if cnt == sc]
            sec.sort(key=lambda x: (x[1], x[0]))
            use = sec[:need]
            for bi, bj in use:
                rs, re = row_blocks[bi]
                cs, ce = col_blocks[bj]
                for r in range(rs, re):
                    for c in range(cs, ce):
                        if out[r][c] == 2:
                            out[r][c] = 8
            need -= len(use)
        # if still need, take from third-highest
        if need > 0 and len(counts) > 2:
            tc = counts[2]
            thr = [(bi, bj) for bi, bj, cnt, *rest in blocks if cnt == tc]
            thr.sort(key=lambda x: (-x[1], x[0]))
            use = thr[:need]
            for bi, bj in use:
                rs, re = row_blocks[bi]
                cs, ce = col_blocks[bj]
                for r in range(rs, re):
                    for c in range(cs, ce):
                        if out[r][c] == 2:
                            out[r][c] = 8
    return out