from Games.Game2048.logic import state

def test(array, leftcase, rightcase, message):
    rightstate = state(array=array.copy(), move='right')
    leftstate = state(array=array.copy(), move='left')

    rightcheck = rightstate == rightcase
    leftcheck = leftstate == leftcase

    print("input:", array)
    if rightcheck is True and leftcheck is True:
        print("Passed Both")
        print(f"Expected Leftcase : {leftcase} got {leftstate}")
        print(f"Expected Rightcase : {rightcase} got {rightstate}")
    elif rightcheck is True and leftcheck is False:
        print(f"Expected Leftcase : {leftcase} got {leftstate}")
    elif rightcheck is False and leftcheck is True:
        print(f"Expected Rightcase : {rightcase} got {rightstate}")
    else:
        print("Failed Both")
        print(f"Expected Leftcase : {leftcase} got {leftstate}")
        print(f"Expected Rightcase : {rightcase} got {rightstate}")
    return None


if __name__ == '__main__':
    test(message="PairCheck", array=[2, 2, 4, 4], leftcase=[4, 8, 0, 0], rightcase=[0, 0, 4, 8])
    print('\n' + "-" * 30)
    
    test(message='first and third are same', array=[2, 2, 2, 4], leftcase=[4, 2, 4, 0], rightcase=[0, 2, 4, 4])
    print('\n' + "-" * 30)
    
    
    test(message='second three fourth are same', array=[4, 2, 2, 2], leftcase=[4, 4, 2, 0], rightcase=[0, 4, 2, 4])
    print('\n' + "-" * 30)
    
    test(message='first and second are same', array=[2, 2, 3, 4], leftcase=[4, 3, 4, 0], rightcase=[0, 4, 3, 4])
    print('\n' + "-" * 30)
    
    test(message='second and third are same', array=[0, 2, 2, 8], leftcase=[4, 8, 0, 0], rightcase=[0, 0, 4, 8])
    print('\n' + "-" * 30)
    
    test(message='third and fouth are same', array=[8, 4, 2, 2], leftcase=[8, 4, 4, 0], rightcase=[0, 8, 4, 4])
    print('\n' + "-" * 30)
    
    test(message='all are same', array=[2, 4, 8, 16], leftcase=[2, 4, 8, 16], rightcase=[2, 4, 8, 16])
    
    print('\n' + "-" * 30)
    
    test(message='test1', array=[0, 0, 1, 4], leftcase=[1, 4, 0, 0], rightcase=[0, 0, 1, 4])
    
    print('\n' + "-" * 30)

    test(message='test1', array=[4, 4, 4, 0], leftcase=[8, 4, 0, 0], rightcase=[0, 0, 4, 8])