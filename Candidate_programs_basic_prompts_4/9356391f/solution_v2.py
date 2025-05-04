from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    px = py = None
    for i in range(h):
        for j in range(w):
            if i>0 and grid[i][j] != 0 and not (i==1 and grid[i][j]==grid[1][0]):
                px, py = i, j
                break
        if px is not None:
            break
    for j, col in enumerate(grid[0]):
        if col != 0 and j > 0:
            d = j
            color = col
            top, bottom = px - d, px + d
            left, right = py - d, py + d
            for x in range(left, right+1):
                if 0 <= top < h and 0 <= x < w:
                    grid[top][x] = color
                if 0 <= bottom < h and 0 <= x < w:
                    grid[bottom][x] = color
            for y in range(top, bottom+1):
                if 0 <= y < h and 0 <= left < w:
                    grid[y][left] = color
                if 0 <= y < h and 0 <= right < w:
                    grid[y][right] = color
    return grid