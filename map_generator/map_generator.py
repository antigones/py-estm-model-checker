
from collections import defaultdict
import itertools

def maps_from_models(model_list):
    possible_tiles_for_indices = list()
    maps = list()
    for m in model_list:
        str_dict = {str(k):v for k,v in m.items()}
        out_dict = defaultdict(set)
        for k,v in str_dict.items():
            if v:
                splitted_symbol = str(k).split('_')
                indices = splitted_symbol[::-1][0]
                literal = splitted_symbol[0]
                split_idx = len(indices)//2
                x,y=int(indices[:split_idx]),int(indices[split_idx:])
                out_dict[(x,y)].add(literal)
        possible_tiles_for_indices.append(out_dict)
   
    for p_tiles in possible_tiles_for_indices:
        keys, values = zip(*p_tiles.items())
        permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]
        maps.append(permutations_dicts)
    maps = sum(maps,[])
    return maps

def maps_to_worlds(maps_dicts, worlds_size):
    height, width = worlds_size
    world= [['' for col in range(width)] for row in range(height)]
    world_list = list()
    for map_dict in maps_dicts:
        world= [['' for col in range(width)] for row in range(height)]
        for k,v in map_dict.items():
            x,y = k
            world[x][y]= v
            
        world_list.append(world)
    return world_list
