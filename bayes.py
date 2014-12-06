import math
import operator

def calculate(p_dataset, p_vectors, p_results):

    test_data = p_vectors[p_dataset.test]

    for lang in p_dataset.train:
        A = reduce(operator.add, [v for k, v in p_vectors[lang].items()])
        N = reduce(operator.add, [v for k, v in test_data.items()])

        # print A, math.lgamma(A), N, math.lgamma(N), A+N, math.lgamma(A+N)

        # get rid of very small values
        p_vectors[lang] = dict((k, v) for k, v in p_vectors[lang].iteritems() if v > 2)
        test_data = dict((k, v) for k, v in test_data.iteritems() if v > 2)

        # if lang == 'finnish_genesis_spaces':
        #     p_vectors[lang]['b'] = 39
        #     p_vectors[lang]['f'] = 50
        #     p_vectors[lang]['g'] = 50            

        print lang
        print p_vectors[lang]

        print reduce(operator.add, [v for k,v in p_vectors[lang].items()]), len(p_vectors[lang])



        # for k,v in test_data.items():
        #      print v, math.lgamma(v)
        nominator = reduce(operator.mul, [math.lgamma(v + p_vectors[lang].get(k, 0)) for k, v in test_data.items()])
        denominator = reduce(operator.mul, [math.lgamma(v) for k, v in p_vectors[lang].items()])

        # denominator = 1
        # for k, v in p_vectors[lang].items():
        #     # if math.lgamma(v) == 0:
        #         # print v, math.lgamma(v)
        #     if v > 2:
        #         denominator *= math.lgamma(v)

        #print lang
        #print p_vectors[lang]
        #nominator = reduce(operator.mul, [math.lgamma(v + test_data.get(k, 0)) for k, v in p_vectors[lang].items()])
        #denominator = reduce(operator.mul, [math.lgamma(v) for k, v in test_data.items()])
        
        #print nominator, denominator
        if denominator != 0:
            res = (math.lgamma(A) / math.lgamma(A + N)) * (nominator / denominator)
            # res = (nominator / denominator)
            p_results[lang] = res