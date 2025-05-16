from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    min_r, max_r, min_c, max_c = h, -1, w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] != bg:
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)
    if max_r < 0:
        return grid
    H, W = max_r - min_r + 1, max_c - min_c + 1
    def divisors(n):
        return [d for d in range(1, n+1) if n % d == 0]
    possible_r = [d for d in divisors(H) if d > 1 and H//d > 1 and (H//d) % 2 == 1]
    possible_c = [d for d in divisors(W) if d > 1 and W//d > 1 and (W//d) % 2 == 1]
    bs_r, bs_c = max(possible_r), max(possible_c)
    br, bc = H // bs_r, W // bs_c
    blocks = [[ [row[min_c + j*bs_c : min_c + (j+1)*bs_c] for row in grid[min_r + i*bs_r : min_r + (i+1)*bs_r]] for j in range(bc)] for i in range(br)]
    out = [row[:] for row in grid]
    for i in range(br):
        for j in range(bc):
            blk = blocks[i][j]
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = i + dr, j + dc
                    r0, c0 = min_r + nr*bs_r, min_c + nc*bs_c
                    newblk = blk
                    if dr != 0:
                        newblk = newblk[::-1]
                    if dc != 0:
                        newblk = [row[::-1] for row in newblk]
                    for bi in range(bs_r):
                        rr = r0 + bi
                        if not (0 <= rr < h):
                            continue
                        for bj in range(bs_c):
                            cc = c0 + bj
                            if not (0 <= cc < w):
                                continue
                            if grid[rr][cc] == bg:
                                out[rr][cc] = newblk[bi][bj]
    return out