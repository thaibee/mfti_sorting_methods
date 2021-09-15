def merge(a, b):
    c = [0] * (len(a) + len(b))
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        c[k] = a[i]
        i += 1
    while j < len(b):
        c[k] = b[j]
        j += 1
    k += 1
    return c


def merge_sort(m):
    if len(m) <= 1:
        return
    middle = len(m) // 2
    left = [m[i] for i in range(0, middle)]
    right = [m[i] for i in range(middle, len(m))]
    merge_sort(left)
    merge_sort(right)
    s = merge(left, right)
    for i in range(len(m)):
        m[i] = s[i]


b = [5, 2, 7, 3, 1]

merge_sort(b)

print(b)