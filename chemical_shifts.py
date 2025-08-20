chemical_shifts = {
    'alpha Adenosine triphosphate': {
        'symbol': 'ATPα',
        'value': -7.56
    }, 
    'beta Adenosine triphosphate': {
        'symbol': 'ATPβ',
        'value': -16.15
    }, 
    'gamma Adenosine triphosphate': {
        'symbol': 'ATPγ',
        'value': -2.53
    },
    'Phosphocreatine': {
        'symbol': 'PCr',
        'value': 0.0
    },
    'Inorganic phosphate': {
        'symbol': 'Pi',
        'value': 4.82
    }, 
    'Nicotinamide adenine dinucleotide (oxygenated)':{
        'symbol': 'NAD+',
        'value': -8.31
    },
    'Nicotinamide adenine dinucleotide (reduced)':{
        'symbol': 'NADH',
        'value': -8.13
    },
    'Membrane phospholipid':{
        'symbol': 'MP',
        'value': 2.30
    },
    'Glycero-3-phosphorylcholine':{
        'symbol': 'GPC',
        'value': 2.94
    },
    'Glycero-3-phosphorylethanolamine':{
        'symbol': 'GPE',
        'value': 3.50
    },
    'Phosphorylcholine':{
        'symbol': 'PC (PDE)',
        'value': 6.23
    },
    'Phosphorylethanolamine': {
        'symbol': 'PE (PDE)',
        'value': 6.77
    },
    '2.3-diphosphoglycerate_d:':{
        'symbol': 'DPG_d',
        'value': 5.71
    },
    '2.3-diphosphoglycerate_t:':{
        'symbol': 'DPG_t',
        'value': 5.23
    },
}

short_list = ['PCr', 'Pi', 'ATPα', 'ATPβ', 'ATPγ', 'NAD+', 'NADH', 'MP', 'GPC', 'GPE', 'PC (PDE)', 'PE (PDE)', 'DPG']
cs = []
for metabolites, details in chemical_shifts.items():
    for symbol in short_list:
        if symbol in details['symbol']:
            # print(metabolites)
            cs.append(details['value'])
