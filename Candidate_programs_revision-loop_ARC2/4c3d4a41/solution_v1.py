def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    # find left 5-frame
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 5 and r+1<h and c+1<w and grid[r+1][c]==5 and grid[r][c+1]==5:
                top, left = r, c
                break
        else:
            continue
        break
    # find left mask bounds (4x7 block of zeros inside frame)
    r0, c0 = top+1, left+1
    # it's always 4 rows high and 7 cols wide
    H, W = 4, 7
    L = [[grid[r0+i][c0+j]==0 for j in range(W)] for i in range(H)]
    # find right 5-frame
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 5 and (c< w-1 and r< h-1 and grid[r][c+1]==5 and grid[r+1][c]==5):
                # check this is not left one
                if not (r==top and c==left):
                    top2, left2 = r, c
                    break
        else:
            continue
        break
    # find colored region in right frame
    cells = [(r,c) for r in range(h) for c in range(w) if grid[r][c] not in (0,5)]
    rmin = min(r for r,c in cells)
    rmax = max(r for r,c in cells)
    cmin = min(c for r,c in cells)
    cmax = max(c for r,c in cells)
    Hs, Ws = rmax-rmin+1, cmax-cmin+1
    # extract shape block
    S = [[grid[rmin+i][cmin+j] for j in range(Ws)] for i in range(Hs)]
    # rotate shape block 90° CW
    R = [[S[Hs-1-i][j] for i in range(Hs)] for j in range(Ws)]
    # clear old shape in right frame
    for i in range(top2+1, top2+1+Hs):
        for j in range(left2+1, left2+1+Ws):
            out[i][j] = 5
    # write rotated block
    for i in range(len(R)):
        for j in range(len(R[0])):
            if R[i][j] != 5:
                out[top2+1 + i][left2+1 + j] = R[i][j]
    return out