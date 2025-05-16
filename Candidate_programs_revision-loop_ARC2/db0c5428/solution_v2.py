def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import Counter
    cnt = Counter(c for row in grid for c in row)
    bg, _ = cnt.most_common(1)[0]
    # find central square
    top = next(r for r in range(h) if any(grid[r][c] != bg for c in range(w)))
    bottom = h-1 - next(r for r in range(h) if any(grid[h-1-r][c] != bg for c in range(w)))
    left = next(c for c in range(w) if any(grid[r][c] != bg for r in range(h)))
    right = w-1 - next(c for c in range(w) if any(grid[r][w-1-c] != bg for r in range(h)))
    size = bottom - top + 1
    bs = size // 3
    # extract 3x3 blocks
    blocks = [[ [ [ grid[top+i*bs+di][left+j*bs+dj] for dj in range(bs) ]
                  for di in range(bs) ]
                for j in range(3) ]
              for i in range(3)]
    # rotation helpers
    def rot90(b): return list(zip(*b[::-1]))
    def rot180(b): return [row[::-1] for row in b[::-1]]
    def rot270(b): return list(zip(*b))[::-1]
    # place blocks
    out = [row[:] for row in grid]
    tc_r, tc_c = top//bs+1, left//bs+1
    for di in (-1,0,1):
        for dj in (-1,0,1):
            if di==0 and dj==0: continue
            ti, tj = tc_r+2*di, tc_c+2*dj
            if not (0 <= ti < h//bs and 0 <= tj < w//bs): continue
            b = blocks[di+1][dj+1]
            if di and dj:
                b2 = rot180(b)
            elif di:
                b2 = rot90(b) if di>0 else rot270(b)
            else:
                b2 = rot270(b) if dj>0 else rot90(b)
            # write b2 into out
            r0, c0 = ti*bs, tj*bs
            for i in range(bs):
                for j in range(bs):
                    out[r0+i][c0+j] = b2[i][j]
    return out