from cProfile import label
from re import M
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# data
x = np.array([ 1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
a = np.array([ 0.446, 0.508, 0.515, 0.516, 0.530, 0.500, 0.527, 0.737, 0.756, 0.774, 0.728, 0.754, 0.785, 1.099, 1.133, 1.160, 0.092, 0.170, 0.241, 0.292, 0.355, 0.397, 0.408, 0.435, 0.462])
b = np.array([  7.759e-03, 7.715e-03, 9.215e-03, 1.648e-02, 2.301e-02, 5.973e-02, 6.705e-02, 6.072e-02, 6.549e-02, 6.380e-02, 6.880e-02, 8.282e-02, 7.863e-02, 6.886e-02, 7.643e-02, 7.962e-02, 3.410e-05, 2.088e-04, 4.287e-04, 3.791e-04, 7.252e-04, 6.110e-04, 2.152e-03, 2.388e-03, 4.369e-03])
c = np.array([ 2.307e-03, 2.033e-03, 2.215e-03, 3.652e-03, 4.747e-03, 1.150e-02, 1.248e-02, 1.229e-02, 1.264e-02, 1.179e-02, 1.165e-02, 1.360e-02, 1.256e-02, 1.348e-02, 1.443e-02, 1.450e-02, 3.710e-04, 6.529e-04, 7.254e-04, 3.748e-04, 5.633e-04, 3.578e-04, 9.738e-04, 9.192e-04, 1.486e-03])
d = np.array([ 1.553 , 1.555 , 1.554 , 1.544 , 1.536 , 1.490 , 1.486 , 1.489 , 1.488 , 1.496 , 1.498 , 1.488 , 1.496 , 1.494 , 1.490 , 1.491 , 1.566 , 1.563 , 1.563 , 1.567 , 1.565 , 1.567 , 1.562 , 1.563 , 1.559 ])

# limit capacitor range
x_max = 1.4

a = a[x <= x_max]
b = b[x <= x_max]
c = c[x <= x_max]
d = d[x <= x_max]
x = x[x <= x_max]

# sort
a = a[x.argsort()]
b = b[x.argsort()]
c = c[x.argsort()]
d = d[x.argsort()]
x = x[x.argsort()]


def fa(x, a, b, c):
    return a * np.log(b*x) + c

def fb(x, a, b):
    return a * np.exp(b*x)

def fc(x, a, b):
    return a * np.exp(b*x)

def fd(x, a, b, c):
    return a * np.exp(b*x) + c

plt.figure(figsize=(8,8))
plt.rcParams["font.size"] = 14
plt.suptitle(r'$capacitance = a + b \ \tan(freq(GHz) \cdot c + d)$')

plt.subplot(221)
plt.title('a')
plt.xlim(0, x_max)
plt.scatter(x, a)

popt_a, pcov = curve_fit(fa, x, a, maxfev=int(1e5))
plt.plot(x, fa(x, *popt_a))
print(popt_a)

plt.subplot(222)
plt.title('b')
plt.xlim(0, x_max)
plt.scatter(x, b)

popt_b, pcov = curve_fit(fb, x, b, maxfev=int(1e5))
plt.plot(x, fb(x, *popt_b))
print(popt_b)

plt.subplot(223)
plt.title('c')
plt.xlim(0, x_max)
plt.scatter(x, c)

popt_c, pcov = curve_fit(fc, x, c, maxfev=int(1e5))
plt.plot(x, fc(x, *popt_c))
print(popt_c)

plt.subplot(224)
plt.title('d')
plt.xlim(0, x_max)
plt.scatter(x, d)

popt_d, pcov = curve_fit(fd, x, d, maxfev=int(1e5))
plt.plot(x, fd(x, *popt_d))
print(popt_d)

# plt.legend()
plt.savefig('est.png')
# plt.show()

plt.clf()

##### copare 'simsurfing' data #####
import csv

refs = [
    'csv/GJM1555C1HR80BB01_InProduction.csv',
    'csv/GJM1555C1H1R1BB01_InProduction.csv'
]

caps = [0.79, 0.8, 0.81] # pF

for r in refs:
    with open(r) as f:
            reader = csv.reader(f)

            # skip sharp '#'
            header = reader.__next__()

            while header[0][0] == '#':
                header = reader.__next__()


            freq = np.array([])
            cap  = np.array([])

            for row in reader:
                freq = np.append(freq, float(row[0]))
                cap  = np.append(cap , float(row[1]))

            freq /= 1e9
            cap *= 1e12

            plt.scatter(freq[::5], cap[::5], label=r, marker='x')


def y(f, cap):
    a_ = fa(cap, *popt_a)
    b_ = fb(cap, *popt_b)
    c_ = fc(cap, *popt_c)
    d_ = fd(cap, *popt_d) 

    return a_ + b_ * np.tan(np.multiply(f, c_) + d_)

f = np.linspace(1, 6, 1000)

for c in caps:
    plt.plot(f, y(f,c), label='{} pF'.format(c))

plt.rcParams["font.size"] = 14
plt.xlim(1, 6)
plt.ylim(0.5, 2)
plt.xlabel('Frequency (GHz)')
plt.ylabel('Capacitance (pF)')
plt.legend()
plt.savefig('est2.png')
# plt.show()
