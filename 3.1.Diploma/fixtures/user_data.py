
raw_user = {'id': 2998414, 'first_name': 'Назар', 'last_name': 'Вотяков', 'is_closed': False, 'can_access_closed': True, 'sex': 2, 'domain': 'obladaet', 'city': {'id': 2, 'title': 'Санкт-Петербург'}, 'country': {'id': 1, 'title': 'Россия'}, 'common_count': 0, 'track_code': 'e7a1ff0c1adOp2tEvVbjBOZgpyLyTfVIJDV0xfl-xxE40To3-OCyzg_zYCK-V-sL3fMbk3Eqgkw1Lw'}


expect_user = {'id': 2998414, 'first_name': 'Назар', 'last_name': 'Вотяков', 'is_closed': False, 'can_access_closed': True, 'sex': 2, 'domain': 'obladaet', 'city': 2, 'country': 1, 'common_count': 10, 'interests': '', 'music': '', 'movies': '12 Angry Men', 'books': 'Достоевский'}


filtered_data = [{'id': 33514697, 'score': 180}, {'id': 2975227, 'score': 160}, {'id': 18607246, 'score': 112}, {'id': 3485494, 'score': 80}]


raw_data = [{"id": 3485494, "first_name": "Ольга", "last_name": "Захарьева", "is_closed": False, "can_access_closed": True, "sex": 1, "domain": "id3485494", "common_count": 8}, {"id": 33514697, "first_name": "Василий", "last_name": "Соколов", "is_closed": False, "can_access_closed": True, "sex": 2, "domain": "superchunk", "common_count": 18, "interests": "", "music": "", "movies": "", "books": ""}, {"id": 18607246, "first_name": "Ирина", "last_name": "Швецова", "is_closed": False, "can_access_closed": True, "sex": 1, "domain": "swingira", "city": {"id": 95, "title": "Нижний Новгород"}, "common_count": 11, "interests": "сальса, свинг, джаз, бачата, румба, ча-ча, танцы, линди хоп, буги вуги, чарльстон, танго, милонга, бальбоа, salsa, swing, jazz, bachata, rumba, dance, lindy hop, boogie woogie, charlestone, tango, milonga", "music": "", "movies": "", "books": ""}, {"id": 2975227, "first_name":"Ilia", "last_name": "Zinovev", "is_closed": False, "can_access_closed": True, "sex": 2, "domain": "hoasodoros", "city": {"id": 1, "title": "Москва"}, "common_count": 16}]


criteria = {'id': 80660212, 'first_name': 'Катерина', 'last_name': 'Фролова', 'is_closed': False, 'can_access_closed': True, 'sex': 2, 'domain': 'katerinawhite', 'city': 2, 'country': 1, 'common_count': 0, 'interests': ['dance', ' singing'], 'music': ['30 Seconds to Mars'], 'movies': ['10 негритят'], 'books': ['достоевский'], 'age_from': 28, 'age_to': 32}
