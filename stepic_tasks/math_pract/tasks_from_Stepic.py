#---------------
#list_a = [0, 2, 3, 4, 5, 19, 42]
#list_b = [0, 6, 19, 33, 42, 55, 66, 77, 99, 101, 256]
#Output:
#[0, 42, 19]
def common(list_a, list_b):
    common_elements = []
    for i in list_a:
        for j in list_b:
            if i == j:
                common_elements.append(i)
    return common_elements
#---------------
#Sample Input
#words = ['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']
#Sample Output:
#['x-files', 'xapple', 'xyz', '', 'apple', 'extra', 'mix']
def front_x(words):
    x_list = []
    other_list = []

    for word in words:
        if word.startswith('x') or word.startswith('X'):
            x_list.append(word)
        else:
            other_list.append(word)
    return sorted(x_list) + sorted(other_list)
#---------------
#Напишите функцию fib(n), возвращающую n-е число Фибоначчи.
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
#-----------------
#проверить, является ли число простым

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#-------------------
#Напишите функцию, которая принимает на вход строку, а возвращает 2 первых\
#    и 2 последних символа. Если длина исходной строки меньше 2 символов, \
#    необходимо вернуть пустую строку.
s = "ch"
def both_ends(s):
    if len(s)<=2:
        return ""
    return s[:2:] + s[len(s)-2]+s[len(s)-1]
print(both_ends(s))
#--------------------

import itertools
def numerics(n):
    return [int(i) for i in str(n)]

def kaprekar_step(L):
    return int(''.join(map(str, sorted(L, reverse=True)))) - int(''.join(map(str, sorted(L))))
def kaprekar_loop(n):
    i = 0
    L = numerics(n)
    for x1, x2, x3, x4 in itertools.combinations(L, 4):
        if x1 == x2 == x3 == x4:
            print(f"Ошибка! На вход подано число {n} - все цифры одинаковые")
        elif n <= 1000:
            print("Ошибка! На вход подано число 1000")
        else:
            print(n)
            if n != 6174:
                L = numerics(n)
                kaprekar_loop(kaprekar_step(L))

#---------------------


def numerics(n):
    return [int(x) for x in str(n)]

def kaprekar_check(n):
    if n == 100 or n == 1000 or n == 100000:
        return False
    elif len(numerics(n)) != 3 and len(numerics(n)) != 4 and len(numerics(n)) != 6:
        return False
    elif len(set((numerics(n)))) == 1:
        return False
    else:
        return True

#--------------------
def numerics(n):
    return [int(x) for x in str(n)]


def kaprekar_check(n):
    if n == 100 or n == 1000 or n == 100000:
        return False
    elif len(numerics(n)) != 3 and len(numerics(n)) != 4 and len(numerics(n)) != 6:
        return False
    elif len(set((numerics(n)))) == 1:
        return False
    else:
        return True


def kaprekar_step(L):
    return int(''.join(map(str, sorted(L, reverse=True)))) - int(''.join(map(str, sorted(L))))


def kaprekar_loop(n):
    if not kaprekar_check(n):
        print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")
        return

    se = set()
    prev_n = None
    while n not in se:
        print(n)
        se.add(n)
        prev_n = n
        L = numerics(n)
        n = kaprekar_step(L)
    if prev_n == n:
        return
    else:
        print(f"Следующее число - {n}, кажется процесс зациклился...")

#--------------------------
letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char_to_num = dict(map(lambda l, n: (l, n), letters, range(len(letters))))


def from_str(str, base=10):
    result = 0
    b = 1
    for c in str[::-1]:
        result += char_to_num[c] * b
        b *= base
    return result


def to_str(num, base=10):
    result = ''
    while num != 0:
        result = letters[num % base] + result
        num = num // base
    return result or '0'


def convert(num, to_base=10, from_base=10):
    x = from_str(num, from_base)
    y = to_str(x, to_base)
    return y

#--------------------------


