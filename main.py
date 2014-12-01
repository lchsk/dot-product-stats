import dataset
import dot_product as dot
import util
import bayes
import pearson

# For computing dot product:
#   if set to true, will ignore         p_vectors[lang] = dict((k, v) for k, v in p_vectors[lang].iteritems() if v != 2)when character is present in one set
#   but not in the other
#   if false, will multiply by -1
ignore_when_not_found   = False
decimal_numbers         = 3
current                 = dataset.genesis_spaces

vectors = {}
results = {}

class Method:
    DOT_PRODUCT = 0
    DIRICHLET   = 1
    DIFFERENCE  = 2
    DIRICHLET2  = 3
    PEARSON     = 4

def run(p_method, p_normalise = True, p_reverse_results = True):

    all_dirs = current.train + [current.test]

    for d in all_dirs:
        vectors[d] = {}
        util.read_files(util.get_files(dataset.DATA_DIRECTORY + d), d, vectors)

    if p_normalise:
        util.normalise(vectors)
    
    if p_method == Method.DOT_PRODUCT:
        dot.compute_dot_product(current, vectors, results)
    elif p_method == Method.DIRICHLET:
        bayes.calculate(current, vectors, results)
    elif p_method == Method.DIRICHLET2:
        bayes.cal(current, vectors, results)
    elif p_method == Method.DIFFERENCE:
        dot.compute_difference(current, vectors, results)
    elif p_method == Method.PEARSON:
        pearson.compute(current, vectors, results)

    #bayes.cal(current, vectors, results)

    util.print_results(results, p_reverse_results, decimal_numbers)

if __name__ == '__main__':

    #run(Method.DIRICHLET)
    run(Method.PEARSON)
    print
    run(Method.DIFFERENCE, p_reverse_results = False)
    print
    run(Method.DOT_PRODUCT)