def solve(grid):
    H, W = len(grid), len(grid[0])
    nonrows = [r for r in range(H) if any(grid[r][c] for c in range(W))]
    top, bot = min(nonrows), max(nonrows)
    barlen = max(sum(1 for c in range(W) if grid[r][c]) for r in nonrows)
    out = [[0]*W for _ in range(H)]
    for r in range(H):
        row = grid[r]
        cnt = sum(1 for v in row if v)
        if r==top or r==bot or cnt>=barlen:
            for c,v in enumerate(row):
                if v: out[r][c]=v
        else:
            k = r-(top+1)
            if k>=0 and k<bot-top-1 and k%2==0:
                d = -1 if k%4==0 else 1
                for c,v in enumerate(row):
                    if v: out[r][c+d]=v
            else:
                for c,v in enumerate(row):
                    if v: out[r][c]=v
    return out