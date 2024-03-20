import numpy as np

def StrassenMatixMultiply(A, B):
    n = len(A)
    if n == 1:
        return A * B

    mid = n // 2
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    P1 = StrassenMatixMultiply(A11 + A22, B11 + B22)
    P2 = StrassenMatixMultiply(A21 + A22, B11)
    P3 = StrassenMatixMultiply(A11, B12 - B22)
    P4 = StrassenMatixMultiply(A22, B21 - B11)
    P5 = StrassenMatixMultiply(A11 + A12, B22)
    P6 = StrassenMatixMultiply(A21 - A11, B11 + B12)
    P7 = StrassenMatixMultiply(A12 - A22, B21 + B22)

    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    C = np.block([[C11, C12], [C21, C22]])

    return C

A = np.array([[1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4]])

B = np.array([[1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4]])

print(StrassenMatixMultiply(A, B))
