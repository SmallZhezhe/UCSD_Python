import csv
import sys

def re_order(in_file, out file):
    with open(in_file, mode='r', newline='') as old_file:
        rows = [[row[1], row[0]] + row[2:] for row in csv.reader(old_file)]

    with open(out_file, mode='w', newline='') as new_file:
        csv.writer(new_file).writerows(rows)

if __name__ == "__main__":
    re_order(*sys.argv[1])
