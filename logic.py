from typing import Union, List, Tuple
import random


def zeroCheck(array, move):
    array = list(filter(lambda a: a != 0, array))
    while len(array) != 4 and move == 'right':
        array.insert(0, 0)
    while len(array) != 4 and move == 'left':
        array.append(0)
    return array


def state(array: Union[Tuple[int, int, int, int], List[int]], move='right'):
    # [2, 4, 8, 16] = [2, 4, 8, 16]
    if len(list(set(array))) == 4:
        return array

    # default zero check
    array = zeroCheck(array=array, move=move)

    # ----- Pair Check -----
    # right -> [2, 2, 4, 4] => [0, 0, x0||x1**2, x2||x3*2] => [0, 0, 4, 8]
    # left  -> [2, 2, 4, 4] => [x0||x1**2, x2||x3*2, 0, 0] => [4, 8, 0, 0]
    if array[0] == array[1] and array[2] == array[3]:
        if move == 'right':
            array = [0, 0, array[0] * 2, array[2] * 2]
        if move == 'left':
            array = [array[0] * 2, array[2] * 2, 0, 0]
        return zeroCheck(array=array, move=move)

    # ----- first, second and third are same -----
    # right -> [4, 4, 4, 0] -> [0, x0, x1||x2*2, x3] = [0, 0, 4 ,8]
    # left  -> [4, 4, 4, 0] -> [x0||x1*2, x2, x3, 0] = [8, 4, 0, 0]
    if array[0] == array[1] == array[2]:
        if move == 'right':
            array = [0, array[0], array[1] * 2, array[3]]
        if move == 'left':
            array = [array[0] * 2, array[2], array[3], 0]
        return zeroCheck(array=array, move=move)

    # ----- second, third and fourth are same -----
    # right -> [4, 2, 2, 2] => [0, x0, x1, x2||x3*2]  => [0, 4, 2, 4]
    # left  -> [4, 2, 2, 2] => [x0, x1||x2*2, x3, 0]  => [4, 4, 2, 0]
    if array[1] == array[2] == array[3]:
        if move == 'right':
            array = [0, array[0], array[1], array[3] * 2]
        elif move == 'left':
            array = [array[0], array[1] * 2, array[3], 0]
        return zeroCheck(array=array, move=move)

    # ----- first and second is same -----
    # right -> [2, 2, 8, 16] -> [0, x0||x1*2, x2, x3] -> [0, 4, 8, 16]
    # left  -> [2, 2, 8, 16] -> [x0||x1*2, x2, x3, 0] -> [4, 8, 16, 0]
    if array[0] == array[1] and array[2] != array[3]:
        if move == 'right':
            array = [0, array[0] * 2, array[2], array[3]]
        elif move == 'left':
            array = [array[0] * 2, array[2], array[3], 0]
        return zeroCheck(array=array, move=move)

    # ----- second and third is same -----
    # right -> [4, 2, 2, 8] => [0, x0, x1||x2*2, x3] =>  [0, 4, 4, 8]
    # left  -> [4, 2, 2, 8] => [x0, x1||x2*2, x3, 0] =>  [4, 4, 8, 0]
    if array[1] == array[2] and array[2] != array[3]:
        if move == 'right':
            array = [0, array[0], array[1] * 2, array[3]]
        elif move == 'left':
            array = [array[0], array[1] * 2, array[3], 0]
        return zeroCheck(array=array, move=move)

    # ----- third and fourth is same -----
    # right -> [8, 4, 2, 2] => [0, x0, x1, x2||x3*2] => [0, 8, 4, 4]
    # left  -> [8, 4, 2, 2] => [x0, x1, x2||x3*2, 0] => [8, 4, 4, 0]
    if array[2] == array[3] and array[1] != array[2]:
        if move == 'right':
            array = [0, array[0], array[1], array[2] * 2]
        elif move == 'left':
            array = [array[0], array[1], array[2] * 2, 0]
        return zeroCheck(array=array, move=move)


def randomstate():
    return [[random.choice([2, 2, 0]) for _ in range(4)] for _ in range(4)]


def setmode(array, mode):
    if mode == 'up' or mode == 'down':
        arrayVertical = [[array[x][y] for x in range(4)] for y in range(4)]
        if mode == 'up':
            myArrayUP = [state(array=x, move='left') for x in arrayVertical]
            return [[myArrayUP[x][y] for x in range(4)] for y in range(4)]
        elif mode == 'down':
            myArrayDown = [state(array=x, move='down') for x in arrayVertical]
            return [[myArrayDown[x][y] for x in range(4)] for y in range(4)]
    elif mode == 'left':
        return [state(array=x, move='left') for x in array]
    elif mode == 'right':
        return [state(array=x, move='right') for x in array]



if __name__ == '__main__':
    pass
    # randomStateCall = randomstate()
    # print(randomStateCall)
    # s1 = setstate(recentstate=randomStateCall, move='left')
    # print(s1)
    # # s2 = setState(recentState=s1, move='right')
