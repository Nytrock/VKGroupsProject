import json
from typing import Union, Optional

import requests

# получение токена из файла
with open("config.json") as file:
    config = json.load(file)

token = config["VK_TOKEN"]
version = 5.199


# Поиск сообществ по названию, возвращает список возможных групп
def get_groups_list(group_name: str) -> Optional[list[tuple[str, int]]]:
    response = requests.get("https://api.vk.com/method/groups.search",
                            params={
                                "access_token": token,
                                "v": version,
                                "q": group_name,
                                "count": 10
                            }).json()
    if 'error' in response:
        print("Ошибка: ", response['error']['error_msg'])
    else:
        groups = response["response"]["items"]
        result: list[tuple[str, int]] = []
        for i in range(len(groups)):
            result.append((f"{i + 1} - {groups[i]['name']}", groups[i]["id"]))
        return result


# Получение информации о сообществе
def get_group_info(group_id: Union[int, str]) -> Optional[dict]:
    response = requests.get("https://api.vk.com/method/groups.getById",
                            params={
                                "access_token": token,
                                "v": version,
                                "group_id": group_id,
                                "fields": "members_count,description,activity,country,verified,status,age_limits"
                            }).json()
    if 'error' in response:
        print("Ошибка: ", response['error']['error_msg'])
    else:
        return response["response"]["groups"][0]
