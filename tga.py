def empty_image(dimens, color):
    return [[color] * dimens[1] for _ in range(dimens[0])]


def func(y, x, a, b, c):
    return abs(a*y + b*x + c)


def draw_point(c, image, color):
    print(c)
    image[c[0]][c[1]] = color
    return image


def draw_line(b_c, e_c, image, color):
    """
    b_c - начальные координаты
    e_c - конечные
    c_c - текущие координаты
    """
    c_c = b_c.copy()
    a = e_c[0] - c_c[0]
    b = c_c[1] - e_c[1]
    c = -(a * e_c[0] + b * e_c[1])
    step_y, step_x = 1, 1
    if a < 0: step_y = -1
    if b > 0: step_x = -1
    print(a, b, c)
    print(step_y, step_x)
    bitmap(len(image), len(image[0]), a, b, c)
    try:
        while not (c_c[0] == e_c[0] and c_c[1] == e_c[1]):
            draw_point(c_c, image, color)
            print(func(c_c[0], c_c[1], a, b, c))
            if func(c_c[0] + step_y, c_c[1], a, b, c) \
                    < func(c_c[0], c_c[1] + step_x, a, b, c):
                c_c[0] += step_y
            else:
                c_c[1] += step_x
        # draw_point(b_c, image, color)
    except Exception as e:
        print(e)
    return image


def bitmap(h, w, a, b, c):
    for y in range(h):
        print([func(y, x, a, b, c) for x in range(w)])


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
black = [0, 255, 0]
red = [0, 0, 255]

size = [9, 9]
c1 = [4, 4]
c2 = [0, 0]

image = empty_image(size, white)
image = draw_line(c1, c2, image, black)
image = draw_point(c1, image, red)
image = draw_point(c2, image, red)
create_image_file("line.tga", image)
