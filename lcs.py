def lcs(a, b):
    # c = [0] * (len(a) + 1) for i in range (2)
    f = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = 1 + f[i - 1][j - 1]
            else:
                f[i][j] = max(f[i - 1][j],f[i][j - 1])
    return f


a1 = list('abcabaac')
a2 = list('baccbca')

c2 = lcs(a1, a2)
[print(*i) for i in c2]

