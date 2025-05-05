from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    ycol = next(j for j in range(cols) if any(grid[i][j] == 4 for i in range(rows)))
    out = [[0]*4 for _ in range(rows)]
    for r in range(rows):
        left = grid[r][:ycol]
        right = grid[r][ycol+1:]
        seg_l = []
        i = 0
        while i < len(left):
            if left[i] == 8:
                start = i
                while i < len(left) and left[i] == 8:
                    i += 1
                seg_l.append((start, i - 1))
            else:
                i += 1
        if len(seg_l) == 2 and seg_l[0][1] - seg_l[0][0] == 0 and seg_l[1][1] - seg_l[1][0] == 0:
            seg_l = seg_l[:1]
        for k in range(min(len(seg_l), 2)):
            out[r][k] = 2
        seg_r = []
        i = 0
        while i < len(right):
            if right[i] == 5:
                start = i
                while i < len(right) and right[i] == 5:
                    i += 1
                seg_r.append((start, i - 1))
            else:
                i += 1
        if len(seg_r) == 1 and seg_r[0][1] - seg_r[0][0] >= 3:
            cnt_r = 2
        elif len(seg_r) == 1 and seg_r[0][1] - seg_r[0][0] == 0 and seg_r[0][1] == len(right) - 1:
            cnt_r = 0
        else:
            cnt_r = min(len(seg_r), 2)
        for k in range(cnt_r):
            out[r][2 + k] = 2
    return out