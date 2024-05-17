#!/usr/bin/python3
"""Serialise outfit items data to json files"""

import json

# Dictionary of clothing items of the top category
outfit_tops_dict = {
    'casual': {
        'male': ['t-shirt',
                ['round-necked sweater', 'collared shirt'],
                'plain top',
                'polo shirt',
                'casual button-down shirt',
                'flannel shirt',
                'oxford shirt',
                'rugby shirt',
                'baseball shirt',
                ['t-shirt', 'hoodie'],
                'crewneck sweater',
                ['V-neck sweater', 'button-down shirt'],
                ['button-down shirt', 'cardigan'],
                'tank top',
                'rugby shirt',
                'turtle-neck sweater',
                'raglan-sleeved baseball shirt',
                'camp shirt',
                'denim shirt',
                'linen shirt',
                ['fleece jacket', 't-shirt']
                ],

        'female': ['plain blouse',
                  ['sleeveless top', 'shawl'],
                   'turtle-necked top',
                   'camisole',
                   'crop top',
                   'button-down shirt',
                   'tunic',
                   'off-the-shoulder top',
                   'cold shoulder top',
                   'halter top',
                   'wrap top',
                   'kimono top',
                   ['camisole', 'cardigan'],
                   ['v-neck sweater', 'turtle-neck top'],
                   ['v-neck sweater', 'round-neck blouse'],
                   'denim shirt',
                   'flannel shirt',
                   ['flannel shirt', 'camisole'],
                   'ruffled blouse',
                   'bell-sleeve blouse',
                   'peplum top',
                   'one-shoulder top',
                   'polo shirt',
                   'crochet top',
                   'satin top',
                   'linen top',
                   ]
        },
    'dinner': {
        'male': ['silk button-down shirt',
                 'plaid T-shirt',
                 'dress shirt, tie',
                 'henley shirt',
                 'oxford shirt',
                 'flannel shirt',
                 ['v-neck sweater', 'button-down shirt'],
                 ['blazer', 'dress shirt'],
                 ['sport coat', 'button-down shirt'],
                 ['waist coat and tie', 'long-sleeved shirt'],
                 'turtle-neck sweater',
                 'mock neck sweater',
                 'silk polo shirt',
                 'patterned shirt',
                 'dinner suit',
                 'cashmere sweater'
                 ],
        'female': ['flowered blouse',
                   'dressy blouse',
                   'top with flared sleeves',
                   ['silk camisole', 'blazer'],
                   ['satin camisole', 'jacket'],
                   'off-the-shoulder top',
                   'wrap top',
                   'peplum top',
                   'lace top',
                   'sequin top',
                   'ruffled blouse',
                   'halter top',
                   'one-shoulder top',
                   'draped top',
                   'bell-sleeve blouse',
                   'embroidered top',
                   'crochet top',
                   'turtle-neck top',
                   'v-neck top',
                   'button-down shirt',
                   'wool cardigan',
                   'cape top',
                   'boat-neck top'
                   ]
        },
    'exercise': {
        'male': ['sweatshirt',
                 'sleeveless top'
                 'tank top',
                 'long-sleeve performance shirt'
                 'hoodie',
                 'sweatshirt',
                 'muscle tank',
                 'polo shirt',
                 'baseball shirt',
                 'running singlet',
                 'cycling jersey',
                 'compression tank top',
                 'running hoodie',
                 'yoga top',
                 'track jacket',
                 'sleeveless hoodie',
                 'mesh shirt'
                 ],
        'female': ['sleeveless breathable top',
                   'light long-sleeved cotton blouse',
                   'sports bra',
                   'cycling jersey',
                   'sleeveless top',
                   'tank top',
                   'compression tank top',
                   'running hoodie',
                   'yoga top',
                   'track jacket',
                   'sleeveless hoodie',
                   'mesh shirt'
                   ]
    }
}

