# Testing code wrote on the papaer

def isort(A):
    n = len(A)
    for j in xrange(1, n):
        key = A[j]
        i = j - 1
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

    return A


if __name__ == "__main__":
    A = [2, 8, 4, 5, 3, 7, 4]
    print isort(A)
        
