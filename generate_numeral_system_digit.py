def generate_number(n, m, prefix=None):
    '''
    Генерация любого числа длинной m в система исчесления n
    '''
    prefix = prefix or []
    for i in range(n):
        if m == 0:
            print(*prefix)
            return
        prefix.append(i)
        generate_number(n, m - 1, prefix)
        prefix.pop()


generate_number(2, 3)
