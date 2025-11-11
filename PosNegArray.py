def rearrange_alternate(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]

    result = pos + neg
    return result

arr = [1, 2, -3, -4, -5, 6, -7, 8, 9]
print("Original array:", arr)
print("Rearranged array:", rearrange_alternate(arr))
