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


recurs_rectangle(A, B, C, D, 20)
window.getMouse()
