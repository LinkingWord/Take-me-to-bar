# -*- coding: utf8 -*-
# проект признана провальным, потому что одновременно можно выгружать по апи только 500 мест
# а это нам не подходит, не говоря уже о том, насколько все медленно

import requests


def get_places(url):
	result = requests.get(url)
	print(result.status_code)
	print(result.text)

	# places_list = result.json()
	# # places_list = [{"global_id":637376221,"Number":1,"Cells":{"global_id":637376221,"Name":"СМЕТАНА","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"кафе","AdmArea":"Северо-Восточный административный округ","District":"Ярославский район","Address":"улица Егора Абакумова, дом 9","PublicPhone":[{"PublicPhone":"(499) 183-14-10"}],"SeatsCount":48,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.714565000436039,55.879001531303373]}}},{"global_id":637376331,"Number":2,"Cells":{"global_id":637376331,"Name":"Родник","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"кафе","AdmArea":"Центральный административный округ","District":"Таганский район","Address":"улица Талалихина, дом 2/1, корпус 1","PublicPhone":[{"PublicPhone":"(495) 676-55-35"}],"SeatsCount":35,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.6733061300344,55.7382386551547]}}},{"global_id":637376349,"Number":3,"Cells":{"global_id":637376349,"Name":"Кафе «Академия»","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"кафе","AdmArea":"Центральный административный округ","District":"Таганский район","Address":"Абельмановская улица, дом 6","PublicPhone":[{"PublicPhone":"(926) 841-45-78"}],"SeatsCount":95,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.6696475969381,55.7355114718314]}}},{"global_id":637376381,"Number":4,"Cells":{"global_id":637376381,"Name":"ПИЦЦЕТОРИЯ","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"кафе","AdmArea":"Северо-Восточный административный округ","District":"район Лианозово","Address":"Абрамцевская улица, дом 1","PublicPhone":[{"PublicPhone":"(499) 200-17-09"}],"SeatsCount":40,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.5733294712098,55.8919565397311]}}},{"global_id":637376403,"Number":5,"Cells":{"global_id":637376403,"Name":"Кафе «Вишневая метель»","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"кафе","AdmArea":"Северо-Восточный административный округ","District":"район Лианозово","Address":"Абрамцевская улица, дом 9, корпус 1","PublicPhone":[{"PublicPhone":"(499) 200-00-22"}],"SeatsCount":50,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.57230613167112,55.90408636984904]}}},{"global_id":637376480,"Number":6,"Cells":{"global_id":637376480,"Name":"СТОЛ. ПРИ ГОУ СОШ № 1051","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"столовая","AdmArea":"Северо-Восточный административный округ","District":"район Лианозово","Address":"Абрамцевская улица, дом 15, корпус 1","PublicPhone":[{"PublicPhone":"(499) 908-06-15"}],"SeatsCount":240,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.571524892243922,55.906797658683253]}}},{"global_id":637376481,"Number":7,"Cells":{"global_id":637376481,"Name":"Брусника","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"кафе","AdmArea":"Центральный административный округ","District":"район Арбат","Address":"город Москва, переулок Сивцев Вражек, дом 6/2","PublicPhone":[{"PublicPhone":"(495) 697-04-89"}],"SeatsCount":10,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.59812754843999,55.747390490525994]}}},{"global_id":637376500,"Number":8,"Cells":{"global_id":637376500,"Name":"Буфет МТУСИ","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"столовая","AdmArea":"Юго-Восточный административный округ","District":"район Лефортово","Address":"Авиамоторная улица, дом 8, строение 1","PublicPhone":[{"PublicPhone":"(495) 673-89-78"}],"SeatsCount":90,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.71542539189803,55.755163750970688]}}},{"global_id":637376534,"Number":9,"Cells":{"global_id":637376534,"Name":"КПФ СЕМЬЯ-1","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"столовая","AdmArea":"Юго-Восточный административный округ","District":"район Лефортово","Address":"Авиамоторная улица, дом 8, строение 1","PublicPhone":[{"PublicPhone":"(495) 273-89-78"}],"SeatsCount":150,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.71542539189803,55.755163750970688]}}},{"global_id":637376536,"Number":10,"Cells":{"global_id":637376536,"Name":"Столовая МТУСИ","IsNetObject":"нет","OperatingCompany":None,"TypeObject":"столовая","AdmArea":"Юго-Восточный административный округ","District":"район Лефортово","Address":"Авиамоторная улица, дом 8, строение 1","PublicPhone":[{"PublicPhone":"(495) 273-89-78"}],"SeatsCount":120,"SocialPrivileges":"нет","geoData":{"type":"Point","coordinates":[37.71542539189803,55.755163750970688]}}}]
	
	# places_types = set()

	# for place in places_list:
	# 	object_type = place.get('Cells').get('TypeObject')
	# 	places_types.add(str(object_type))
			
	# print(places_types)



if __name__ == '__main__':
	get_places('https://apidata.mos.ru/v1/datasets/1903/rows?api_key=DATA_MOS_APIKEY&$top=10000')