# Dictionary of clothing items of the bottom category
outfit_bottoms_dict = {
    'casual': {
        'male': ['jean trousers',
                 'cargo pants',
                 'khaki shorts',
                 'chinos',
                 'track pants',
                 'denim shorts',
                 'cargo shorts',
                 'joggers',
                 'linen pants',
                 'dress pants',
                 'jorts',
                 'wool trousers',
                 'harem pants',
                 'yoga pants',
                 'cycling shorts',
                 'leather pants'
                 ],
        'female': ['flared skirt',
                   'straight skirt',
                   'leggings',
                   'boyfriend jeans',
                   'bootcut jeans',
                   'flared jeans',
                   'leggings',
                   'chinos',
                   'cargo pants',
                   'khakis',
                   'sweatpants',
                   'shorts',
                   'midi skirt',
                   'pencil skirt',
                   'maxi skirt',
                   'pleated skirt',
                   'palazzo pants',
                   'jeggings',
                   'bike shorts',
                   'leather pants',
                   'linen trousers',
                   'denim skirt',
                   'wrap skirt'
                   ]
        },
    'dinner': {
        'male': ['pants trousers',
                 'silk trousers',
                 'suit trousers',
                 'corduroy pants',
                 'tweed trousers',
                 'linen pants',
                 'denim jeans',
                 'pleated pants',
                 'leather pants',
                 'flannel-lined pants',
                 'satin pants'
                ],
        'female': ['skirt',
                   'flared skirt',
                   'dress pants',
                   'palazzo pants',
                   'maxi skirt',
                   'midi skirt',
                   'pencil skirt',
                   'high-waisted skirt',
                   'sequin pants',
                   'velvet skirt',
                   'velvet pants',
                   'lace skirt',
                   'high-waisted wide-leg pants',
                   'tuxedo pants',
                   'crochet skirt'
                   ]
        },
    'exercise': {
        'male': ['3/4 shorts',
                 'athletic shorts',
                 'athletic leggings',
                 'track pants',
                 'joggers',
                 'training shorts',
                 'cycling shorts',
                 'sweatpants',
                 'yoga pants',
                 'basketball pants',
                 'hiking pants',
                 'running tights',
                 'spandex shorts',
                 'thermal leggings'
                 ],
        'female': ['biker shorts',
                   'leggings',
                   'yoga pants',
                   'running shorts',
                   'athletic shorts',
                   'capri leggings',
                   'cycling shorts',
                   'joggers',
                   'track pants',
                   'training shorts',
                   'skorts',
                   'high-waisted leggings',
                   'dance shorts',
                   'running tights',
                   'spandex shorts'
                   ]
    }
}


# Dictionary if formal clothing items
formal_outfits_dict = {
    'female': [
        [['suit skirt'],['suit']],
        [['tights'], ['evening gown']],
        [['tights'], ['cocktail dress']],
        [['tights'], ['ball gown']],
        [['tights'], ['sheath dress']],
        [['tights'], ['A-line dress']],
        [['tights'], ['empire waist dress']],
        [['tights'], ['wrap dress']],
        [['tights'], ['peplum dress']],
        [['tights'], ['halter dress']],
        [['tights'], ['lace gown']],
        [['tailored trousers'], ['blazer']],
        [['tailored skirt'], ['blazer']],
        [['plaid skirt'], ['jacket', 'camisole']]
        ],
    'male': [
        [['trousers'], ['tuxedo']],
        [['trousers'], ['suit', 'shirt']],
        [['trousers'], ['three-piece suit']],
        [['black trousers'], ['dinner jacket']],
        [['formal trousers'], ['tailcoat']],
        [['trousers'], ['double-breasted suit']],
        [['trousers'], ['velvet dinner jacket']]
        ]
}

# Hold status of user- if the app is being used for the first time
# to enable user registration page
status_dict = {'new': 'yes'}

# Serialize all dictionaries into their respective json files"
#with open ("json_files/colours.json", "w") as json_colour:
#    json.dump(colours_dict, json_colour, indent = 3)
with open ("json_files/tops.json", "w") as json_top:
    json.dump(outfit_tops_dict, json_top, indent = 3)
with open ("json_files/bottoms.json", "w") as json_bottom:
    json.dump(outfit_bottoms_dict, json_bottom, indent = 3)
with open ("json_files/formal_outfits.json", "w") as json_formal:
    json.dump(formal_outfits_dict, json_formal, indent = 3)
with open ("json_files/status.json", "w") as json_status:
    json.dump(status_dict, json_status, indent = 3)

"""
colours_dict = dict({
    "red" : "255,0,0" ,  # RGB Hex Code for Red
    "green": "0,128,0", # RGB Hex Code for Green
    "blue": "0,0,255",  # RGB HEX Code for Blue
    "white": "255,255,255",   # RGB Hex Code for White
    "black": "0,0,0",          # RGB Hex Code for Black
    "yellow": "255,255,0",     # Yellow Color in RGB
    "navl blue":  "0,68,174", # Navy Blue color in RGB
    "gold": "255,193,0",
    "pink": "255,192,203",
    "orange": "255,165,0",
    "cyan": "0,255,255",
    "magenta": "255,0,255",
    "brown": "165,42,42",
    "lime": "0,255,0",
    "purple": "128,0,128",
    "tan": "210,180,140",
    "teal": "0,128,128",
    "olive": "128,128,0",
    "light brown": "181,101,29",
    "bronze": "205,127,50",
    "ochre": "204,119,34",
    "black bean": "61,12,2",
    "dark salmon": "233,150,122",
    "chocolate": "210,105,30",
    "sky blue": "135,206,235",
    "royal blue": "65,105,225",
    "dark blue": "0,0,139",
    "cobalt": "0,71,171",
    "imperial blue": "0,35,149",
    "grey": "128,128,128",
    "light grey": "211,211,211",
    "violet": "143,0,255",
    "indigo": "75,0,130",
})
"""
