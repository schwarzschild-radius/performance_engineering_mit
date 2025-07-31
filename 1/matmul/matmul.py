import time
import argparse as ap


def matmul(a, b, d, dims):
    m, n, k = dims
    for i in range(m):
        for j in range(n):
            for l in range(k):
                d[i * n + j] += a[i * k + l] * b[l * k + j]
    return d


parser = ap.ArgumentParser()
parser.add_argument("input")
parser.add_argument("-o")
args = parser.parse_args()

f = open(args.input, "r")

m, n, k = [int(x) for x in f.readline().split()]
print(f"{m}, {n}, {k}")

a = [float(x) for x in f.readline().split()]
b = [float(x) for x in f.readline().split()]
d = [0] * (m * n)

start = time.time_ns()
d = matmul(a, b, d, (m, n, k))
end = time.time_ns() - start

print(f"time taken: {end / (1000 * 1000 * 1000)}")

if args.o:
    with open(args.o, "w") as f:
        f.write(str(m))
        f.write(" ")
        f.write(str(n))
        f.write("\n")
        for i in range(m):
            for j in range(n):
                f.write(str(d[i * n + j]))
                f.write(" ")

        f.write("\n")
else:
    print(d)
