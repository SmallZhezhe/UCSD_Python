import math
import sys


def quadratic(a, b, c):
    x1 = -1 * b / (2 * a)
    x2 = math.sqrt(b ** 2 - 4 * a * c) / (2 * a)
    return (x1 + x2), (x1 - x2)


def main(args):
    try:
        a, b, c = (float(x) for x in args)
    except ValueError:
        print("Error: Three numeric arguments required")
        exit(1)
    try:
        solution1, solution2 = quadratic(a, b, c)
    except ZeroDivisionError:
        print("Error: the first argument cannot be zero")
        exit(1)
    except ValueError:
        print("Error: invalid arguments")
        exit(1)
    print("x = {} or {}".format(solution1, solution2))


if __name__ == "__main__":
    main(sys.argv[1:])
