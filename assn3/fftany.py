import numpy as np 
from functools import reduce
import random

# Find factors code adapted from Stack Overflow answer: https://stackoverflow.com/a/15837796/6641502
def factors(n):    
    factorset = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
    val = random.sample(factorset, 1)[0]
    return val, n//val

def isprime(x):
    for i in range(1,x):
        if x%i == 0:
            return False
    return True

def xi(n):
    return np.exp((2*3.14j) / n)

def FFT(n, x):
    out = [0] * len(x)
    if isprime(n): 
        for i in range(n-1):
           out[i] = sum([ x[k]*(xi(n)**(i*k)) for k in range(n-1) ])
        out[0] = x[0]
    else:
        # figure out r1 and r2 where r1*r2=n
        r1, r2 = factors(n)
        #print(r1, r2)
        for k in range(r1):
            ak = FFT(r2, [ x[k+(i*r1)] for i in range(r2) ])
        for i in range(n):
            out[i] = sum([ ak[i%r2]*(xi(n)**(i*k)) for k in range(r1) ])
    return np.array(out)

if __name__ == "__main__":
    testArr = np.array([ -3.44505240e-16 +1.14383329e-17j,
            8.00000000e+00 -5.71092652e-15j,
            2.33482938e-16 +1.22460635e-16j,
            1.64863782e-15 +1.77635684e-15j,
            9.95839695e-17 +2.33482938e-16j,
            0.00000000e+00 +1.66837030e-15j,
            1.14383329e-17 +1.22460635e-16j,
            -1.64863782e-15 +1.77635684e-15j])
    print("input array: \n%s\n" % testArr)
    print("FFT_any: \n%s\n" % FFT(8, testArr))
    print("numpy.ftt.ftt: \n%s\n" % np.fft.fft(testArr, 8))
