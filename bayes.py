import math
import operator

def dirichlet(x, alpha):
    nominator = reduce(operator.mul, [x[i]**(alpha[i]-1.0) for i in range(len(alpha))])
    denominator = reduce(operator.mul, [math.gamma(a) for a in alpha]) / (math.gamma(sum(alpha)))
    
    return (nominator / denominator)

def multinomial(n, P, X):
    denominator = reduce(operator.mul, [math.factorial(x) for x in X])
    nominator = math.factorial(n) * reduce(operator.mul, [P[i] ** X[i] for i in range(len(P))])

    return nominator / denominator


def calculate(p_dataset, p_vectors, p_results):

    #product = 0
    test_data = p_vectors[p_dataset.test]

    for lang in p_dataset.train:
        arr = [v for k, v in p_vectors[lang].items()]
        test = [v for k, v in test_data.items()]
        test2 = [round(1 * v) for k, v in test_data.items()]

        likelihood_v = multinomial(1, test, test2)

        prior_v = dirichlet(arr, arr)
        norm = reduce(operator.add, arr)
        #print arr
        norm /= len(arr)
        print norm

        res = (prior_v * likelihood_v) / norm

        p_results[lang] = res