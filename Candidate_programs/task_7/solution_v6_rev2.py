from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    visited = [[False] * W for _ in range(H)]
    comps_by_color = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0 and not visited[r][c]:
                stack = [(r, c)]
                visited[r][c] = True
                comp = []
                while stack:
                    rr, cc = stack.pop()
                    comp.append((rr, cc))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = rr + dr, cc + dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == v:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                comps_by_color.setdefault(v, []).append(comp)
    info = {}
    for v, comps in comps_by_color.items():
        comps_sorted = sorted(comps, key=lambda c: len(c), reverse=True)
        large, small = comps_sorted[0], comps_sorted[1]
        def mask_and_size(comp):
            rs = [r for r, c in comp]
            cs = [c for r, c in comp]
            r0, c0 = min(rs), min(cs)
            mask = [(r - r0, c - c0) for r, c in comp]
            h = max(r for r, c in mask) + 1
            w = max(c for r, c in mask) + 1
            return mask, h, w, c0
        lm, lh, lw, lminc = mask_and_size(large)
        sm, sh, sw, _ = mask_and_size(small)
        large_avg = sum(r for r, c in large) / len(large)
        small_avg = sum(r for r, c in small) / len(small)
        info[v] = (lm, lh, lw, sm, sh, sw, lminc, large_avg, small_avg)
    colors = sorted(info.keys(), key=lambda v: info[v][6])
    left_color, right_color = colors[0], colors[1]
    lm, lh, lw, sm, sh, sw, _, large_avg, small_avg = info[left_color]
    cs_left = 0
    out = [[0] * W for _ in range(H)]
    if small_avg > large_avg:
        base_small_left = H - sh
        base_large_left = base_small_left - lh - 1
    else:
        base_large_left = H - lh
        base_small_left = base_large_left - sh - 1
    for y, x in lm:
        out[base_large_left + y][cs_left + x] = left_color
    for y, x in sm:
        out[base_small_left + y][cs_left + x] = left_color
    rlm, rlh, rlw, rsm, rsh, rsw, _, r_large_avg, r_small_avg = info[right_color]
    cs_right = max(sw, lw) + 1
    if r_small_avg > r_large_avg:
        base_small_right = H - rsh
        base_large_right = base_small_right - rlh - 1
    else:
        base_large_right = H - rlh
        base_small_right = base_large_right - rsh - 1
    for y, x in rlm:
        out[base_large_right + y][cs_right + x] = right_color
    for y, x in rsm:
        out[base_small_right + y][cs_right + x] = right_color
    return out