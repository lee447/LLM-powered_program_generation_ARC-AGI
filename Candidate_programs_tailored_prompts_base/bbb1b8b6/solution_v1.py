from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    left = [row[:4] for row in grid]
    right = [row[5:9] for row in grid]
    shape_color = None
    for r in range(4):
        for c in range(4):
            v = right[r][c]
            if v > 1:
                shape_color = v
                break
        if shape_color is not None:
            break
    mask = [(r, c) for r in range(4) for c in range(4) if right[r][c] == shape_color]
    if mask:
        vals = [left[r][c] for r, c in mask]
        if len(set(vals)) == 1:
            small = vals[0]
            uniq = set(v for row in left for v in row)
            if len(uniq) > 1:
                border = next(v for v in uniq if v != small)
            else:
                border = small
            out = [[border]*4 for _ in range(4)]
            for r, c in mask:
                out[r][c] = shape_color
            return out
    return left