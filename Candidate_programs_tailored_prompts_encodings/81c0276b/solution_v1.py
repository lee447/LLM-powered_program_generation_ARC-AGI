from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    counts = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                counts[v] = counts.get(v, 0) + 1
    anchor = max(counts, key=counts.get)
    block_counts = {}
    for r in range(h-1):
        for c in range(w-1):
            v = grid[r][c]
            if v != 0 and v != anchor and grid[r][c+1] == v and grid[r+1][c] == v and grid[r+1][c+1] == v:
                block_counts[v] = block_counts.get(v, 0) + 1
    items = sorted(block_counts.items(), key=lambda x: x[1])
    if not items:
        return []
    m = max(cnt for _, cnt in items)
    result = []
    for color, cnt in items:
        row = [color]*cnt + [0]*(m-cnt)
        result.append(row)
    return result