import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import glob
from update_list import get_capacity_from_csv


freq_min = 3e9
freq_max = 6e9

files = glob.glob("csv/*")
for file_name in files:

    if file_name.split('.')[-1] != 'csv':
        continue

    print("================================================================")
    print("- File path : {}".format(file_name))
    print("- Frequency : {} ~ {} [GHz]".format(freq_min/1e9, freq_max/1e9))

    with open(file_name) as f:
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

    # pick up range
    i_max = len(freq)-1
    i_min = 0

    while freq[i_max] >= freq_max:
        i_max += -1

    while freq[i_min] <= freq_min:
        i_min += 1

    freq = freq[i_min:i_max]
    cap  = cap[i_min:i_max]

    # convert unit
    freq /= 1e9
    cap  *= 1e12

    # fit function
    def func(f, a, b, c, d):
        return a + b * np.tan( np.multiply(f, c) + d )
        return a + b * np.exp( np.multiply(f, c) + d )

    # curve fitting
    a0 = get_capacity_from_csv(file_name)
    popt, pcov = curve_fit(func, freq, cap, p0=[a0, 1, 1e-4, 0], maxfev=5000)


    plt.scatter(freq, cap, s=5, c='blue', zorder=2)
    # plt.plot(freq, func(freq, *popt), lw=4, c='red', zorder=1, label='{:.2E} + {:.2E}*exp(freq[GHz] * {:.2E} + {:.2E})'.format(*popt))
    plt.plot(freq, func(freq, *popt), lw=4, c='red', zorder=1, label='{:.2f} + {:.4f}*tan(freq[GHz] * {:.2f} + {:.2f})'.format(*popt))
    plt.title(file_name.split('/')[-1])
    plt.xlabel('Frequency [GHz]')
    plt.ylabel('Capacity [pF]')
    plt.legend()

    plt.savefig('img/{}.png'.format(file_name.split('/')[-1].split('.csv')[0]))
    # plt.show()
    plt.close()

