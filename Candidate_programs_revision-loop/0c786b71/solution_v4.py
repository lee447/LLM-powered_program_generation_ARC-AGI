from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    I = grid
    B = I[::-1]
    A = [row[::-1] for row in B]
    C = A[::-1]
    D = B[::-1]
    out = []
    R = len(I)
    for i in range(R):
        out.append(A[i] + B[i])
    for i in range(R):
        out.append(C[i] + D[i])
    return out