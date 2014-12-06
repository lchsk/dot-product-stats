import math
import operator
import dataset
import main

def compute_dot_product(p_dataset, p_vectors, p_results):

    product = 0
    test_data = p_vectors[p_dataset.test]

    for lang in p_dataset.train:
        product = 0
        for key, value in p_vectors[lang].items():
            factor = 0
            if main.ignore_when_not_found:
                factor = 0
            else:
                factor = -1
            product += value * test_data.get(key, factor)

        p_results[lang] = product

def compute_difference(p_dataset, p_vectors, p_results):

    result = 0
    test_data = p_vectors[p_dataset.test]

    for lang in p_dataset.train:

        if len(p_vectors[lang]) < 1:
            continue

        p_results[lang] = reduce(operator.add, [abs(v - test_data.get(k, 0)) for k, v in p_vectors[lang].items()])