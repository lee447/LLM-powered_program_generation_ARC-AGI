def solve(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    sep = [i for i in range(h) if all(v==0 for v in grid[i])]
    for bi in range(len(sep)-1):
        top, bot = sep[bi], sep[bi+1]
        if bot-top<6: continue
        r0 = top+1
        row0 = grid[r0]
        runs = []
        in_run = False
        for c in range(w):
            if row0[c]!=0 and not in_run:
                start = c; in_run = True
            if (row0[c]==0 or c==w-1) and in_run:
                end = c-1 if row0[c]==0 else c
                runs.append((start,end))
                in_run = False
        for idx,(c0,_) in enumerate(runs):
            color = grid[r0][c0]
            for dr in range(3):
                for dc in range(3):
                    rr, cc = r0+1+dr, c0+1+dc
                    if idx==0 and not (dr==1 or dc==1): continue
                    if idx==1: continue
                    out[rr][cc] = color
    return out