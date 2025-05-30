# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'.
# This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# for x in picture:
#     # print(x)
#     for y in x:
#         print(' ') if y == 0 else print('*')

# theirs

def show_tree(fill, empty, picture):
    for row in picture:
        for pixel in row:
            if pixel:  # if pixel == 1:
                print(fill, end='')
            else:
                print(empty, end='')
        else:
            print('')


fill = '*'
empty = ' '

show_tree(fill, empty, picture)
show_tree(fill, empty, picture)

#
# for row in picture:
#     for pixel in row:
#         if pixel: # if pixel == 1:
#             print(fill, end='')
#         else:
#             print(empty, end='')
#     else:
#         print('')