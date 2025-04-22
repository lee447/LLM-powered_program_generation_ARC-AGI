def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i,row in enumerate(grid) if all(c==0 for c in row)]
    sep_cols = [j for j in range(w) if all(grid[i][j]==0 for i in range(h))]
    bands = [(sep_rows[i], sep_rows[i+1]) for i in range(len(sep_rows)-1) if sep_rows[i+1]-sep_rows[i]>1]
    colbands = [(sep_cols[j], sep_cols[j+1]) for j in range(len(sep_cols)-1) if sep_cols[j+1]-sep_cols[j]>1]
    out = [row[:] for row in grid]
    for br, er in bands:
        top = br+1; bot = er-1; H = bot-top+1
        for idx, (lc, rc) in enumerate(colbands):
            left = lc+1; right = rc-1; W = right-left+1
            c = grid[top][left-1]  # border color
            for dr in range(H-2):
                for dc in range(W-2):
                    r = top+1+dr; col = left+dc
                    if idx==0:
                        # cross
                        if dr==H//2 or dc==W//2:
                            out[r][col] = c
                    elif idx==1:
                        # vertical line
                        if dc==W//2:
                            out[r][col] = c
                    else:
                        # horizontal line
                        if dr==H//2:
                            out[r][col] = c
    return out