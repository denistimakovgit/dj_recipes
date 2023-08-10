from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet_recipe(request):
    servings = int(request.GET.get("servings", 1))
    if servings == 1:
        context = {
            'recipe': DATA['omlet']
        }
    else:
        for key, value in DATA['omlet'].items():
            value = value * servings
            DATA['omlet'][key] = value
            context = {
                'recipe': DATA['omlet']
            }
    return render(request, 'index.html', context)

def pasta_recipe(request):
    servings = int(request.GET.get("servings", 1))
    if servings == 1:
        context = {
            'recipe': DATA['pasta']
        }
    else:
        for key, value in DATA['pasta'].items():
            value = value * servings
            DATA['pasta'][key] = value
            context = {
                'recipe': DATA['pasta']
            }
    return render(request, 'index.html', context)