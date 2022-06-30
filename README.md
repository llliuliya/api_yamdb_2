# api_yamdb

## Описание проекта

Проект YaMDb собирает отзывы пользователей на произведения.

### Над проектом работали

- [LianaVolkova](https://github.com/LianaVolkova)
- [llliuliya](https://github.com/llliuliya)
- [cherryofmind](https://github.com/cherryofmind)

## Стек технологий

- Python 3.7
- Django 2.2.16
- Django REST Framework 3.12.4
- Djangorestframework-simplejwt 4.7.2
- Git

### Пользовательские роли

- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
- Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- Суперюзер Django — обладет правами администратора (admin)

### Эндпоинты

- /auth/singup/ — регистрация нового пользователя
- /auth/token/ — получение токена
- /users/ — пользователи
- /users/me/ — эндпоинт для получения и изменения данных о самом себе

### Модели

В приложении реализованы модели для следующих ресурсов API YaMDb:

- Auth - аутентификация;
- Users - пользователи;
- Titles - произведения, к которым пишут отзывы (определённый фильм, книга или песенка);
- Categories - категории (типы) произведений (например: «Фильмы», «Книги», «Музыка»);
- Genres - жанры произведений, одно произведение может быть привязано к нескольким жанрам;
- Reviews - отзывы на произведения, отзыв привязан к определённому произведению;
- Comments - комментарии к отзывам, комментарий привязан к определённому отзыву;

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:LianaVolkova/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать виртуальное окружение:

```
# для Windows-систем:
py -m venv venv

# для *nix-систем:
python3 -m venv venv   
```

Активировать виртуальное окружение:

```
# для Windows-систем:
source venv/Scripts/activate

# для *nix-систем:
source venv/bin/activate
```

Обновить pip:

```
# для Windows-систем:
py -m pip install --upgrade pip

# для *nix-систем:
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
# для Windows-систем:
py manage.py migrate

# для *nix-систем:
python3 manage.py migrate
```

Запустить проект:

```
# для Windows-систем:
py manage.py runserver

# для *nix-систем:
python3 manage.py runserver
```

Документация с примерами запросов и ответов на них по адресу

```
http://127.0.0.1:8000/redoc/
```

### Примеры запросов

Пример POST-запроса: добавление нового отзыва.

```
POST .../api/v1/titles/{title_id}/reviews/
```

```
{
  "text": "string",
  "score": 1
}
```

Пример ответа:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

Пример GET-запроса: получение списка всех комментариев к отзыву.

```
GET .../api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

Пример ответа:

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```

Пример POST-запроса: получение JWT-токена.

```
POST .../api/v1/auth/token/
```

```
{
  "username": "string",
  "confirmation_code": "string"
}
```

Пример ответа:

```
{  
  "token": "string"
}
```

Пример PATCH-запроса: изменение данных пользователя по username.

```
PATCH .../api/v1/users/{username}/
```

```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

Пример ответа:

```
{  
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
