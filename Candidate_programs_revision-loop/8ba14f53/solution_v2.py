def solve(grid):
    h, w = len(grid), len(grid[0])
    bw = w // 3
    def summarize(block):
        cnt = {}
        for row in block:
            for v in row:
                if v != 0:
                    cnt[v] = cnt.get(v, 0) + 1
        if not cnt:
            return [0, 0, 0]
        shapec = max(sorted(cnt), key=lambda x: cnt[x])
        top = sum(1 for v in block[0] if v == shapec)
        bot = sum(1 for v in block[-1] if v == shapec)
        left = sum(1 for r in block if r[0] == shapec)
        right = sum(1 for r in block if r[-1] == shapec)
        if top >= bw or bot >= bw or (left >= h and right >= h):
            return [shapec] * 3
        if left >= h // 2:
            return [shapec, 0, 0]
        if right >= h // 2:
            return [0, 0, shapec]
        return [shapec, shapec, 0]
    out = []
    for b in range(3):
        blk = [row[b*bw:(b+1)*bw] for row in grid]
        out.append(summarize(blk))
    return out