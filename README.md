# VKGroupsProject
Простая программа, которая может отобразить информацию о сообществе в ВК: название, описание, публичность, страна и т.д.

# Как начать работать
- Клонируем репозиторий
```
https://github.com/Nytrock/VKGroupsProject.git
```

- Получаем ключ доступа к API. Вводим в браузер ссылку ниже и в получившейся адресной строке копируем аттрибут с названием `access_token`
```
oauth.vk.com/authorize?client_id=51891735&display=page&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&v=5.199
```

- Создаём в папке с проектом файл `config.json` и заполняем его так:
```
{
  "VK_TOKEN": "Ваш токен"
}
```

- Запускаем программу
