from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    col = next((v for row in grid for v in row if v != 0), 0)
    seen = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == col and not seen[i][j]:
                pts = []
                stack = [(i,j)]
                seen[i][j] = True
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<R and 0<=ny<C and grid[nx][ny]==col and not seen[nx][ny]:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                hi, wi = r1-r0+1, c1-c0+1
                mask = [[False]*wi for _ in range(hi)]
                for x,y in pts:
                    mask[x-r0][y-c0] = True
                comps.append((hi,wi,mask))
    if not comps:
        return grid
    max_h = max(h for h,w,_ in comps)
    max_w = max(w for h,w,_ in comps)
    pads = []
    for h,w,mask in comps:
        tr = (max_h - h)//2; br = max_h - h - tr
        lc = (max_w - w)//2; rc = max_w - w - lc
        padded = [[False]*max_w for _ in range(tr)]
        for row in mask:
            padded.append([False]*lc + row + [False]*rc)
        padded += [[False]*max_w for _ in range(br)]
        pads.append(padded)
    mask_all = [[all(pads[k][i][j] for k in range(len(pads))) for j in range(max_w)] for i in range(max_h)]
    r0 = next(i for i in range(max_h) if any(mask_all[i]))
    r1 = max(i for i in range(max_h) if any(mask_all[i]))
    c0 = next(j for j in range(max_w) if any(mask_all[i][j] for i in range(max_h)))
    c1 = max(j for j in range(max_w) if any(mask_all[i][j] for i in range(max_h)))
    out = []
    for i in range(r0, r1+1):
        row = []
        for j in range(c0, c1+1):
            row.append(col if mask_all[i][j] else 0)
        out.append(row)
    return out