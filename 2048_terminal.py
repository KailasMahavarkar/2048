from Games.Game2048.logic import state, setmode, randomstate, fillMatrix

print(state([32, 8, 0, 4], move='left'))

#
# def display(array):
#     for x in array:
#         print(x)
#
#
# display(array=state)
#
# while True:
#     ui = 's'
#     if ui == 'up' or ui == 'w':
#         state = setmode(array=state, mode='up')
#     elif ui == 'down' or ui == 's':
#         state = setmode(array=state, mode='down')
#     elif ui == 'left' or ui == 'a':
#         state = setmode(array=state, mode='left')
#     elif ui == 'right' or ui == 'd':
#         state = setmode(array=state, mode='right')
#
#     if ui == 'x' or ui == 'exit':
#         break
#
#     display(array=state)
