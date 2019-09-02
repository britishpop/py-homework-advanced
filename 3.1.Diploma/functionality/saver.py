import time
import re
from classes.vk_users import MatchingUser


def save_matching_users(data, criteria, token):
    data = filter_for_users(data, criteria)
    for user in data:
        print('Добавляем подходящего пользователя...')
        matching_user = MatchingUser(user['id'], token)
        matching_user.write_to_json()
        time.sleep(1)


def filter_for_users(data, criteria):
    scores = []
    for user in data:
        score = get_score_for_user(user, criteria)
        scores.append({'id': user['id'], 'score': score})

    scores.sort(key=lambda x: x['score'], reverse=True)
    return scores[:10]


def get_score_for_user(user, criteria):
    score = 0

    if user['common_count'] != 0:
        score += common_count*user['common_count']

    for item in ['music', 'books', 'interests', 'movies']:
        for i in criteria.get(item):
            result = re.findall(i, user[item], re.IGNORECASE)
            if result:
                if item == 'music':
                    score += 5
                if item == 'books':
                    score += 3
                if item == 'interests':
                    score += 2
                if item == 'movies':
                    score += 1

        return score
