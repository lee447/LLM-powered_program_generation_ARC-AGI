def solve(grid):
    n, m = len(grid), len(grid[0])
    seen = [[False]*m for _ in range(n)]
    comps = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and not seen[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0<=rr<n and 0<=cc<m and not seen[rr][cc] and grid[rr][cc]!=0:
                            seen[rr][cc] = True
                            stack.append((rr,cc))
                minr = min(r for r,c in cells)
                maxr = max(r for r,c in cells)
                minc = min(c for r,c in cells)
                maxc = max(c for r,c in cells)
                pat = [[0]*3 for _ in range(3)]
                for r,c in cells:
                    rr = round((r-minr)*2/(maxr-minr)) if maxr>minr else 1
                    cc = round((c-minc)*2/(maxc-minc)) if maxc>minc else 1
                    pat[rr][cc] = grid[r][c]
                rc = (minr+maxr)/2
                cc = (minc+maxc)/2
                br = 0 if rc < n/2 else 1
                bc = 0 if cc < m/2 else 1
                comps.append((br,bc,pat))
    out = [[0]*6 for _ in range(6)]
    for br,bc,pat in comps:
        ro,co = br*3, bc*3
        for i in range(3):
            for j in range(3):
                if pat[i][j]:
                    out[ro+i][co+j] = pat[i][j]
    return out