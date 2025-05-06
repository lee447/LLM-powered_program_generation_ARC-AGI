def solve(grid):
    from collections import Counter
    h0, w0 = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg = max(cnt, key=lambda c: cnt[c])
    blocks = {}
    for i in range(h0):
        for j in range(w0):
            c = grid[i][j]
            if c == bg: continue
            if c not in blocks:
                blocks[c] = [i, i, j, j]
            else:
                blocks[c][0] = min(blocks[c][0], i)
                blocks[c][1] = max(blocks[c][1], i)
                blocks[c][2] = min(blocks[c][2], j)
                blocks[c][3] = max(blocks[c][3], j)
    infos = []
    for c,(r1,r2,c1,c2) in blocks.items():
        h = r2 - r1 + 1
        w = c2 - c1 + 1
        infos.append((h*w, c, h, w))
    infos.sort(reverse=True)
    _, canvas_c, H, W = infos[0]
    res = [[canvas_c]*W for _ in range(H)]
    for _, c, h, w in infos[1:]:
        for i in range(h):
            for j in range(w):
                res[i][j] = c
    return res