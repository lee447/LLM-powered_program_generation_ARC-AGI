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
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    subgrid = []
                    for x in range(i, n):
                        if grid[x][j] == 0:
                            break
                        row = []
                        for y in range(j, m):
                            if grid[x][y] == 0:
                                break
                            row.append(grid[x][y])
                        subgrid.append(row)
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