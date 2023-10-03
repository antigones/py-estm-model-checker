
from estm_model_checker.estm_rule_parser import ESTMRuleParser
from estm_model_checker.model_checker import models_for_map, format_models

from map_generator.map_generator import maps_from_models,maps_to_worlds


def print_map(m):
    out = list()
    for elm in m:
        contents = [tuple(x)[0] for x in elm]
        out.append("".join(contents))
    print('\n'.join(out))

def main():
    img = [
            '🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳',
            '🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳',
            '🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳',
            '🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳',
            '🌳🌳🌳🌳🌳🐚🌳🌳🐚🌴',
            '🌳🌳🌳🌳🌴🌊🌴🌴🌊🌊',
            '🌳🌳🌳🌴🌊🌊🌊🌊🌊🌊',
            '🌳🌳🌴🌊🌊🌊🌊🌊🌊🌊',
            '🌳🌴🌊🌊🌊🌊🌊🌊🌊🌊',
            '🐚🌊🌊🌊🌊🌊🌊🌊🌊🌊'
            ]


    rule_parser = ESTMRuleParser(img)
    rules,_,literals = rule_parser.calc_rules()

    map_size = (5,5)
    model_ruleset,models,indexed_literals = models_for_map(map_size=map_size, literals=literals, rule_dict=rules)
    print('*** MODEL RULESET ***')
    print(model_ruleset)
    model_list = list(models)
    print('*** MODELS ***')
    print(model_list)
    print('*** MODELS FOR RULESET ***')
    m, sorted_keys = format_models(indexed_literals=indexed_literals, models=model_list)
    print(",".join(sorted_keys))

    for mod in m:
        print(mod)
    
    
    maps_dicts = maps_from_models(model_list=model_list)
    worlds = maps_to_worlds(maps_dicts, map_size)
    print('*** GENERATED MAPS ***')
    for w in worlds:
        print_map(w)
        print()
    
if __name__ == "__main__":
    main()