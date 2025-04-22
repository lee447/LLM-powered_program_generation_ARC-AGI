from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*cols for _ in range(rows)]
    blocks = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != bg and not visited[r][c]:
                color = grid[r][c]
                queue = [(r, c)]
                visited[r][c] = True
                cells = [(r, c)]
                for cr, cc in queue:
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = cr+dr, cc+dc
                        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                            cells.append((nr, nc))
                top = min(r0 for r0, _ in cells)
                blocks.append((top, color, cells))
    blocks.sort(key=lambda x: x[0])
    out = [[bg]*cols for _ in range(rows)]
    for i, (_, color, cells) in enumerate(blocks):
        shift = -1 if i % 2 == 0 else 1
        for r, c in cells:
            out[r][c+shift] = color
    return out