BEGIN_CONSISTENCY = "bgcnstny"
END_CONSISTENCY = "endcnstny"
FALSITY = "■"


def print_proof(lines):
    indent = 1
    for line in lines:
        if line == BEGIN_CONSISTENCY:
            indent += 1
        elif line == END_CONSISTENCY:
            indent -= 1
        elif line[0] == FALSITY:
            print_indent(indent)
            print(FALSITY, "\t", line[1], "\n")
        else:
            print_indent(indent)
            print("⟵ ", end="")
            for i in range(len(line) - 1):
                print(line[i] + ", ", end="")
            print(line[len(line) - 1])
            # Leave space to hand draw vertical bars
            print()
            # Print bars below all ⟵
            # print_indent(indent)
            # print("|")


def print_indent(indent):
    for i in range(indent):
        print("\t", end="")


def build_params(params):
    string = "("
    string = append_list_to_string(params, string)
    return string + ")"


def succesful_consistency_check(all_abduced):
    return [FALSITY, abduced_list(all_abduced)]


def abduced_list(abduced):
    string = "\t△ = {"
    string = append_list_to_string(abduced, string)
    return string + "}"


def append_list_to_string(abduced, string):
    for i in range(len(abduced) - 1):
        string += abduced[i] + ", "
    string = string + abduced[len(abduced) - 1]
    return string


def not_(predicate):
    return "not " + predicate
