import json
import settings

# стандартный питоновский модуль ура

# задача: понять, какие типы заведений собраны в этом выгруженном датасете

with open('data-4275-2018-04-10.json', encoding='cp1251') as allpl:
	moscow_foodplaces = json.load(allpl)

	# json.load - чтобы json нормально выгрузился, списком со словарями, а не чем-то другим

	# print(moscow_foodplaces)

	places_types = set()

	for place in moscow_foodplaces:
		object_type = place.get('TypeObject')		
		places_types.add(str(object_type))
			
	print(places_types)

