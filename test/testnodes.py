
# This file has been generated at $TIME

from openalea.core import *

def register_packages(pkgmanager):
    
    metainfo = {} 
    pkg = UserPackage("TestLambda", metainfo)

    

    nf = CompositeNodeFactory(name='TestLambda', 
                              description='', 
                              category='Unclassified',
                              doc='',
                              inputs=[],
                              outputs=[],
                              elt_factory={2: ('Catalog.Python', 'range'), 3: ('Catalog.Functional', 'map'), 4: ('Catalog.Math', '+'), 7: ('System', 'lambda var'), 8: ('Catalog.Data', 'int'), 9: ('Catalog.Math', '*')},
                              elt_connections={139960164: (2, 0, 3, 1), 139960200: (7, 0, 4, 0), 139960176: (8, 0, 4, 1), 139960212: (8, 0, 9, 1), 139960152: (4, 0, 9, 0), 139960188: (9, 0, 3, 0)},
                              elt_data={2: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'range', 'posx': 366.25, 'posy': 145.0, 'minimal': False}, 3: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'map', 'posx': 220.0, 'posy': 297.5, 'minimal': False}, 4: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '+', 'posx': 98.75, 'posy': 138.75, 'minimal': False}, 7: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'lambda var', 'posx': 50.0, 'posy': 36.25, 'minimal': False}, 8: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '5', 'posx': 172.5, 'posy': 47.5, 'minimal': False}, 9: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '*', 'posx': 131.25, 'posy': 206.25, 'minimal': False}, '__out__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Out', 'posx': 20.0, 'posy': 250.0, 'minimal': False}, '__in__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'In', 'posx': 20.0, 'posy': 5.0, 'minimal': False}},
                              elt_value={2: [(0, '0'), (1, '10'), (2, '1')], 3: [], 4: [], 7: [(0, "'x'")], 8: [(0, '5')], 9: [], '__out__': [], '__in__': []},
                              lazy=True,
                              )

    pkg.add_factory(nf)


    nf = CompositeNodeFactory(name='LambdaFactoriel', 
                              description='', 
                              category='Unclassified',
                              doc='',
                              inputs=[],
                              outputs=[],
                              elt_factory={2: ('Catalog.Functional', 'reduce'), 3: ('System', 'lambda var'), 4: ('System', 'lambda var'), 5: ('Catalog.Math', '*'), 6: ('Catalog.Python', 'range')},
                              elt_connections={159178632: (4, 0, 5, 1), 159178644: (3, 0, 5, 0), 159178620: (5, 0, 2, 0), 159178608: (6, 0, 2, 1)},
                              elt_data={2: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'reduce', 'posx': 323.75, 'posy': 405.0, 'minimal': False}, 3: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'lambda var', 'posx': 202.5, 'posy': 118.75, 'minimal': False}, 4: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'lambda var', 'posx': 382.5, 'posy': 122.5, 'minimal': False}, 5: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '*', 'posx': 335.0, 'posy': 255.0, 'minimal': False}, 6: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'range', 'posx': 488.75, 'posy': 308.75, 'minimal': False}, '__out__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Out', 'posx': 20.0, 'posy': 250.0, 'minimal': False}, '__in__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'In', 'posx': 20.0, 'posy': 5.0, 'minimal': False}},
                              elt_value={2: [], 3: [(0, "'x'")], 4: [(0, "'x'")], 5: [], 6: [(0, '1'), (1, '10'), (2, '1')], '__out__': [], '__in__': []},
                              lazy=True,
                              )

    pkg.add_factory(nf)


    nf = CompositeNodeFactory(name='testlambdaFor', 
                              description='', 
                              category='Unclassified',
                              doc='',
                              inputs=[],
                              outputs=[],
                              elt_factory={2: ('System', 'lambda var'), 3: ('System', 'for'), 4: ('Catalog.Math', '>='), 5: ('Catalog.Data', 'int'), 6: ('Catalog.Data', 'int'), 7: ('Catalog.Math', '+'), 8: ('Catalog.Data', 'int'), 9: ('System', 'forlist'), 10: ('Catalog.Data', 'list'), 11: ('System', 'lambda var'), 12: ('System', 'lambda var'), 13: ('Catalog.Math', '*'), 14: ('Catalog.Math', '>='), 15: ('Catalog.Data', 'int'), 16: ('Catalog.Math', '+'), 17: ('Catalog.Data', 'int'), 18: ('System', 'annotation'), 19: ('System', 'annotation')},
                              elt_connections={150069056: (14, 0, 9, 1), 150069008: (13, 0, 9, 2), 150069092: (7, 0, 3, 2), 150068972: (10, 0, 9, 0), 150069128: (4, 0, 3, 1), 150069020: (12, 0, 14, 1), 150069068: (17, 0, 14, 0), 150068984: (11, 0, 13, 0), 150069104: (5, 0, 4, 0), 150069032: (2, 0, 4, 1), 150069140: (16, 0, 9, 2), 150068996: (15, 0, 16, 1), 150069080: (2, 0, 7, 0), 150069044: (12, 0, 13, 1), 150068948: (12, 0, 16, 0), 150069116: (8, 0, 3, 0), 150068960: (6, 0, 7, 1)},
                              elt_data={2: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'lambda var', 'posx': 307.5, 'posy': 112.5, 'minimal': False}, 3: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'for', 'posx': 288.75, 'posy': 327.5, 'minimal': False}, 4: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '>=', 'posx': 298.75, 'posy': 217.5, 'minimal': False}, 5: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '10', 'posx': 241.25, 'posy': 150.0, 'minimal': False}, 6: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '3', 'posx': 475.0, 'posy': 176.25, 'minimal': False}, 7: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '+', 'posx': 441.25, 'posy': 258.75, 'minimal': False}, 8: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '0', 'posx': 216.25, 'posy': 247.5, 'minimal': False}, 9: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'forlist', 'posx': 386.25, 'posy': 742.5, 'minimal': False}, 10: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'list', 'posx': 242.5, 'posy': 622.5, 'minimal': False}, 11: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'lambda var', 'posx': 485.0, 'posy': 516.25, 'minimal': False}, 12: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'lambda var', 'posx': 685.0, 'posy': 515.0, 'minimal': False}, 13: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '*', 'posx': 510.0, 'posy': 637.5, 'minimal': False}, 14: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '>=', 'posx': 390.0, 'posy': 618.75, 'minimal': False}, 15: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '1', 'posx': 766.25, 'posy': 613.75, 'minimal': False}, 16: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '+', 'posx': 670.0, 'posy': 650.0, 'minimal': False}, 17: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '10', 'posx': 346.25, 'posy': 553.75, 'minimal': False}, 18: {'txt': 't', 'posx': 728.75, 'posy': 480.0}, 19: {'txt': 'x', 'posx': 530.0, 'posy': 477.5}, '__out__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Out', 'posx': 20.0, 'posy': 250.0, 'minimal': False}, '__in__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'In', 'posx': 20.0, 'posy': 5.0, 'minimal': False}},
                              elt_value={2: [(0, "'x'")], 3: [], 4: [], 5: [(0, '10')], 6: [(0, '3')], 7: [], 8: [(0, '0')], 9: [], 10: [(0, '[1, 1]')], 11: [(0, "'x'")], 12: [(0, "'x'")], 13: [], 14: [], 15: [(0, '1')], 16: [], 17: [(0, '10')], 18: [], 19: [], '__out__': [], '__in__': []},
                              lazy=True,
                              )

    pkg.add_factory(nf)


    nf = CompositeNodeFactory(name='testorder', 
                              description='', 
                              category='Unclassified',
                              doc='',
                              inputs=[],
                              outputs=[],
                              elt_factory={2: ('Catalog.Data', 'float'), 3: ('Catalog.Data', 'float'), 4: ('Catalog.Data', 'list')},
                              elt_connections={154750856: (2, 0, 4, 0), 154750868: (3, 0, 4, 0)},
                              elt_data={3: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'float', 'posx': 60.0, 'posy': 116.25, 'minimal': False}, 2: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'float', 'posx': 225.0, 'posy': 112.5, 'minimal': False}, '__in__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'In', 'posx': 20.0, 'posy': 5.0, 'minimal': False}, 4: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'list', 'posx': 71.25, 'posy': 195.0, 'minimal': False}, '__out__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Out', 'posx': 20.0, 'posy': 250.0, 'minimal': False}},
                              elt_value={3: [(0, '0.0')], 2: [(0, '0.0')], '__in__': [], 4: [], '__out__': []},
                              lazy=True,
                              )

    pkg.add_factory(nf)


    nf = CompositeNodeFactory(name='testlambda2', 
                              description='', 
                              category='Unclassified',
                              doc='',
                              inputs=[],
                              outputs=[],
                              elt_factory={2: ('Catalog.Python', 'range'), 4: ('Catalog.Math', '>='), 5: ('Catalog.Math', 'and'), 6: ('Catalog.Math', '>='), 7: ('System', 'lambda var'), 8: ('Catalog.Data', 'int'), 9: ('Catalog.Data', 'int'), 10: ('Catalog.Functional', 'filter')},
                              elt_connections={140115776: (7, 0, 6, 0), 140115812: (4, 0, 5, 0), 140115848: (5, 0, 10, 0), 140115788: (8, 0, 6, 1), 140115824: (6, 0, 5, 1), 140115860: (2, 0, 10, 1), 140115800: (7, 0, 4, 1), 140115836: (9, 0, 4, 0)},
                              elt_data={2: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'range', 'posx': 493.75, 'posy': 230.0, 'minimal': False}, 4: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '>=', 'posx': 143.75, 'posy': 212.5, 'minimal': False}, 5: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'and', 'posx': 233.75, 'posy': 307.5, 'minimal': False}, 6: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '>=', 'posx': 266.25, 'posy': 215.0, 'minimal': False}, 7: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'lambda var', 'posx': 175.0, 'posy': 107.5, 'minimal': False}, 8: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '2', 'posx': 297.5, 'posy': 118.75, 'minimal': False}, 9: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '7', 'posx': 113.75, 'posy': 133.75, 'minimal': False}, 10: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'filter', 'posx': 345.67901234567898, 'posy': 376.54320987654313, 'minimal': False}, '__out__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Out', 'posx': 20.0, 'posy': 250.0, 'minimal': False}, '__in__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'In', 'posx': 20.0, 'posy': 5.0, 'minimal': False}},
                              elt_value={2: [(0, '0'), (1, '10'), (2, '1')], 4: [], 5: [], 6: [], 7: [(0, "'x'")], 8: [(0, '2')], 9: [(0, '7')], 10: [], '__out__': [], '__in__': []},
                              lazy=True,
                              )

    pkg.add_factory(nf)


    nf = CompositeNodeFactory(name='testlambda3', 
                              description='', 
                              category='Unclassified',
                              doc='',
                              inputs=[],
                              outputs=[],
                              elt_factory={2: ('Catalog.Data', 'list'), 3: ('Catalog.Functional', 'map'), 4: ('System', 'lambda var'), 6: ('Catalog.Math', '>='), 7: ('System', 'lambda var'), 8: ('Catalog.Data', 'int'), 9: ('Catalog.Functional', 'filter')},
                              elt_connections={145370980: (2, 0, 3, 1), 145371016: (9, 0, 3, 0), 145370992: (4, 0, 9, 1), 145371028: (6, 0, 9, 0), 145370968: (8, 0, 6, 1), 145371004: (7, 0, 6, 0)},
                              elt_data={2: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'list', 'posx': 433.75, 'posy': 286.25, 'minimal': False}, 3: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'map', 'posx': 345.0, 'posy': 368.75, 'minimal': False}, 4: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'lambda var', 'posx': 376.25, 'posy': 172.5, 'minimal': False}, 6: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '>=', 'posx': 266.25, 'posy': 215.0, 'minimal': False}, 7: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'lambda var', 'posx': 175.0, 'posy': 107.5, 'minimal': False}, 8: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '7', 'posx': 297.5, 'posy': 118.75, 'minimal': False}, 9: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'filter', 'posx': 290.0, 'posy': 278.75, 'minimal': False}, '__out__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Out', 'posx': 20.0, 'posy': 250.0, 'minimal': False}, '__in__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'In', 'posx': 20.0, 'posy': 5.0, 'minimal': False}},
                              elt_value={2: [(0, '[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]')], 3: [], 4: [(0, "'x'")], 6: [], 7: [(0, "'x'")], 8: [(0, '7')], 9: [], '__out__': [], '__in__': []},
                              lazy=True,
                              )

    pkg.add_factory(nf)


    pkgmanager.add_package(pkg)


