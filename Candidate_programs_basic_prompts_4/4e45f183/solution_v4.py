def solve(grid):
    H, W = len(grid), len(grid[0])
    row_seps = [i for i in range(H) if all(v == 0 for v in grid[i])]
    col_seps = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    row_blocks = [(row_seps[i] + 1, row_seps[i+1] - row_seps[i] - 1) for i in range(len(row_seps)-1)]
    col_blocks = [(col_seps[j] + 1, col_seps[j+1] - col_seps[j] - 1) for j in range(len(col_seps)-1)]
    out = [row[:] for row in grid]
    for rb in row_blocks:
        r0, h = rb
        for cb_index in [0, 1, 2]:
            pass
        blocks = []
        counts = []
        for ci, (c0, w) in enumerate(col_blocks):
            blk = [grid[r][c0:c0+w] for r in range(r0, r0+h)]
            blocks.append(blk)
            freq = {}
            for row in blk:
                for v in row:
                    if v != 0:
                        freq[v] = freq.get(v, 0) + 1
            if freq:
                bg = max(freq, key=lambda k: freq[k])
                sec_count = sum(1 for row in blk for v in row if v != 0 and v != bg)
            else:
                sec_count = 0
            counts.append(sec_count)
        uniq = sorted(set(counts))
        if len(uniq) == 1:
            center_i = 0
            side_i = [1, 2]
        elif len(uniq) == 3:
            small, mid, large = uniq
            center_i = counts.index(large)
            side_i = [i for i in range(3) if counts[i] == mid]
        else:
            small, large = uniq
            if counts.count(large) == 1:
                center_i = counts.index(large)
                side_i = [i for i in range(3) if counts[i] == small]
            else:
                center_i = counts.index(small)
                side_i = [i for i in range(3) if counts[i] == large]
        side_i = sorted(side_i, key=lambda i: col_blocks[i][0], reverse=True)
        new_blocks = [None, blocks[center_i], None]
        if len(side_i) == 1:
            i0 = side_i[0]
            blk = blocks[i0]
            new_blocks[0] = blk
            new_blocks[2] = [row[::-1] for row in blk]
        else:
            new_blocks[0] = blocks[side_i[0]]
            new_blocks[2] = blocks[side_i[1]]
        for ci, (c0, w) in enumerate(col_blocks):
            blk = new_blocks[ci]
            for dr in range(h):
                for dc in range(w):
                    out[r0+dr][c0+dc] = blk[dr][dc]
    return out