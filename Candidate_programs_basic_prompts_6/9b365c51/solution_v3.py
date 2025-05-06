from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    left_colors = []
    seen = set()
    for c in range(w):
        for r in range(h):
            v = grid[r][c]
            if v != 0 and v != 8 and v not in seen:
                seen.add(v)
                left_colors.append((c, v))
                break
    left_colors.sort(key=lambda x: x[0])
    colors = [v for _, v in left_colors]
    comp_id = [[-1]*w for _ in range(h)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and comp_id[i][j] < 0:
                cid = len(comps)
                comps.append({'pixels': [], 'min_r': i, 'min_c': j})
                stack = [(i,j)]
                comp_id[i][j] = cid
                while stack:
                    r,c = stack.pop()
                    comps[cid]['pixels'].append((r,c))
                    if r < comps[cid]['min_r']: comps[cid]['min_r'] = r
                    if c < comps[cid]['min_c']: comps[cid]['min_c'] = c
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 8 and comp_id[nr][nc] < 0:
                            comp_id[nr][nc] = cid
                            stack.append((nr,nc))
    n = len(comps)
    cols = sorted([c['min_c'] for c in comps])
    med = cols[n//2]
    left_grp = [i for i,c in enumerate(comps) if c['min_c'] < med]
    right_grp = [i for i,c in enumerate(comps) if c['min_c'] >= med]
    left_grp.sort(key=lambda i: comps[i]['min_r'])
    right_grp.sort(key=lambda i: comps[i]['min_r'], reverse=True)
    order = left_grp + right_grp
    out = [[0]*w for _ in range(h)]
    for idx, col in zip(order, colors):
        for r,c in comps[idx]['pixels']:
            out[r][c] = col
    return out