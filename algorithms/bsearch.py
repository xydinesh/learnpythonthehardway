"""
Binary search
"""

def search(x, A, low, high):
    mid = (low + high)/2
    if x == A[mid]:
        return mid

    if low == mid or mid == high:
        return -1

    if x > A[mid]:
        low = mid
    else:
        high = mid

    return search(x, A, low, high)

if __name__ == "__main__":
    A = [1, 4, 5, 6, 8, 10 , 3, 2, 21, 19]
    B = sorted(A)
    x = 3
    print B, ":", x
    print "index:", search(x, B, 0, len(B))
    
