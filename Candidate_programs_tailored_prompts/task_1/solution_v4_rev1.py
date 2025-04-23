import numpy as np
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    runs = []
    for r in range(H):
        c = 0
        while c < W:
            v = grid[r][c]
            if v != 0:
                s = c
                while c < W and grid[r][c] == v:
                    c += 1
                runs.append((r, s, c - s, v))
            else:
                c += 1
    runs_set = set(runs)
    best = (0, 0, 0, 0, 0, 0, 0)
    for r, s, l, v in runs:
        for p in range(2, H):
            if (r + p, s, l, v) in runs_set:
                cnt = 1
                while (r + cnt * p, s, l, v) in runs_set:
                    cnt += 1
                if cnt >= 2:
                    key = (cnt, l, -r, p, r, s, v)
                    if key > best:
                        best = key
    cnt, l0, nr0, p, r0, s0, v0 = best
    anchor_rows = [r0 + k * p for k in range(cnt)]
    anchor_rows = [r for r in anchor_rows if r < H]
    anchor_first = True
    if anchor_rows:
        nr = anchor_rows[0]
        nr_next = nr + 1
        if nr_next >= H or any(grid[nr_next][c] == 0 for c in range(s0, s0 + l0)):
            anchor_first = False
    block_h = 1
    if anchor_rows:
        nr = anchor_rows[0]
        if anchor_first:
            while nr + block_h < H and grid[nr + block_h][s0] != 0:
                block_h += 1
        else:
            while nr - block_h >= 0 and grid[nr - block_h][s0] != 0:
                block_h += 1
    out = [[0]*W for _ in range(H)]
    segments = []
    if anchor_rows:
        nr = anchor_rows[0]
        dr = 1 if anchor_first else -1
        nr2 = nr + dr
        for s in range(0, W - l0 + 1):
            ok = True
            for c in range(s, s + l0):
                if nr2 < 0 or nr2 >= H or grid[nr][c] == 0 or grid[nr2][c] == 0:
                    ok = False
                    break
            if ok:
                segments.append(s)
    if anchor_rows:
        start0 = anchor_rows[0] if anchor_first else anchor_rows[0] - (block_h - 1)
        for k, ar in enumerate(anchor_rows):
            b0 = start0 + k * p
            for dr in range(block_h):
                r = b0 + dr
                if 0 <= r < H:
                    for s in segments:
                        for c in range(s, s + l0):
                            if 0 <= c < W and grid[r][c] != 0:
                                out[r][c] = grid[r][c]
    return out