def solve(grid):
    H, W = len(grid), len(grid[0])
    bars = [c for c in range(W) if grid[0][c] != 0 and all(grid[r][c] != 0 for r in range(H))]
    palette = [grid[0][c] for c in bars]
    cols = sorted({c for r in range(H) for c in range(W) if grid[r][c] == 8})
    blocks = []
    for c in cols:
        if not blocks or c != blocks[-1][-1] + 1:
            blocks.append([c])
        else:
            blocks[-1].append(c)
    B, P = len(blocks), len(palette)
    out = [[0]*W for _ in range(H)]
    for j, blk in enumerate(blocks):
        if B > 1:
            idx = round(j*(P-1)/(B-1))
        else:
            idx = 0
        color = palette[idx]
        for r in range(H):
            for c in blk:
                if grid[r][c] == 8:
                    out[r][c] = color
    return out