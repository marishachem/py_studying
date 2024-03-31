from math import atan
def f():
    return 2*atan(x)
x1 = 1e6
x2 = 1e7
print(f(x1), f(x2))
#---------------------------
def derivative(f, x0=0):
    dx = 1e-10
    d = (f(x0 + dx) - f(x0)) / dx
    return d


#--------------------------
def list_pull(L):
    res = []
    for i in L:
        if isinstance(i, list):
            res.extend(list_pull(i))
        else:
            res.append(i)
    return res
#--------------------------
def deep_copy_list(original_list):
    new_list = []
    for element in original_list:
        new_list.append(deep_copy_list(element))

    return new_list


L2 = deep_copy_list(L1)
#--------------------------
def verbing(s):
    if s.endswith('ing'):
        return s + 'ly'
    elif len(s) >= 3:
        return s + 'ing'
    else:
        return s

#--------------------------
def front_back(a,b):
    def mysplit(x):
        n = len(x) // 2 + int(len(x) % 2)
        return (x[:n], x[n:])
    a1, a2 = mysplit(a)
    b1, b2 = mysplit(b)
    return a1 + b1 + a2 + b2

#---------------------------

def mimic_dict(string):
    k = string.split()
    v = string.split()
    v = [[x] for x in v]
    k.insert(0, "")
    result = {}
    for key, value in zip(k, v):
        if key in result:
            if isinstance(result[key], list):
                result[key].append(''.join(value))
            else:
                result[key] = [result[key], ''.join(value)]
        else:
            result[key] = value
    return result

#--------------------------
import random


def print_mimic(mimic_dict, word):
    result = []
    print(mimic_dict)
    print(word)
    for i in range(200):
        result.append(word)
        # print(i)
        # print(word)
        word = random.choice(mimic_dict[word if word in mimic_dict else ''])

    return ' '.join(result)
