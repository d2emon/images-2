import sys
import math
import os
from PIL import Image
from numpy import asarray, mean, std


def even_weight(k):
    return 1


def L_Euclide_Minkowski(S, etalon, n, l=2, weight=None):
    weight = weight or even_weight
    return sum([weight(k) * (S[k] - etalon[k]) ** l for k in range(len(S))]) ** (1 / l)


def L_abs(S, etalon, weight=None):
    weight = weight or even_weight
    return sum([weight(k) * math.fabs(S[k] - etalon[k]) for k in range(len(S))])


def L_Kamberr(S, etalon):
    return sum([math.fabs((S[k] - etalon[k]) / (S[k] + etalon[k])) for k in range(len(S))])


def compare_images(image1, image2):
    data1 = asarray(image1)
    data2 = asarray(image2)
    image1.show()
    image2.show()

def main(path='.'):
    files = os.listdir(path)
    files = filter(lambda f: f[0] != '.', files)
    for filename1 in files:
        print("Loading image from {}...".format(filename1))
        image1 = Image.open("{}/{}".format(path, filename1)).convert('L')
        for filename2 in files:
            image2 = Image.open("{}/{}".format(path, filename1)).convert('L')
            print("{}<==>{}".format(filename1, filename2))
            compare_images(image1, image2)

    # image.show()

    """
    for grade in [None, 8, 16, 32, 64, 128]:
        if grade is None:
            images = image,
        else:
            images = image.quantize(grade), quantize(image, grade)

        print('=' * 80)
        print("quantize grade = {}".format(grade or "original"))
        for id, quantized in enumerate(images):
            quantized = quantized.

            print('-' * 20)
            if id == 0:
                print("PIL quantizer")
            else:
                print("My quantizer")

            print("min = {}".format(data.min()))
            print("max = {}".format(data.max()))
            if grade is None:
                print("original")
                continue

            du = data.max() - data.min()
            L = math.log2(grade)
            df = (2 ** 8) / (2 ** L)
            disperse = math.sqrt((df ** 2) / 12)
            sh = 20 * math.log10(du / disperse)
            # K_sq =

            print("delta u = {}".format(du))
            print("mean = {}".format(mean(data)))
            print("std = {}".format(std(data)))
            print("df = {}".format(df))
            print("disperse = {}".format(disperse))
            print("s/sh = {}".format(sh))
            # print("K sq = {}".format(K_sq))

            quantized.show(grade)

    print(input_file, output_file)
    """


if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("images-2.py <inputfile> <outputfile>")
    #     sys.exit(0)
    # main(*sys.argv[1:3])
    main('./res')
