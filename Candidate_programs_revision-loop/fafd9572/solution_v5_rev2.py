import numpy as np

def solve(grid):
    A = np.array(grid)
    h, w = A.shape
    visited = np.zeros((h, w), bool)
    mask_pts = None
    for i in range(h):
        for j in range(w):
            if A[i, j] > 1:
                stack = [(i, j)]
                visited[i, j] = True
                mask_pts = []
                while stack:
                    r, c = stack.pop()
                    mask_pts.append((r, c))
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0: continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < h and 0 <= nc < w and not visited[nr, nc] and A[nr, nc] > 1:
                                visited[nr, nc] = True
                                stack.append((nr, nc))
                break
        if mask_pts is not None:
            break
    if mask_pts is None:
        return grid
    rs = [r for r, c in mask_pts]
    cs = [c for r, c in mask_pts]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    M = np.zeros((r1 - r0 + 1, c1 - c0 + 1), int)
    for r, c in mask_pts:
        M[r - r0, c - c0] = A[r, c]
    Ts = []
    for flip in (False, True):
        M2 = np.fliplr(M) if flip else M
        for k in range(4):
            T = np.rot90(M2, k)
            if not any(t.shape == T.shape and np.array_equal(t, T) for t in Ts):
                Ts.append(T)
    B = A.copy()
    visited1 = np.zeros((h, w), bool)
    for i in range(h):
        for j in range(w):
            if A[i, j] == 1 and not visited1[i, j]:
                stack = [(i, j)]
                visited1[i, j] = True
                comp = []
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0: continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < h and 0 <= nc < w and not visited1[nr, nc] and A[nr, nc] == 1:
                                visited1[nr, nc] = True
                                stack.append((nr, nc))
                rs2 = [r for r, c in comp]
                cs2 = [c for r, c in comp]
                r2, c2 = min(rs2), min(cs2)
                r3, c3 = max(rs2), max(cs2)
                sub = (A[r2:r3+1, c2:c3+1] == 1)
                for T in Ts:
                    if T.shape == sub.shape and (T > 0).tolist() == sub.tolist():
                        mask = T > 0
                        B[r2:r3+1, c2:c3+1][mask] = T[mask]
                        break
    return B.tolist()