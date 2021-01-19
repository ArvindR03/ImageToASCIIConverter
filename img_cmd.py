# Make sure to set terminal to the lowest font possible for best results.

from PIL import Image
import sys
from math import sqrt

HASH = " `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def load_image(path, dim):
    image = Image.open(path)

    width, height = image.size
    scale = width / dim
    newwidth = int(width / scale)
    newheight = int(height / scale)
    new_size = (newwidth, newheight)
    image_resized = image.resize(new_size)
    image.show()

    return image_resized, new_size

def to_grayscale(image, size):
    arr = image.load()
    grayscale = []

    for col in range(size[1]):
        grayscale.append([])
        for row in range(size[0]):
            r, g, b = arr[row - 1, col - 1]
            val = (r * 0.2 + g * 0.72 + b * 0.08)
            grayscale[-1].append(val)

    return grayscale

def to_letters(grayscale):
    temp = []
    for i in grayscale:
        temp.append([])
        for j in i:
            c = int((j / 255) * 65)
            temp[-1].append(HASH[c])
    letters = []
    for i in temp:
        tempstring = ''
        for j in i:
            tempstring += j
            tempstring += j
        letters.append(tempstring)
    return letters

def main():
    if sys.argv[1]:
        path = sys.argv[1]
    else:
        print('Error: file dir not given.')
        quit()

    if len(sys.argv) == 3:
        dim = int(sys.argv[2])
    else:
        dim = 300

    image, size = load_image(path, dim)
    grayscale = to_grayscale(image, size)
    letters = to_letters(grayscale)

    for i in letters:
        print(i)


if __name__ == '__main__':
    main()