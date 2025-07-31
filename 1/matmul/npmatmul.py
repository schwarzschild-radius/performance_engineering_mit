import numpy as np
import argparse as ap
import time

parser = ap.ArgumentParser()
parser.add_argument("input")
parser.add_argument("-o")
args = parser.parse_args()

f = open(args.input, 'r')

m, n, k = [int(x) for x in f.readline().split()]
print(f"{m}, {n}, {k}")

a = np.array([float(x) for x in f.readline().split()]).reshape((m , k))
b = np.array([float(x) for x in f.readline().split()]).reshape((k, n))

start = time.time_ns()
d = np.matmul(a,b)
end = time.time_ns() - start

print(f'time taken: {end / (1000 * 1000 * 1000)}')

if args.o:
  with open(args.o, 'w') as f:
    f.write(str(m))
    f.write(' ')
    f.write(str(n))
    f.write('\n')
    for i in range(d.shape[0]):
      for j in range(d.shape[1]):
        f.write(str(d[i, j]))
        f.write(' ')
        
    f.write('\n')
else:
  print(d)
