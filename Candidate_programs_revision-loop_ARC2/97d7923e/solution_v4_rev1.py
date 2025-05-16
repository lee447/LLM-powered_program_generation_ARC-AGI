from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    segments = []
    for j in range(w):
        i = 0
        while i < h:
            c = grid[i][j]
            if c != 0:
                start = i
                i += 1
                while i < h and grid[i][j] == c:
                    i += 1
                end = i - 1
                segments.append((end - start + 1, j, start, end, c))
            else:
                i += 1
    src_cands = [s for s in segments if s[0] >= 2]
    if not src_cands:
        return grid
    min_len = min(s[0] for s in src_cands)
    src_cands = [s for s in src_cands if s[0] == min_len]
    src = max(src_cands, key=lambda s: s[2])
    src_len, src_j, _, _, src_col = src
    dst_cands = [s for s in segments if s[0] > src_len]
    if not dst_cands:
        return grid
    dst = min(dst_cands, key=lambda s: (abs(s[1] - src_j), -s[0], s[1]))
    _, dst_j, dst_start, dst_end, _ = dst
    for i in range(dst_start + 1, dst_end):
        grid[i][dst_j] = src_col
    return grid