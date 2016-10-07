# -*- coding: utf-8 -*-

startingBalance = 50000

cocktails = [
    {
        'name': 'Cocktail A',
        'img': 'cocktail1.png',
        'price': 150, #Eur / L
        'growth': 0.2, # 20% per day
        'growthParameters': "[0.21, 0.20, 0.18]", #json
        'fieldId': 'GR_P',
    },
    {
        'name': 'Cocktail B',
        'img': 'cocktailB.png',
        'price': 210, #Eur / L
        'growth': 0.25, # 25% per day
        'growthParameters': "[0.27, 0.25, 0.20]", #json
        'fieldId': 'GR_P',
    }
]



market = [
    {
        'name': 'Incubator',
        'tooltip': '',
        'img': '',
        'fieldId': 'TOTAL_INCUBATORS',
        'price': 15000
    },
    {
        'name': 'Worker',
        'tooltip': 'operates the equipment',
        'img': '',
        'fieldId': 'TOTAL_WORKERS',
        'price': 1000,
        'priceDescription': '50€/day'
    },
    {
        'name': 'Safety Cabinet',
        'tooltip': '',
        'img': '',
        'fieldId': 'TOTAL_BSC',
        'price': 12000
    },
    {
        'name': 'Bioreactor',
        'tooltip': '',
        'img': '',
        'fieldId': 'TOTAL_BIOREACTORS',
        'price': 56000
    }
]

def get_asset(fieldId):

    for item in market:
        if fieldId == item['fieldId']:
            return item

    raise Exception("Item Not Found {}".format(fieldId))
