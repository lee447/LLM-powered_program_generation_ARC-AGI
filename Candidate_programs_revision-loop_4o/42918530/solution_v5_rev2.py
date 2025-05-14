from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    for r in range(len(grid)):
        row = grid[r]
        if r % 6 == 0:
            continue
        for i in range(1, len(row) - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                color = row[i]
                start = i
                while i < len(row) - 1 and row[i] == color:
                    i += 1
                end = i
                for j in range(start, end):
                    if (j - start) % 2 == 0:
                        row[j] = color
                    else:
                        row[j] = 0
    return grid