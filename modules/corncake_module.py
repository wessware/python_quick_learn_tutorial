def make_uji(size, *ingridients):
    print('Preparing ' + size + ' amount of porridge.')
    print('Ingridients:')
    for ingridient in ingridients:
        print('- ' + ingridient)


make_uji('small', 'flour', 'water')
make_uji('small', 'sorghum', 'cassava', 'water')
make_uji('large', 'maize_grade_1', 'water', 'peanuts', 'coconut_milk')


def uji_recipes(size, water_amount, **additionals):
    required_ings = {'size': size, 'water': water_amount}

    for key, value in additionals.items():
        required_ings[key] = value

    return required_ings


recipe_1 = uji_recipes('medium', '0.7 litres', flour='600g')
recipe_2 = uji_recipes('large', '2.5 litres', maize_flour='600g',
                       wheat_flour='200g', peanut_flour='100g', coconut_milk='800ml')

print(recipe_1)
print(recipe_2)
