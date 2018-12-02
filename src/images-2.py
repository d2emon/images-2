import sys
import math
import os
from PIL import Image
from numpy import asarray, mean, std


def even_weight(k):
    return 1.0


def sample_weight(k):
    return k * 1.0


def L_Euclide_Minkowski(l=2.0, weight=None):
    weight = weight or even_weight
    l = l * 1.0
    def f(S, X):
        size = min(len(S), len(X))
        return sum([weight(k) * (S[k] - X[k]) ** l for k in range(size)]) ** (1 / l)
    return f


def L_abs(weight=None):
    weight = weight or even_weight
    def f(S, X):
        size = min(len(S), len(X))
        return sum([weight(k) * math.fabs(S[k] - X[k]) for k in range(size)])
    return f


def L_Kamberr(S, X):
    size = min(len(S), len(X))
    return sum([math.fabs((S[k] - X[k]) / (S[k] + X[k])) for k in range(size)])


def find_similar(L, image1, files, path='.'):
    result = dict()
    for filename in files:
        image2 = Image.open("{}/{}".format(path, filename)).convert('L')
        if image2 == image1:
            continue
        value = compare_images(L, image1, image2)
        print("{}:\t{}".format(filename, value))
        result[value] = filename
    best = min(result.keys())
    return result[best]


def compare_images(L, image1, image2):
    data1 = image1.getdata()
    data2 = image2.getdata()
    # image1.show()
    # image2.show()
    # print(data1, data2)
    return L(data1, data2)


def main(filename, path='.'):
    files = os.listdir(path)
    files = filter(lambda f: f[0] != '.', files)

    print("Loading image from {}...".format(filename))
    image = Image.open(filename).convert('L')

    similar = find_similar(L_Euclide_Minkowski(), image, files, path)
    print("Best value (Euclid):\t{}".format(similar))

    similar = find_similar(L_Euclide_Minkowski(l=4), image, files, path)
    print("Best value (Minkowski):\t{}".format(similar))

    similar = find_similar(L_abs(), image, files, path)
    print("Best value (Abs):\t{}".format(similar))

    similar = find_similar(L_Euclide_Minkowski(weight=sample_weight), image, files, path)
    print("Best value (Euclid with weight):\t{}".format(similar))

    similar = find_similar(L_Euclide_Minkowski(l=4, weight=sample_weight), image, files, path)
    print("Best value (Minkowski with weight):\t{}".format(similar))

    similar = find_similar(L_abs(weight=sample_weight), image, files, path)
    print("Best value (Abs with weight):\t{}".format(similar))

    similar = find_similar(L_Kamberr, image, files, path)
    print("Best value (Kamberr):\t{}".format(similar))

    # image.show()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("images-2.py <file> <path>")
        sys.exit(0)
    main(*sys.argv[1:3])
