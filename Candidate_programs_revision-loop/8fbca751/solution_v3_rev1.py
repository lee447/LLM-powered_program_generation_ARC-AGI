def solve(grid):
    h = len(grid)
    w = len(grid[0])
    seen = [[False] * w for _ in range(h)]
    boxes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and not seen[i][j]:
                seen[i][j] = True
                stack = [(i, j)]
                minr = maxr = i
                minc = maxc = j
                while stack:
                    r, c = stack.pop()
                    minr = min(minr, r)
                    maxr = max(maxr, r)
                    minc = min(minc, c)
                    maxc = max(maxc, c)
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == 8:
                            seen[nr][nc] = True
                            stack.append((nr, nc))
                boxes.append([minr, maxr, minc, maxc])
    changed = True
    while changed:
        changed = False
        n = len(boxes)
        for i in range(n):
            for j in range(i + 1, n):
                a = boxes[i]
                b = boxes[j]
                if a[0] <= b[1] and b[0] <= a[1] and a[2] <= b[3] + 1 and b[2] <= a[3] + 1:
                    boxes[i] = [min(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), max(a[3], b[3])]
                    boxes.pop(j)
                    changed = True
                    break
            if changed:
                break
    out = [row[:] for row in grid]
    for minr, maxr, minc, maxc in boxes:
        for r in range(minr, maxr + 1):
            for c in range(minc, maxc + 1):
                if out[r][c] == 0:
                    out[r][c] = 2
    return out