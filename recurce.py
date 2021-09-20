import graphics as gr

window = gr.GraphWin('Picture', 300, 300)

A = gr.Point(10, 10)
B = gr.Point(10, 290)
C = gr.Point(290, 290)
D = gr.Point(290, 10)
ALPHA = 0.2


def chn_point(p1, p2):
    """
    меняем координтаты точки на коэфицент ALPHA
    """
    return gr.Point(p1.x * (1 - ALPHA) + p2.x * ALPHA, p1.y * (1 - ALPHA) + p2.y * ALPHA)


def recurs_rectangle(a, b, c, d, depth=10):
    """
    рекурсия рисующая меньший квадрат в квадрате с заданными координатами a,b,c,d и соотношением alpha
    """
    if depth < 1:
        return
    for m, n in (a, b), (b, c), (c, d), (d, a):
        gr.Line(m, n).draw(window)
    a1 = chn_point(a, b)
    b1 = chn_point(b, c)
    c1 = chn_point(c, d)
    d1 = chn_point(d, a)
    recurs_rectangle(a1, b1, c1, d1, depth - 1)


# recurs_rectangle(A, B, C, D, 20)
# window.getMouse()


def gcd(a, b):
    """алгоритм Евклида по поиску НОД"""
    return a if not b % a else gcd(b % a, a)


def change_tow(length, t_source, t_target, t_temp):
    """ханойские башни example: change_tow(6, [6, 5, 4, 3, 2, 1], [], [])"""
    if length > 0:
        change_tow(length-1, t_source, t_temp, t_target)
        t_target.append(t_source.pop())
        print(t_source, t_target, t_temp)
        change_tow(length-1, t_temp, t_target, t_source)



def merge(a, b):
    """алгоритм сортировки слиянием"""
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


def sort(a):
    """Сортировка Тони Хора"""
    if len(a) < 2:
        return
    l = []
    m = []
    r = []
    for i in a:
        if i < a[0]:
            l.append(i)
        elif i == a[0]:
            m.append(i)
        else:
            r.append(i)
    k = 0
    sort(l)
    sort(r)
    for x in l + m + r:
        a[k] = x
        k += 1