import toolbox

functions = [
    [toolbox.euler_characteristic_chief, {'ec':{}}],
    [toolbox.tribe_size, {'ts':{}}],
    [toolbox.degree, {'degree':{}}],
    [toolbox.in_degree, {'in_degree':{}}],
    [toolbox.out_degree, {'out_degree':{}}],
    [toolbox.reciprocal_connections, {
        'rc':{},
        'rc_chief':{'chief_only':True}
        }
    ],
    [toolbox.tcc, {'tcc':{}}],
    [toolbox.ccc, {'ccc':{}}],
    [toolbox.asg_radius, {'asg_radius':{}}],
    [toolbox.asg, {'asg_high':{'gap':'high'},
                   'asg_low':{'gap':'low'}
                  }
    ],
    [toolbox.tpsg_radius, {'tpsg_radius':{}}],
    [toolbox.tpsg, {'tpsg_high':{'gap':'high'},
                       'tpsg_low':{'gap':'low'}
                   }
    ],
    [toolbox.clsg_radius, {'clsg_radius':{}}],
    [toolbox.clsg, {'clsg_high':{'gap':'high'},
                       'clsg_low':{'gap':'low'}
                   }
    ],
    [toolbox.blsg_radius, {'blsg_radius':{}}],
    [toolbox.blsg, {'blsg_high':{'gap':'high'},
                       'clsg_low':{'gap':'low'}
                   }
    ],
    [toolbox.nbc, {'nbc':{}}],
    [toolbox.dc, {'dc2':{'coeff_index':2},
                     'dc3':{'coeff_index':3},
                     'dc4':{'coeff_index':4},
                     'dc5':{'coeff_index':5},
                     'dc6':{'coeff_index':6}
                 }
    ],
    [toolbox.number_of_n_degree_nodes, {'0_out_degree_amount':{'n':0, 'which':'out'},
                                        '1_out_degree_amount':{'n':1, 'which':'out'},
                                        '0_in_degree_amount':{'n':0, 'which':'in'},
                                        '1_in_degree_amount':{'n':1, 'which':'in'}
                                        }],
    [toolbox.average_degree, {'average_in_degree':{'which':'in'},
                              'average_out_degree':{'which':'out'},}],
    [toolbox.average_in_tribe_indegree, {'average_in_tribe_degree':{}}],
    [toolbox.edge_boundary, {'edge_boundary':{}}],
    [toolbox.edge_volume, {'edge_volume':{}}],
    [toolbox.cell_counts, {'cell_counts':{}}],
    [toolbox.connected_components, {'conn_comps':{}}],
]

tribe_args = {'which':'in', 'exclude_chief':True}
out_dir = '/gpfs/bbp.cscs.ch/project/proj9/bisimplices/santoro/TriDy/results_in_tribe/'


for function in functions:
    for name, kwargs in function[1].items():
        print('Processing ' + name + '...')
        try:
            toolbox.recompute_single(function[0], name, out_dir, tribe_args = tribe_args, **kwargs)
        except FileExistsError as exception:
            print(exception)
