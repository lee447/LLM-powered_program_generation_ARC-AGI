from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    r0, r1 = H, -1
    c0, c1 = W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 4:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    h, w = r1 - r0 + 1, c1 - c0 + 1
    tile = [row[c0:c0+w] for row in grid[r0:r0+h]]
    newH, newW = 2*H + 1, 2*W + 1
    out = [[0]*newW for _ in range(newH)]
    for dr in (0, H+1):
        for dc in (0, W+1):
            for i in range(h):
                for j in range(w):
                    out[r0+dr+i][c0+dc+j] = tile[i][j]
    # trim zero-only borders
    def trim_rows(mat):
        top = 0
        while top < len(mat) and all(x==0 for x in mat[top]):
            top += 1
        bot = len(mat)-1
        while bot >= 0 and all(x==0 for x in mat[bot]):
            bot -= 1
        return mat[top:bot+1]
    def trim_cols(mat):
        if not mat: return mat
        left = 0
        while left < len(mat[0]) and all(row[left]==0 for row in mat):
            left += 1
        right = len(mat[0]) - 1
        while right >= 0 and all(row[right]==0 for row in mat):
            right -= 1
        return [row[left:right+1] for row in mat]
    out = trim_rows(out)
    out = trim_cols(out)
    return out