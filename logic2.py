from contextlib import suppress
from collections import deque

state = [4, 4, 4, 4]
duels = []

def zeroCheck(array, move):
    array = list(filter(lambda a: a != 0, array))
    while len(array) != 4 and move == 'right':
        array.insert(0, 0)
    while len(array) != 4 and move == 'left':
        array.append(0)
    return array


def rotate(state, n=-1):
    res = deque(state)
    res.rotate(n)
    return list(res)


def left(array):
    for i, item in enumerate(array):
        with suppress(Exception):
            if array[i] == array[i+1]:
                array[i] = array[i]*2
                del array[i+1]
    return zeroCheck(array, 'left')


def right(array):
    return left(array)


print(left(array=state))
print(state)
print(left(array=state))


