# py-estm-model-checker

A model checker for "Even Simpler Tiled Model"

This script generates propositional formulae for a generic map. Eg:

Input:
```
img = [
        'LLLLLLLLLL',
        'LLLLLLLLLL',
        'LLLLLLLLLL',
        'LLLLLLLLLL',
        'LLLLLCLLCC',
        'LLLLCSCCSS',
        'LLLCSSSSSS',
        'LLCSSSSSSS',
        'LCSSSSSSSS',
        'CSSSSSSSSS'
        ]
```

Rules:
```
{
    'L': {
        (1, 0): {'C', 'L'}, 
        (0, 1): {'C', 'L'}, 
        (0, -1): {'C', 'L'}, 
        (-1, 0): {'L'}
        }, 
    'C': {
        (-1, 0): {'L'}, 
        (0, -1): {'C', 'L', 'S'}, 
        (1, 0): {'S'}, 
        (0, 1): {'C', 'L', 'S'}
        }, 
    'S': {
        (-1, 0): {'C', 'S'}, 
        (0, -1): {'C', 'S'}, 
        (1, 0): {'S'}, 
        (0, 1): {'C', 'S'}
        }
    }
```

Output:
```
(C_00 | L_00 | S_00) & (C_10 | L_10 | S_10) & (Equivalent(C_00, S_10 & ~C_10 & ~L_10)) & (Equivalent(C_10, L_00 & ~C_00 & ~S_00)) & (Equivalent(L_00, ~S_10 & (C_10 | L_10))) & (Equivalent(L_10, L_00 & ~C_00 & ~S_00)) & (Equivalent(S_00, S_10 & ~C_10 & ~L_10)) & (Equivalent(S_10, ~L_00 & (C_00 | S_00)))
```

The script was written trying to bridge the gap between Wave Function Collapse (in its "Even Simpler Model" form) to propositional rules, in order to study easy/hard to collapse maps.

A model for the KB inferred from rules is, in fact, a new valid generated map.