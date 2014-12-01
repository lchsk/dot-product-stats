#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import re
import fnmatch
import math
import os
import operator

test_data = u'nua d,lcDöf .teldajetv,v r y  aNlJ, Dvgjåaroaunann,nögd g r,,  rdanönnm dlvagDgDndgi: t a JDiröt mDdnj ia lau rugofdv i ta  m  e äa k.Df,häll eanr ij / lh äräå  ot ö:ä  raDufp2vgr rsatr aevos s r ,ern!i at l uln haDb ksDou jlila utsDa dåo.ä a dvna noe./,/s:ug,mäaerl /iålmJ :nnöi rrrj utpe e o1igia d fi D pt  h Dg n lrDanr io'
test_data_lc = test_data.lower()
test_data_len = len(test_data)
test_stats = None

check = '''1Du gamla, Du fria, Du fjällhöga nordDu tysta, Du glädjerika sköna!Jag hälsar Dig, vänaste land uppå jord,/: Din sol, Din himmel, Dina ängder gröna.:/2Du tronar på minnen från fornstora dar,då ärat Ditt namn flög över jorden.Jag vet att Du är och Du blir vad Du var./:Ja, jag vill leva, jag vill dö i Norden.:/'''

# files
swedish_text    = './bibles/svenska1917.txt'
danish_text     = './bibles/danish.txt'
norwegian_text  = './bibles/norwegian.txt'
swedish2_text   = './bibles/swedish2.txt'
finnish_text    = './bibles/finnish.txt'
polish_text     = './bibles/polish.txt'
german_text     = './bibles/german.txt'

# directories
norwegian_dir   = './bibles/no/'
swedish2_dir    = './bibles/se/'
finnish_dir     = './bibles/fi/'
polish_dir      = './bibles/pl/'
german_dir      = './bibles/de/'

def get_stats(p_text):

    results = {}

    for c in p_text:
        results[c] = results.get(c, 0) + 1

    return results

def normalise(p_stats):
    sum_ = float(reduce(operator.add, [v for k, v in p_stats.items()]))

    ret_dictionary = {}

    for k, v in p_stats.items():
        ret_dictionary[k] = v / sum_

    return ret_dictionary

def look_at_indices(p_handle):
    chunk = ''
    second = False

    for line in handle:
        search = re.search(r'[0-9]+:[0-9]+:(1|2):', line, re.M | re.I)
        if search:
            if ':1:' in search.group():
                if second:
                    second = True
                    s = get_stats(chunk)
                    if s.get('D') > 5:
                        print s.get('D')
                        print chunk
                        print len(chunk)
                        print test_data_len 
                    #if abs(len(chunk) - test_data_len) < 5:
                        #print chunk
                    chunk = ''
                chunk += line
            elif ':2:' in search.group():
                chunk += line
                second = True

def window_search(p_handle, p_language, p_window_size, p_step_size):

    text = p_handle.read()
    #window_size = test_data_len

    # indices at the start
    idx_s = 0
    idx_e = p_window_size
    chunks_file = codecs.open('./' + p_language, 'w', encoding='utf-8')

    while idx_e < len(text):

        chunk = text[idx_s:idx_e]
        s = get_stats(chunk.lower())

        if similar(test_stats, normalise(s)):
            print chunk

        #similar()
        #if s.get('å') > 3 and s.get('ä') > 3 and s.get('ö') > 3:
        #if s.get('d') > 25:
        # if s.get(',') > 5 and s.get('j') > 5 and s.get('N') > 0 and s.get('1') > 0 and s.get('2') > 0 and s.get('D') > 10:
        #   chunks_file.write(chunk + '\n\n')
            #print s.get('D')
            #print 'length: ' + str(len(chunk))

        idx_s += p_step_size
        idx_e += p_step_size

    chunks_file.close()

def open_file(p_filename):

    handle = codecs.open(p_filename, encoding='utf-8')

    window_search(handle, p_filename + 'search', 200, 50)

    handle.close()

def copy_to_single_file(p_dir, p_target_filename):
    matches = []
    for root, dirnames, filenames in os.walk(p_dir):
      for filename in fnmatch.filter(filenames, '*.htm'):
          matches.append(os.path.join(root, filename))

    target_file = open(p_target_filename, 'w')

    for directory in matches:
        h = open(directory)

        body = h.read()

        # those are really in the source code
        start_string = '<!--... the Word of God:-->'
        end_string = '<!--... sharper than any twoedged sword... -->'

        found = re.findall(r'' + start_string + '(.*)' + end_string, body, re.M | re.S)

        if len(found) > 0:
             found = found[0]
             target_file.write(strip_html(found).strip())

        h.close()
        #return

    target_file.close()

def strip_html(p_str):
    return re.sub('<[^<]+?>', '', p_str)

def similar(p_set1, p_set2):

    #print p_set1
    #print p_set2
    result = 0
    for key, value in p_set1.items():
        result += abs(value - p_set2.get(key, 0))

    if result < 0.25:
        print result
        return True
    else:
        return False


if __name__ == '__main__':

    test_stats = get_stats(test_data)
    print test_stats
    test_stats = normalise(test_stats)
    #print test_stats
    #print get_stats(test_data_lc)

    #t = get_stats(test_data_lc)
    # normalise(t)

    #print t
    similar(test_stats, normalise(get_stats(check)))
    print get_stats(check)

    #open_file(swedish_text)
    #copy_to_single_file(german_dir, german_text)