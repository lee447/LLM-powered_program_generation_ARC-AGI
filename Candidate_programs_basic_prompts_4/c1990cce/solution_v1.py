from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    w = len(grid[0])
    res = [[0]*w for _ in range(w)]
    c = grid[0].index(2)
    def draw_v(r, c0, size, color):
        h = size // 2
        for i in range(h+1):
            j1 = c0 - i
            j2 = c0 + i
            ri = r + i
            if 0 <= ri < w:
                if 0 <= j1 < w: res[ri][j1] = color
                if 0 <= j2 < w: res[ri][j2] = color
    def recurse(r, c0, size, color):
        if size < 1: return
        draw_v(r, c0, size, color)
        if size > 1:
            nh = size // 2
            recurse(r + nh, c0 - nh, nh, 1 if color == 2 else 2)
            recurse(r + nh, c0 + nh, nh, 1 if color == 2 else 2)
    recurse(0, c, w, 2)
    return res