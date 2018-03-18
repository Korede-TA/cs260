
def FFT(n, x):
    out = [0] * len(x)
    if n == 1: 
        out[0] = x[0]
    else:
        evenarray = [ i for i in x if i%2 == 0 ]
        oddarray = [ i for i in x if i%2 == 1 ]
        u = FFT(n/2, evenarray)
        v = FFT(n/2, oddarray)
        for j in range(n-1):
            tau = (2*3.14*i*j) / n
            FFT[j] = u[j % (n/2)] + tau*v[j % (n/2)]
