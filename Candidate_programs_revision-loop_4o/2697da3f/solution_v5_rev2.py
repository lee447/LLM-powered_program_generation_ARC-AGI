from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def rotate_and_mirror(subgrid):
        n = len(subgrid)
        m = len(subgrid[0])
        result = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                result[j][n - i - 1] = subgrid[i][j]
        return result

    def extract_subgrids(grid):
        subgrids = []
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        
        def dfs(x, y, subgrid):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0 or visited[x][y]:
                return
            visited[x][y] = True
            subgrid.append((x, y))
            dfs(x + 1, y, subgrid)
            dfs(x - 1, y, subgrid)
            dfs(x, y + 1, subgrid)
            dfs(x, y - 1, subgrid)

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and not visited[i][j]:
                    subgrid_coords = []
                    dfs(i, j, subgrid_coords)
                    min_x = min(x for x, y in subgrid_coords)
                    max_x = max(x for x, y in subgrid_coords)
                    min_y = min(y for x, y in subgrid_coords)
                    max_y = max(y for x, y in subgrid_coords)
                    subgrid = [[0] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]
                    for x, y in subgrid_coords:
                        subgrid[x - min_x][y - min_y] = grid[x][y]
                    subgrids.append(subgrid)
        return subgrids

    subgrids = extract_subgrids(grid)
    transformed_subgrids = [rotate_and_mirror(subgrid) for subgrid in subgrids]

    max_height = max(len(subgrid) for subgrid in transformed_subgrids)
    max_width = max(len(subgrid[0]) for subgrid in transformed_subgrids)

    output_grid = [[0] * (max_width * 2 + 1) for _ in range(max_height * 2 + 1)]

    for idx, subgrid in enumerate(transformed_subgrids):
        offset_x = (idx % 2) * (max_width + 1)
        offset_y = (idx // 2) * (max_height + 1)
        for i in range(len(subgrid)):
            for j in range(len(subgrid[0])):
                output_grid[offset_y + i][offset_x + j] = subgrid[i][j]

    return output_grid