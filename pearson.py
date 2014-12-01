import operator
import math

def mean(p_d):
    mean = reduce(operator.add, [v for k, v in p_d.items()])
    return mean / len(p_d)

def stddev(p_d, p_mean):
    stddev = reduce(operator.add, [(v - p_mean)**2 for k, v in p_d.items()])
    return math.sqrt(stddev / len(p_d))

def pearson(p_d1, p_d2, p_mean1, p_mean2, p_stddev1, p_stddev2):
    tmp = reduce(operator.add, [(v - p_mean1) * (p_d2.get(k, 0) - p_mean2) for k, v in p_d1.items()])

    return (tmp / len(p_d1)) / (p_stddev1 * p_stddev2)

def compute(p_dataset, p_vectors, p_results):

    test_data = p_vectors[p_dataset.test]
    m_test = mean(test_data)
    s_test = stddev(test_data, m_test)

    for lang in p_dataset.train:
        l = p_vectors[lang]
        m_l = mean(l)
        s_l = stddev(l, m_l)

        p_results[lang] = pearson(test_data, l, m_test, m_l, s_test, s_l)