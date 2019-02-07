from proof_printing import build_params, BEGIN_CONSISTENCY, END_CONSISTENCY, print_proof, FALSITY, abduced_list


def metabolism(lac, exp):
    return "metabolism" + build_params([lac, exp])


def produce(enz, exp):
    return "produce" + build_params([enz, exp])


def expressed(lac, exp):
    return "expressed" + build_params([lac, exp])


def concentration(lac, hl, exp):
    return "concentration" + build_params([lac, hl, exp])

def gene_code(g, p):
    return "geneCode" + build_params([g, p])


lactose = "lactose"
exp1 = "exp1"
p1 = "p1"
g1 = "g1"
G = "G"
lacy = "lacy"
high = "high"
glucose = "glucose"
low = "low"
lacz = "lacz"
