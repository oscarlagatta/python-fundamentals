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
for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    else:
        print('')