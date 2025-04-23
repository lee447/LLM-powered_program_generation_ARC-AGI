from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    segments = []
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v and not visited[r][c]:
                stack = [(r, c)]
                visited[r][c] = True
                cnt = 0
                while stack:
                    x, y = stack.pop()
                    cnt += 1
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == v:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                segments.append((cnt, v))
    segments.sort(key=lambda x: -x[0])
    side = segments[0][0]
    out = [[0]*side for _ in range(side)]
    for i, (_, v) in enumerate(segments):
        lo, hi = i, side-1-i
        if lo > hi: break
        for c in range(lo, hi+1):
            out[lo][c] = v
            out[hi][c] = v
        for r in range(lo+1, hi):
            out[r][lo] = v
            out[r][hi] = v
    return out