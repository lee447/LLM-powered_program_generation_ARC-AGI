from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    v = next(grid[i][j] for i in range(n) for j in range(m) if grid[i][j] != 0)
    cr, cc = n // 2, m // 2
    pts = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == v:
                dx, dy = i - cr, j - cc
                if dx == 0 or dy == 0:
                    continue
                if dx < 0 and dy < 0:
                    k = 0
                elif dx < 0 and dy > 0:
                    k = 1
                elif dx > 0 and dy > 0:
                    k = 2
                else:
                    k = 3
                for _ in range(k):
                    dx, dy = -dy, dx
                x, y = -dx - 1, -dy - 1
                pts.append((x, y))
    if not pts:
        return []
    max_x = max(x for x, _ in pts)
    max_y = max(y for _, y in pts)
    out = [[0] * (max_y + 1) for _ in range(max_x + 1)]
    for x, y in pts:
        out[x][y] = v
    # trim rows
    while out and all(c == 0 for c in out[0]):
        out.pop(0)
    while out and all(c == 0 for c in out[-1]):
        out.pop()
    if not out:
        return out
    # trim cols
    left = 0
    while left < len(out[0]) and all(row[left] == 0 for row in out):
        left += 1
    right = len(out[0]) - 1
    while right >= 0 and all(row[right] == 0 for row in out):
        right -= 1
    return [row[left:right+1] for row in out]