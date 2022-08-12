import glob
from fitting import fitting


if __name__ == "__main__":

    header = "# capacitor-fitting\n" \
             "curve fitting for capacitor vs frequency\n" \
             "\n" \
             "note : use only simsurfing data\n" \
             "\n" \
             "| label | value | func |\n" \
             "| ---   | ---   | --- |\n" 

    with open('README.md', mode='w') as f:
        f.write(header)

    with open('README.md', mode='a') as f:
        csvs = glob.glob("csv/*")
        for csv in sorted(csvs):

            label = csv.split('csv/')[1]
            cap, func, img_file = fitting(csv, 2e9, 7e9)

            s = '| [{}]({}) | {:.1f}pF | `{}` |\n'.format(label, img_file, cap, func)
            f.write(s)
