from collections import Counter, defaultdict
def solve(grid):
    n, m = len(grid), len(grid[0])
    brow = [i for i in range(n) if all(grid[i][j]==4 for j in range(m))]
    bcol = [j for j in range(m) if all(grid[i][j]==4 for i in range(n))]
    rows = [i for i in range(n) if i not in brow]
    cols = [j for j in range(m) if j not in bcol]
    def intervals(a):
        iv, i = [], 0
        while i < len(a):
            j = i
            while j+1 < len(a) and a[j+1] == a[j] + 1:
                j += 1
            iv.append(a[i:j+1])
            i = j+1
        return iv
    rints, cints = intervals(rows), intervals(cols)
    cs = {v for row in grid for v in row if v not in (0,1,4)}
    if not cs:
        return grid
    tc = cs.pop()
    masks_by_shape = defaultdict(Counter)
    for bi, ri in enumerate(rints):
        for bj, ci in enumerate(cints):
            h, w = len(ri), len(ci)
            got = False
            mask = []
            for di in range(h):
                row = []
                for dj in range(w):
                    if grid[ri[di]][ci[dj]] == tc:
                        row.append(1)
                        got = True
                    else:
                        row.append(0)
                mask.append(tuple(row))
            if got:
                masks_by_shape[(h,w)][tuple(mask)] += 1
    best_mask = {shape: cnt.most_common(1)[0][0] for shape, cnt in masks_by_shape.items()}
    ans = [row[:] for row in grid]
    for bi, ri in enumerate(rints):
        for bj, ci in enumerate(cints):
            h, w = len(ri), len(ci)
            shape = (h, w)
            if shape not in best_mask:
                continue
            block = [(grid[ri[di]][ci[dj]]==tc) for di in range(h) for dj in range(w)]
            if any(block):
                continue
            if not any(grid[ri[di]][ci[dj]]==1 for di in range(h) for dj in range(w)):
                continue
            mask = best_mask[shape]
            for di in range(h):
                for dj in range(w):
                    if mask[di][dj] and grid[ri[di]][ci[dj]]==1:
                        ans[ri[di]][ci[dj]] = tc
    return ans