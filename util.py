import main
import dataset
import operator
from os import listdir
from os.path import isfile, join

def print_results(p_results, p_reverse = True, p_decimal_numbers = 5):
    r = sorted(((v, k) for k, v in p_results.iteritems()), reverse = p_reverse)
    
    string_format = "{:." + str(p_decimal_numbers) + "f}\t{}"

    for (val, key) in r:
        print(string_format.format(val, key))


def get_files(p_directory):
    return [(p_directory, f) for f in listdir(p_directory) if isfile(join(p_directory, f)) and f.startswith(dataset.LETTER_FILENAME)]

def get_all_files(p_directory):
    return [(p_directory, f) for f in listdir(p_directory) if isfile(join(p_directory, f))]


def read_files(p_filelist, p_language, p_vectors):
    for entry in p_filelist:
        try:
            handle = open(entry[0] + '/' + entry[1], 'r')

            for line in handle:
                pair = line.split("\t")
                p_vectors[p_language][pair[0]] = p_vectors[p_language].get(pair[0], 0) + int(pair[1])

            handle.close()
        except:
            print 'Error: ' + p_language

def normalise(p_vectors):
    for lang, dat in p_vectors.items():
        # sum of all the values in a list

        if len(dat) < 1:
            continue

        values_sum = float(reduce(operator.add, [v for k, v in dat.items()]))

        # normalise
        p_vectors[lang] = dict((k, v / values_sum) for k, v in dat.items())