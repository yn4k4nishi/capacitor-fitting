import re
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

if __name__ == "__main__":

    header = "# capacitor-fitting\n" \
             "curve fitting for capacitor vs frequency\n" \
             "\n" \
             "note : use only simsurfing data\n" \
             "\n" \
             "| label | value |\n" \
             "| ---   | ---   |\n" 

    with open('README.md', mode='w') as f:
        f.write(header)

    with open('README.md', mode='a') as f:
        imgs = glob.glob("img/*")
        for img in sorted(imgs):
            label = img.split('img/')[1]
            s = '| [{}]({}) | {:.1f}pF |\n'.format(label, img, get_capacity_from_png(img))
            f.write(s)
