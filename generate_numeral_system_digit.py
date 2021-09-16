def generate_number(n, m, prefix=None):
    """
    Генерация любого числа длинной m в система исчесления n
    """
    prefix = prefix or []
    for i in range(n):
        if m == 0:
            print(*prefix)
            return
        prefix.append(i)
        generate_number(n, m - 1, prefix)
        prefix.pop()
# generate_number(2, 3)


def mutable_digit(n, m=-1, prefix=None):
    """
    Перестановка n чисел
    """
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep='')
        return
    for i in range(1, n+1):
        if i in prefix:
            continue
        prefix.append(i)
        mutable_digit(n, m-1, prefix)
        prefix.pop()


mutable_digit(5)
