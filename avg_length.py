import util
import sys


def average(p_str):

    string = p_str.strip()
    punctuation = '`~!@#$%^&*()-_=+[{]}\\|\'";:<>,./?'

    # remove punctuation
    for c in punctuation:
        string = string.replace(c, '')

    length = len(string)

    # count spaces
    spaces = 0
    for c in string:
        if c == ' ':
            spaces += 1

    return length / float(spaces)

def calculate():
    d = sys.argv[1]
    files = util.get_all_files(d)
    files_count = float(len(files))

    avg = 0
    for f in files:
        h = open(f[0] + f[1])

        body = h.read()
        avg += average(body)

        h.close()

    avg /= files_count

    print 'Average word length: ' + str(avg)


def main():
    if len(sys.argv) < 2:
        print 'Argument needed: the directory with files to load'
    else:
        calculate()

if __name__ == '__main__':
    main()