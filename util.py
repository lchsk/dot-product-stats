import main
import dataset
from os import listdir
from os.path import isfile, join

def print_results(p_results):
    r = sorted(((v, k) for k, v in p_results.iteritems()), reverse=True)
    
    for (val, key) in r:
        print("{:.3f}\t{}".format(val, key))


def get_files(p_directory):
    return [(p_directory, f) for f in listdir(p_directory) if isfile(join(p_directory, f)) and f.startswith(dataset.LETTER_FILENAME)]

def read_files(p_filelist, p_language, p_vectors):
    for entry in p_filelist:
        handle = open(entry[0] + '/' + entry[1], 'r')

        for line in handle:
            pair = line.split("\t")
            p_vectors[p_language][pair[0]] = p_vectors[p_language].get(pair[0], 0) + int(pair[1])

        handle.close()

def normalise(p_vectors):

    #print p_vectors
    for lang, dat in p_vectors.items():

        values_sum = 0

        # sum all the values
        for key, value in dat.items():
            values_sum += value

        #print 'sum for ' + l[0] + ' = ' + str(values_sum)

        # normalise
        for key, value in dat.items():
            dat[key] /= float(values_sum)