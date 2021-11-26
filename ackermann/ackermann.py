# Calculate the ackermann function values for given m and n

import sys, math

def ackermann(m, n):
    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

def main(mlimit, nlimit):

    for m in range(mlimit):
        for n in range(nlimit):
            ack = ackermann(m, n)
            print(f"Ackermann({m}, {n}) = {ack}")

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
