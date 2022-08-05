import sys
import csv
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import glob


def get_capacity_from_csv(file_name):
    a0 = 0
    t = file_name.split('csv/GJM1555C1')[1].split('BB01_InProduction.csv')[0]
    t = re.split('[HR]', t)[1:]
    if t[0] == '':
        pass
    else:
        a0 += float(t[0])
    a0 += 0.1 * int(t[1][0])

    return a0

def get_capacity_from_png(file_name):
    a0 = 0
    t = file_name.split('img/GJM1555C1')[1].split('BB01_InProduction.png')[0]
    t = re.split('[HR]', t)[1:]
    if t[0] == '':
        pass
    else:
        a0 += float(t[0])
    a0 += 0.1 * int(t[1][0])

    return a0

def fitting(file_name, freq_min, freq_max, save_img=True):

    if file_name.split('.')[-1] != 'csv':
        return

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
        # return a + b * np.exp( np.multiply(f, c) + d )

    # curve fitting
    a0 = get_capacity_from_csv(file_name)
    popt, pcov = curve_fit(func, freq, cap, p0=[a0, 1, 1e-4, 0], maxfev=5000)

    img_file = ''

    if save_img:
        plt.scatter(freq, cap, s=5, c='blue', zorder=2)
        # plt.plot(freq, func(freq, *popt), lw=4, c='red', zorder=1, label='{:.2E} + {:.2E}*exp(freq[GHz] * {:.2E} + {:.2E})'.format(*popt))
        func_str = '{:.3f} + {:.3e}*tan(freq/1e9 * {:.3e} + {:.3f})'.format(*popt)
        plt.plot(freq, func(freq, *popt), lw=4, c='red', zorder=1, label=func_str)
        plt.title(file_name.split('/')[-1])
        plt.xlabel('Frequency [GHz]')
        plt.ylabel('Capacity [pF]')
        plt.legend()

        plt.savefig('img/{}.png'.format(file_name.split('/')[-1].split('.csv')[0]))
        # plt.show()
        plt.close()

    return a0, func_str, img_file

