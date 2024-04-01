import vk_api


# Вывод информации о сообществе на основе полученных данных
def print_group_info(group_info: dict) -> None:
    print("Название сообщества: ", group_info["name"])
    status: str = group_info["status"]
    if len(status) > 0:
        print("Статус сообщества:", group_info["status"])
    description: str = group_info["description"]
    if len(description) > 0:
        if len(description) > 200:
            description = description[:200] + "..."
        print("Описание: ", description)
    print("Кол-во подписчиков: ", group_info["members_count"])
    group_type: str = group_info["type"]
    if group_type == "group":
        print("Это группа.")
    elif group_type == "page":
        print("Это паблик.")
    else:
        print(f"Это мероприятие, которое начнётся {group_info['activity']}.")
    is_closed: int = group_info["is_closed"]
    if is_closed == 0:
        print("Сообщество доступно для всех")
    elif is_closed == 1:
        print("Это закрытое сообщество")
    else:
        print("Это частное сообщество")
    age_limits: int = group_info["age_limits"]
    if age_limits == 1:
        print("Сообщество не имеет возрастных ограничений.")
    elif age_limits == 2:
        print("Возрастное ограничение 16+")
    else:
        print("Возрастное ограничение 18+")
    if "country" in group_info.keys():
        print("Страна сообщества:", group_info["country"]["title"])
    else:
        print("Страна сообщества не указана.")
    is_verified: int = group_info["verified"]
    if is_verified:
        print("Сообщество подтверждено")
    else:
        print("Сообщество не подтверждено")


# Основная программа для взаимодействия пользователя с api через консоль
def main():
    print("Приветствую в приложении по получению информации о группе.")
    while True:
        print("Выберите способ нахождения группы.")
        print("1 - через поисковик")
        print("2 - через прямую ссылку")
        choice = int(input())
        if choice == 1:
            name = input("Введите название группы: ")
            groups = vk_api.get_groups_list(name)
            if not groups:
                break
            print("Выберите номер нужной группы. Если нужной группы нет, введите -1 и выйдите из поиска.")
            for group in groups:
                print(group[0])
            index = int(input())
            while index >= len(groups) or (index <= 0 and index != 1):
                print("Такого номера нет. Попробуйте ещё раз или введите -1, чтобы выйти.")
            if index == -1:
                continue
            else:
                group_id = groups[index - 1][1]
                group_info = vk_api.get_group_info(group_id)
                print_group_info(group_info)
        elif choice == 2:
            group_id = input("Введите айди или короткое название группы: ")
            group_info = vk_api.get_group_info(group_id)
            if group_info is None:
                break
            print_group_info(group_info)
        else:
            print("Такого варианта нет. Попробуйте ещё раз.")
            continue

        print("Хотите узнать информацию о другой группе? (да/нет)")
        ans = input()
        while ans not in ["нет", "да"]:
            print("Неизвестная команда. Попробуйте ещё раз.")
            ans = input()
        if ans == "нет":
            break


if __name__ == "__main__":
    main()
