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
    
    def fill_pattern(row):
        n = len(row)
        result = [0] * n
        for i in range(0, n, 6):
            if i + 6 <= n:
                segment = row[i:i+6]
                if segment[0] != 0:
                    result[i:i+6] = segment
                else:
                    if i >= 6 and result[i-6] != 0:
                        result[i:i+6] = result[i-6]
        return result
    
    return [fill_pattern(row) for row in grid]