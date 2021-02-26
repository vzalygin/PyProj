from math import sqrt

def empty_image(width, height, color):
    return [[color] * width for _ in range(height)]


def draw_line(begin_coord, end_coord, image, color):
    a = end_coord[0] - begin_coord[0]
    b = begin_coord[1] - end_coord[1]
    c = -(a*begin_coord[0] + b*begin_coord[1])
    print(a, b, c)
    curr_coord = begin_coord
    tmp = 0
    try:
        while curr_coord[0] != end_coord[0]:
            image[curr_coord[0]][curr_coord[1]] = color
            print(curr_coord[0], curr_coord[1], '=', a * curr_coord[0],  b * curr_coord[1], c)
            if sqrt():
                curr_coord[0] += 1
            else:
                curr_coord[1] += 1
            tmp += 1

        image[curr_coord[0]][curr_coord[1]] = color
    except:
        print('err')
    return image


def create_image_file(filename, image):
    width = len(image[0])
    height = len(image)
    matrix = [component for row in image for pixel in row for component in pixel]

    with open(filename, 'wb') as f:
        f.write(bytes([
                          0,
                          0,
                          2,
                          0, 0, 0, 0, 0,
                          0, 0,
                          0, 0,
                          width % 256, width // 256,
                          height % 256, height // 256,
                          24,
                          1 << 5, ] + matrix))


white = [255, 255, 255]
black = [0, 0, 0]

img = empty_image(10, 10, white)
img = draw_line([0, 0], [4, 4], img, black)
create_image_file("line.tga", img)
