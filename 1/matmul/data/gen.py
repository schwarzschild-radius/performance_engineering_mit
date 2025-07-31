import numpy as np
import argparse as ap
import random as rnd

parser = ap.ArgumentParser()
parser.add_argument("m")
parser.add_argument("n")
parser.add_argument("k")
parser.add_argument("-o")
args = parser.parse_args()

m, n, k = int(args.m), int(args.n), int(args.k)

a = np.arange(m * k, dtype=float).reshape((m, k))
b = np.arange(k * n, dtype=float).reshape((k, n))

for i in range(a.shape[0]):
  for j in range(a.shape[1]):
    a[i, j] = rnd.uniform(0, 100)

for i in range(b.shape[0]):
  for j in range(b.shape[1]):
    b[i, j] = rnd.uniform(0, 100)

if args.o:
  with open(args.o, 'w') as f:
    f.write(str(m))
    f.write(' ')
    f.write(str(n))
    f.write(' ')
    f.write(str(k))
    f.write('\n')
    for i in range(a.shape[0]):
      for j in range(a.shape[1]):
        f.write(str(a[i, j]))
        f.write(' ')
        
    f.write('\n')

    for i in range(b.shape[0]):
      for j in range(b.shape[1]):
        f.write(str(b[i, j]))
        f.write(' ')
    f.write('\n')
else:
  print(a)
  print(b)
