def sort_insert(lst):
    """
    сортировка списка методом вставки
    """
    n = len(lst)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]


def sort_choise(lst):
    """
    сортировка списка методом выбора
    """
    n = len(lst)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


def sort_buble(lst):
    """
    сортировка списка методом пузырька
    """
    n = len(lst)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]


def sort_count(lst):
    """
    сортировка списка методом подсчета
    """
    cnt = [0]*10
    for i in lst:
        cnt[i] += 1
    lst.clear()
    for i in range(10):
        lst += ([i] * cnt[i])


def test_sort_func(f):
    """
    тестирование функции сортировки
    """
    print(f.__doc__)
    lst_1 = [5, 3, 2, 4, 1]
    print('   до:', *lst_1)
    f(lst_1)
    print('после:', *lst_1)
    print(['не получилось', 'получилось'][lst_1 == [1, 2, 3, 4, 5]])
    print()
    lst_2 = [1, 2, 3, 5, 2, 7, 6, 0, 9, 9, 2, 8, 6, 2, 8, 6, 3, 4, 1, 5, 2, 3, 7, 6, 6, 1, 3, 5, 2]
    print('   до:', *lst_2)
    f(lst_2)
    print('после:', *lst_2)
    print(['не получилось', 'получилось'][
              lst_2 == [0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9]])
    print()
    lst_3 = [6, 6, 3, 4, 3, 1, 0, 6]
    print('   до:', *lst_3)
    f(lst_3)
    print('после:', *lst_3)
    print(['не получилось', 'получилось'][lst_3 == [0, 1, 3, 3, 4, 6, 6, 6]])


if __name__ == '__main__':
    test_sort_func(sort_insert)
    test_sort_func(sort_choise)
    test_sort_func(sort_buble)
    test_sort_func(sort_count)
