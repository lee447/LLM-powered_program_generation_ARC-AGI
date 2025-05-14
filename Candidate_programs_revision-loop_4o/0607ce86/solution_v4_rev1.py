from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def process_row(row):
        n = len(row)
        result = [0] * n
        for i in range(0, n, 6):
            if i + 6 <= n:
                segment = row[i:i+6]
                if segment[0] != 0:
                    result[i:i+6] = segment
        return result
    
    return [process_row(row) for row in grid]