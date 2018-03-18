import numpy as np

def FFT(n, x):
    out = [0] * len(x)
    if n == 1: 
        out[0] = x[0]
    else:
        evenarray = x[1::2]
        oddarray = x[::2]
        u = FFT(len(evenarray), evenarray)
        v = FFT(len(oddarray), oddarray)
        for i in range(n-1):
            tau = np.exp((2*3.14j*i) / n)
            out[i] = u[i % len(evenarray)] + tau*v[i % len(oddarray)]
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
    print("FFT_dyadic: \n%s\n" % FFT(8, testArr))
    print("numpy.ftt.ftt: \n%s\n" % np.fft.fft(testArr, 8))
