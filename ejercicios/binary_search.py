def binary_search(aList, aValue):
    imin = 0
    imax = len(aList) - 1
    while imax >= imin:
        imid = int(imin + ((imax - imin) / 2))
        if aList[imid] < aValue:
            imin = imid + 1
        elif aList[imid] > aValue:
            imax = imid - 1
        else:
            return imid
    return None


assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1) == 0
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 2) == 1
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 4) == 3
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5) == 4
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 6) == 5
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 7) == 6
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8) == 7
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 9) == None
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 8

assert binary_search([1], 1) == 0
assert binary_search([], 1) == None
