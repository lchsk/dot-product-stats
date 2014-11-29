import dataset
import dot_product as dot
import util
import bayes

# For computing dot product:
#   if set to true, will ignore when character is present in one set
#   but not in the other
#   if false, will multiply by -1
ignore_when_not_found = True
current = dataset.genesis_latin_only

vectors = {}
results = {}

class Method:
    DOT_PRODUCT = 0
    DIRICHLET   = 1

def run(p_method):

    all_dirs = current.train + [current.test]

    for d in all_dirs:
        vectors[d] = {}
        util.read_files(util.get_files(dataset.DATA_DIRECTORY + d), d, vectors)
    util.normalise(vectors)
    
    if p_method == Method.DOT_PRODUCT:
        dot.compute_dot_product(current, vectors, results)
    elif p_method == Method.DIRICHLET:
        bayes.calculate(current, vectors, results)

    util.print_results(results)

if __name__ == '__main__':

    run(Method.DOT_PRODUCT)    
    print
    run(Method.DIRICHLET)