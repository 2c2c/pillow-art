import random
import math
import sys
from PIL import Image, ImageFilter, ImageDraw, ImagePath


def random_line(max_length):
    """
    for ellipses, arcs, rectangles this serves as topleft/bottomright coordinates
    """
    x_1 = random.randrange(0, source.size[0])
    y_1 = random.randrange(0, source.size[1])

    x_2 = 0
    y_2 = 0

    rand_op = random.randint(0, 3)
    if rand_op == 0:
        x_2 = x_1 + random.randrange(3, max_length)
        y_2 = y_1 + random.randrange(3, max_length)
    elif rand_op == 1:
        x_2 = x_1 - random.randrange(3, max_length)
        y_2 = y_1 + random.randrange(3, max_length)
    elif rand_op == 2:
        x_2 = x_1 + random.randrange(3, max_length)
        y_2 = y_1 - random.randrange(3, max_length)
    elif rand_op == 3:
        x_2 = x_1 - random.randrange(3, max_length)
        y_2 = y_1 - random.randrange(3, max_length)

    x_2 = max(0, x_2)
    y_2 = max(0, y_2)
    x_2 = min(x_2, source.size[0])
    y_2 = min(y_2, source.size[1])

    return [(x_1, y_1), (x_2, y_2)]


def color_distance(source, new):
    r = abs(source[0] - new[0])
    g = abs(source[1] - new[1])
    b = abs(source[2] - new[2])

    total = r + g + b
    return total


def attempt_change(endpoints, colors):
    global img1, img2

    d = ImageDraw.Draw(img1)

    rand_color = colors[random.randrange(0, len(colors))]
    d.ellipse(endpoints, rand_color)

    dist_1 = 0
    dist_2 = 0

    [(x_1, y_1), (x_2, y_2)] = endpoints
    if x_1 > x_2:
        [x_1, x_2] = [x_2, x_1]
    if y_1 > y_2:
        [y_1, y_2] = [y_2, y_1]

    for x in range(x_1, x_2):
        for y in range(y_1, y_2):
            dist_1 += color_distance(
                source.getpixel((x, y)), img1.getpixel((x, y)))
            dist_2 += color_distance(
                source.getpixel((x, y)), img2.getpixel((x, y)))

    if dist_1 > dist_2:
        img1 = img2.copy()
    else:
        img2 = img1.copy()


source = Image.open(sys.argv[1])
img1 = Image.new("RGB", source.size, (255, 255, 255))
img2 = Image.new("RGB", source.size, (255, 255, 255))

colors = list(set(source.getdata()))
counter = 0
for i in range(int(sys.argv[2]) + 1):
    attempt_change(random_line(int(sys.argv[3])), colors)
    if i % 10000 == 0:
        img1.save('output/{:04d}.jpg'.format(counter))
        counter += 1
