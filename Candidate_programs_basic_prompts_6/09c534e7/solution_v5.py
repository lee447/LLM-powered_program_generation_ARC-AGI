from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 1 and not visited[i][j]:
                queue = [(i,j)]
                visited[i][j] = True
                cluster = []
                for x, y in queue:
                    cluster.append((x,y))
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                min_i = min(x for x, _ in cluster)
                max_i = max(x for x, _ in cluster)
                min_j = min(y for _, y in cluster)
                max_j = max(y for _, y in cluster)
                h = max_i - min_i + 1
                w = max_j - min_j + 1
                rvis = [[False]*w for _ in range(h)]
                for a in range(min_i, max_i+1):
                    for b in range(min_j, max_j+1):
                        if grid[a][b] != 1 and not rvis[a-min_i][b-min_j]:
                            q = [(a,b)]
                            rvis[a-min_i][b-min_j] = True
                            region = []
                            col_count = {}
                            border = False
                            for x, y in q:
                                region.append((x,y))
                                if x in (min_i, max_i) or y in (min_j, max_j):
                                    border = True
                                val = grid[x][y]
                                if val not in (0,1):
                                    col_count[val] = col_count.get(val, 0) + 1
                                for dx, dy in dirs:
                                    nx, ny = x+dx, y+dy
                                    if min_i <= nx <= max_i and min_j <= ny <= max_j:
                                        if not rvis[nx-min_i][ny-min_j] and grid[nx][ny] != 1:
                                            rvis[nx-min_i][ny-min_j] = True
                                            q.append((nx, ny))
                            if not border and col_count:
                                fill = max(col_count, key=col_count.get)
                                for x, y in region:
                                    if out[x][y] == 0:
                                        out[x][y] = fill
    return out