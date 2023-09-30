import random as rd
from estm_model_checker.utils import get_neighbours
from sympy.logic.inference import satisfiable
from sympy.logic.boolalg import Equivalent
from sympy import Symbol
from sympy import Or,And, Not


def format_models(models):
    m = []
    sorted_keys = []
    for model in models:
        if model:
            sorted_dict = dict(sorted(model.items(), key=lambda i: str(i[0]).split('_')[::-1]))
            sorted_values = list(sorted_dict.values())
            m.append(sorted_values)
            sorted_keys = [str(key) for key, value in sorted_dict.items()]
    return m, sorted_keys
        
def generate_rules(map_size, literals, rule_dict):
    indexed_literals = []
    indexed_ruleset = dict()
    uniqueness_rules = []
    height,width = map_size
    for literal in literals:
        for i in range(height):
            for j in range(width):
                indexed_literal = Symbol(f"{literal}_{i}{j}")
                indexed_literals.append(indexed_literal)
                uniqueness_rules.append([Symbol(f"{u}_{i}{j}") for u in literals])
                neighbours = get_neighbours(i,j,height,width)
                or_rule = []
                for n in neighbours:
                    nx,ny = n
                    rx,ry = nx - i, ny - j
                    if (rx,ry) in rule_dict[literal].keys():
                        vinculi = rule_dict[literal][(rx,ry)]
                        indexed_vinculi = [Symbol(f"{v}_{nx}{ny}") for v in vinculi]
                        to_exclude = set(literals).difference(vinculi)
                        not_vinculi = [Not(Symbol(f"{e}_{nx}{ny}")) for e in to_exclude]
                        if not_vinculi:
                            v_or = And(Or(*indexed_vinculi),*not_vinculi)
                        else:
                            v_or = Or(*indexed_vinculi)
                    else:
                        # no value for tile is admissible here
                        no_tile_vinculi = [Not(Symbol(f"{l}_{nx}{ny}")) for l in literals]
                        v_or = And(*no_tile_vinculi)
                    or_rule.append(v_or)                           
                if or_rule:
                   indexed_ruleset[indexed_literal] = And(*or_rule)
                
    iif_ruleset = []
    for k,v in indexed_ruleset.items():
        iif_ruleset.append(Equivalent(k,v))

    for u_rule in uniqueness_rules:
        iif_ruleset.append(Or(*u_rule))
    model_ruleset = And(*iif_ruleset)
    return model_ruleset

def models_for_map(map_size, literals, rule_dict):
    model_ruleset = generate_rules(map_size=map_size, literals=literals, rule_dict=rule_dict)
    models = satisfiable(model_ruleset, all_models=True)
    return model_ruleset, models

def pretty_print(model:dict, size):
    height, width = size
    m = [['' for col in range(width)] for row in range(height)]
    for k,v in model.items():
        splitted_symbol = str(k).split('_')
        indices = splitted_symbol[::-1][0]
        literal = list(splitted_symbol[0])
        chosen_literal = rd.choices(population=literal,k=1)
        split_idx = len(indices)//2
        x,y=int(indices[:split_idx]),int(indices[split_idx:])
        if v:
            # add literal
            m[x][y] = chosen_literal[0]
    return m



