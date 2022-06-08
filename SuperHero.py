import requests


def most_intelligent(*names):
    intelligence_dict = {}
    for name in names:
        url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
        responce = requests.get(url)
        hero_id = responce.json()['results'][0]['id']
        url = (f'https://superheroapi.com/api/2619421814940190/'
               f'{hero_id}/powerstats')
        responce = requests.get(url)
        hero_intelligence = responce.json()['intelligence']
        temp_dict = intelligence_dict.fromkeys([name], hero_intelligence)
        intelligence_dict.update(temp_dict)

    sorted_tuple = sorted(intelligence_dict.items(), key=lambda x: x[1])
    intelligence_dict = dict(sorted_tuple)
    print(f'Самый умный супергерой это: {list(intelligence_dict.keys())[0]}')
    return list(intelligence_dict.keys())[0]


if __name__ == '__main__':
    most_intelligent('Hulk', 'Captain America', 'Thanos')
