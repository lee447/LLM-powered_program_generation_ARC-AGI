from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    rects = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 3 and not visited[y][x]:
                stack = [(x, y)]
                visited[y][x] = True
                pts = []
                while stack:
                    px, py = stack.pop()
                    pts.append((px, py))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = px+dx, py+dy
                        if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and grid[ny][nx] == 3:
                            visited[ny][nx] = True
                            stack.append((nx, ny))
                xs = [p[0] for p in pts]
                ys = [p[1] for p in pts]
                rects.append((min(xs), min(ys), max(xs), max(ys)))
    groups = {}
    for bx0, by0, bx1, by1 in rects:
        groups.setdefault((by0, by1), []).append((bx0, by0, bx1, by1))
    for (by0, by1), boxes in groups.items():
        boxes.sort(key=lambda b: b[0])
        y1, y2 = by0+1, by1-1
        for i in range(len(boxes)-1):
            _, _, x1, _ = boxes[i]
            x2, _, _, _ = boxes[i+1]
            for x in range(x1+1, x2):
                grid[y1][x] = 3
                grid[y2][x] = 3
    return grid