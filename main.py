import math


def print_menu():
    print("1. Citire lista.")
    print("2. Afisare cea mai lunga subsecventa cu toate numerele prime.")
    print("3. Afisare cea mai lunga subsecventa cu toate numerele care au acelasi numar de divizori.")
    print("4. Afisare cea mai lunga subsecventa cu toate numerele neprime.")
    print("x. Pentru iesire.")


def read_list():
    given = input("Dati numerele separate prin virgula:")
    str_list = given.split(',')
    int_list = []
    for str_num in str_list:
        int_list.append(int(str_num))
    return int_list


def is_pp(nr):
    """
    Verifica daca un numar este patrat perfect.
    :param nr: numarul dat
    :return: true daca e prim, false daca nu
    """
    root = math.sqrt(nr)
    if int(root + 0.5) ** 2 == nr:
        return True
    else:
        return False

def is_all_pp(lst):
    """
    Verifica daca toate elementele dintr-o lista sunt patrate perfecte.
    :param lst: lista data
    :return: true daca da, false daca nu
    """
    for num in lst:
        if not is_pp(num):
            return False
    return True


def test_is_all_pp():
    assert is_all_pp([2, 4, 9]) == False
    assert is_all_pp([4, 16, 25]) == True


def get_longest_sublist_pp(lst):
    """
    Determina cea mai lunga subsecventa cu toate elementele prime a unei lista.
    :param lst: lista data
    :return: o lista reprezentand prima cea mai lunga subsecventa
    """
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            considered = lst[i:j+1]
            if is_all_pp(considered):
                if len(considered) > len(result):
                    result = considered
    return result


def test_get_longest_sublist_pp():
    assert get_longest_sublist_pp([2, 4, 9, 1, 5, 16, 25]) == [4, 9, 1]
    assert get_longest_sublist_pp([2, 4, 9, 1, 5, 16, 25, 4, 100]) == [16, 25, 4, 100]


def nr_div(num):
    contor = 0
    for i in range(1, num+1):
        if num % i == 0:
            contor += 1
    return contor


def test_nr_div():
    assert nr_div(7) == 2
    assert nr_div(5) == 2
    assert nr_div(18) == 6


def is_all_same_nr_div(lst):
    """
    Verifica daca toate elementele dintr-o lista au acelasi nr de div.
    :param lst: lista data
    :return: true daca da, false daca nu
    """
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if nr_div(lst[i]) != nr_div(lst[j]):
                return False
    return True


def test_is_all_same_nr_div():
    assert is_all_same_nr_div([2, 4, 5]) == False
    assert is_all_same_nr_div([3, 5]) == True


def get_longest_sublist_same_nr_div(lst):
    """
    Determina cea mai lunga subsecventa cu toate elementele care au acelasi nr de div.
    :param lst: lista data
    :return: o lista reprezentand prima cea mai lunga subsecventa
    """
    result = []
    for i in range(len(lst)):
        for j in range(i , len(lst)):
            considered = lst[i:j+1]
            if is_all_same_nr_div(considered):
                if len(considered) > len(result):
                    result = considered
    return result


def test_get_longest_sublist_same_nr_div():
    assert get_longest_sublist_same_nr_div([23, 4, 7, 5, 7, 8, 2, 3, 5, 9]) == [7, 5, 7]
    assert get_longest_sublist_same_nr_div([5, 4, 3, 2, 5, 4]) == [3, 2, 5]



def is_all_same_bin(lst):
    """
    Verifica daca toate elementele dintr-o lista au aceeasi lungime in reprezentarea binara.
    :param lst: lista data
    :return: true daca da, false daca nu
    """
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if len(bin(lst[i])) != len(bin(lst[j])):
                return False
    return True


def test_is_all_same_bin():
    assert is_all_same_nr_div([2, 25, 5]) == False
    assert is_all_same_nr_div([2, 3]) == True


def get_longest_sublist_same_bin(lst):
    """
    Determina cea mai lunga subsecventa cu toate elementele care au aceeasi lungime in reprezentarea binara.
    :param lst: lista data
    :return: o lista reprezentand prima cea mai lunga subsecventa
    """
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            considered = lst[i:j+1]
            if is_all_same_bin(considered):
                if len(considered) > len(result):
                    result = considered
    return result

def test_get_longest_sublist_same_bin():
    assert get_longest_sublist_same_bin([15, 2, 3, 100]) == [2, 3]
    assert get_longest_sublist_same_bin([12, 3, 2, 100, 3, 2, 3]) == [3, 2, 3]



def main():
    test_is_all_pp()
    test_get_longest_sublist_pp()
    test_nr_div()
    test_is_all_same_nr_div()
    test_get_longest_sublist_same_nr_div()
    test_is_all_same_bin()
    test_get_longest_sublist_same_nr_div()
    lst = []
    while True:
        print_menu()
        optiune = input("Alege optiunea:")
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print(get_longest_sublist_pp(lst))
        elif optiune == '3':
            print(get_longest_sublist_same_nr_div(lst))
        elif optiune == '4':
            print(get_longest_sublist_same_bin(lst))
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida, reincearca !")
main()
