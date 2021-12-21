from PIL import Image, ImageDraw
import numpy as np

def convert(path: str):
    file = Image.open(path)
    (width, height) = file.size
    #file = file.resize((10, 10))
    arr = toGray(np.array(file))

    symbols = ['.', ',', '^', '!', '/', '$', '#', '@']


    new_img = Image.new('RGB', (width * 6, height * 15))
    ImageDraw.Draw(new_img).text((0, 0), toSymbols(arr, symbols), fill=('#FFFFFF'))
    #new_img = new_img.resize((width, height))
    new_img.save('rez.jpg')

def toGray(arr):

    for lines in range(len(arr)):
        for pixels in range(len(arr[lines])):
            md = 0
            for col in arr[lines][pixels]:
                md += col

            md //= len(arr[lines][pixels])

            arr[lines][pixels] = np.array((md, md, md))

    return arr

def toSymbols(arr, symbols):
    rez = ''
    for lines in range(len(arr)):
        for pixels in range(len(arr[lines])):
            sb = symbols[map(arr[lines][pixels], len(symbols))]
            rez += sb

        rez += '\n'

    return rez


def map(arr, limit):
    return (arr[0]*limit)//256
