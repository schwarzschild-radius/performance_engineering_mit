import numpy as np
import argparse as ap
import math
import logging

parser = ap.ArgumentParser()
parser.add_argument("input1")
parser.add_argument("input2")
parser.add_argument("-debug")
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)

input1 = open(args.input1, "r")
input2 = open(args.input2, "r")

dim1 = tuple([int(x) for x in input1.readline().split(' ')])
dim2 = tuple([int(x) for x in input2.readline().split(' ')])
logging.debug(f"(m1, n1): {dim1[0]}, {dim2[1]}")
logging.debug(f"(m2, n2): {dim2[0]}, {dim2[1]}")

d1 = [float(x) for x in input1.readline().split()]
d2 = [float(x) for x in input2.readline().split()]

if dim1 != dim2:
    print(f"{dim1} != {dim2}")
    exit(1)

isequal = all(
    map(lambda x: math.isclose(x[0], x[1]), list(zip(d1, d2)))
)

if not isequal:
    print("they are not equal")
    exit(1)
