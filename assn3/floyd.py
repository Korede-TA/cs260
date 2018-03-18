from math import inf

# class Node:
#     def __init__(self, val=None, next=[]):
#         self.val = val
#         self.next = []

def Floyd(A, C):
    """
    Floyd computes shortest path matrix A given  arc cost matrix C
    """
    n = len(A)
    for i in range(n):
        for j in range(n):
            A[i][j] = C[i][j]
    for i in range(n):
        A[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]

if __name__ == "__main__":
    A = [[0]*6 for i in range(6)]
    A[1][2] = 4
    A[1][3] = 1
    A[1][4] = 5
    A[1][5] = 8
    A[1][6] = 10
    A[3][2] = 2
    A[4][5] = 2
    A[5][6] = 1
    C = []
    Floyd(A, C)
