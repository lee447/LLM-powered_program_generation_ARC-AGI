from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps_by_color = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v and not visited[r][c]:
                stack = [(r,c)]
                comp = []
                visited[r][c] = True
                while stack:
                    rr, cc = stack.pop()
                    comp.append((rr, cc))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == v:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                comps_by_color.setdefault(v, []).append(comp)
    info = {}
    for v, comps in comps_by_color.items():
        comps.sort(key=len)
        small, large = comps
        def mask_and_size(comp):
            rs = [rc[0] for rc in comp]
            cs = [rc[1] for rc in comp]
            r0, c0 = min(rs), min(cs)
            mask = [(r-r0, c-c0) for r,c in comp]
            h = max(r for r,c in mask) + 1
            w = max(c for r,c in mask) + 1
            return mask, h, w
        sm, sh, sw = mask_and_size(small)
        lm, lh, lw = mask_and_size(large)
        info[v] = {'small':(sm, sh, sw), 'large':(lm, lh, lw), 'sarea':len(small)}
    vs = list(info.keys())
    a, b = vs[0], vs[1]
    left_color, right_color = (a, b) if info[a]['sarea'] < info[b]['sarea'] else (b, a)
    slm, sh, sw = info[left_color]['small']
    llm, lh, lw = info[left_color]['large']
    rsm, rsh, rsw = info[right_color]['small']
    rlm, rlh, rlw = info[right_color]['large']
    maxw_left = max(sw, lw)
    maxw_right = max(rsw, rlw)
    cs_left = 0
    cs_right = maxw_left + 1
    out = [[0]*W for _ in range(H)]
    base_large_left = H - lh
    base_small_left = base_large_left - sh - 1
    for y, x in llm:
        out[base_large_left + y][cs_left + x] = left_color
    for y, x in slm:
        out[base_small_left + y][cs_left + x] = left_color
    base_large_right = H - rlh
    base_small_right = base_large_right - rsh - 1
    for y, x in rlm:
        out[base_large_right + y][cs_right + x] = right_color
    for y, x in rsm:
        out[base_small_right + y][cs_right + x] = right_color
    return out