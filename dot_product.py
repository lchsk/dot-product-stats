import math
import operator
import dataset
import main

def compute_dot_product(p_dataset, p_vectors, p_results):

    product = 0
    test_data = p_vectors[p_dataset.test]

    for lang in p_dataset.train:
        for key, value in p_vectors[lang].items():
            factor = 0
            if main.ignore_when_not_found:
                factor = 0
            else:
                factor = -1
            product += value * test_data.get(key, factor)

        p_results[lang] = product
        #print "Dot product for " + lang + ': ' + str(product)

    # for lang in p_dataset.train:
    #     for key, value in test_data.items():
    #         product += value * vectors[lang].get(key, -1)
    #     print "Dot product for " + lang + ': ' + str(product)

    # for key, value in test_data.items():
    #     product += value * vectors[p_language].get(key, -1)