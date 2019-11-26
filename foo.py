import numpy as np


def axes():
    i = np.array([1, 0, 0])
    j = np.array([0, 1, 0])
    k = np.array([0, 0, 1])

    print(np.cross(i, j))
    print(np.cross(j, k))
    print(np.cross(k, i))

    print(np.dot(i,j))
    print(np.dot(j,k))
    print(np.dot(k,i))


def main():
    axes()


if __name__ == '__main__':
    main()
