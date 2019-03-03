""""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.

"""""


def areSimilar(A, B):
    max = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            if A[i] in B:
                for j in range(len(B)):
                    if B[j] == A[i]:
                        if A[j] == B[i]:
                            B[j], B[i] = B[i], B[j]
            max += 1
    if max > 1:
        return False
    return True
