from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def extract_non_zero_blocks(grid):
        blocks = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in visited:
                    color = grid[r][c]
                    block = []
                    queue = [(r, c)]
                    while queue:
                        x, y = queue.pop(0)
                        if (x, y) in visited or grid[x][y] != color:
                            continue
                        visited.add((x, y))
                        block.append((x, y))
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                                queue.append((nx, ny))
                    blocks.append(block)
        return blocks

    def get_bounding_box(block):
        min_r = min(block, key=lambda x: x[0])[0]
        max_r = max(block, key=lambda x: x[0])[0]
        min_c = min(block, key=lambda x: x[1])[1]
        max_c = max(block, key=lambda x: x[1])[1]
        return min_r, max_r, min_c, max_c

    def extract_subgrid(grid, min_r, max_r, min_c, max_c):
        return [row[min_c:max_c+1] for row in grid[min_r:max_r+1]]

    blocks = extract_non_zero_blocks(grid)
    subgrids = []
    for block in blocks:
        min_r, max_r, min_c, max_c = get_bounding_box(block)
        subgrid = extract_subgrid(grid, min_r, max_r, min_c, max_c)
        subgrids.append(subgrid)

    subgrids.sort(key=lambda x: (len(x), len(x[0]), x))
    result = []
    for subgrid in subgrids:
        result.extend(subgrid)
    return result