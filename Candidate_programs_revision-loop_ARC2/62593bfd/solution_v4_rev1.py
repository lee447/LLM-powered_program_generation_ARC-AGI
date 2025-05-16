from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    freq = {}
    for row in grid:
        for c in row:
            freq[c] = freq.get(c, 0) + 1
    bg = max(freq, key=lambda k: freq[k])
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != bg and not visited[i][j]:
                col = grid[i][j]
                stack = [(i, j)]
                pts = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    pts.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < H and 0 <= cc < W and not visited[rr][cc] and grid[rr][cc] == col:
                            visited[rr][cc] = True
                            stack.append((rr, cc))
                rs = [r for r,_ in pts]
                cs = [c for _,c in pts]
                mnr, mnc = min(rs), min(cs)
                h, w = max(rs)-mnr+1, max(cs)-mnc+1
                clusters.append((mnr, mnc, h, w, col, pts))
    # filter out straight lines
    filt = [cl for cl in clusters if cl[2] > 1 and cl[3] > 1]
    use_two_rows = len(filt) == len(clusters)
    # sort by original row descending, tie by col ascending
    order = sorted(filt, key=lambda cl: (-cl[0], cl[1]))
    if use_two_rows:
        k = len(order) // 2
        tops = order[:k]
        bots = order[k:]
    else:
        tops = order
        bots = []
    out = [[bg]*W for _ in range(H)]
    x = 0
    for mnr, mnc, h, w, col, pts in tops:
        for r, c in pts:
            out[r-mnr][x + (c-mnc)] = col
        x += w + 1
    if bots:
        row0 = H - max(h for _,_,h,_,_,_ in bots)
        x = 0
        for mnr, mnc, h, w, col, pts in bots:
            for r, c in pts:
                out[row0 + (r-mnr)][x + (c-mnc)] = col
            x += w + 1
    return out