from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and not visited[rr][cc] and grid[rr][cc] != 0:
                            visited[rr][cc] = True
                            stack.append((rr,cc))
                rs = [r for r,_ in cells]
                cs = [c for _,c in cells]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                area = (maxr-minr+1)*(maxc-minc+1)
                comps.append((area, cells, minr, maxr, minc, maxc))
    comps.sort(key=lambda x: x[0], reverse=True)
    _, region_cells, minr, maxr, minc, maxc = comps[0]
    region_set = set(region_cells)
    mapping = {}
    for r in range(h):
        for c in range(w-1):
            if (r,c) not in region_set and (r,c+1) not in region_set:
                a, b = grid[r][c], grid[r][c+1]
                if a != 0 and b != 0:
                    mapping[b] = a
    out = []
    for r in range(minr, maxr+1):
        row = []
        for c in range(minc, maxc+1):
            v = grid[r][c]
            row.append(mapping.get(v, v))
        out.append(row)
    return out