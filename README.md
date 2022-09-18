# Веб-сервис для сбора отзывов YaMDB и API к нему 

Это групповой проект студентов Яндекс.Практикум в рамках курса "API: интерфейс взаимодействия программ"

## Описание проекта

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: "Категории", "Фильмы", "Музыка". Список категорий (Category) может быть расширен администратором. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. Произведению может быть присвоен жанр из списка предустановленных. Новые жанры может создавать только администратор. Пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

#### Документация к API доступна по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) после запуска проекта

## Стек технологий

- Python 3.7
- Django 2.2.16
- Django REST Framework 3.12.4
- Djangorestframework-simplejwt 4.7.2
- Git

### Доступный функционал:
- Для аутентификации используются JWT-токены
- У неаутентифицированных пользователей доступ к API только на уровне чтения
- Создание объектов разрешено только аутентифицированным пользователям. На прочий фунционал наложено ограничение в виде административных ролей и авторства.
- Управление пользователями
- Получение списка всех категорий и жанров, добавление и удаление
- Получение списка всех произведений, их добавление. Получение, обновление и удаление конкретного произведения
- Получение списка всех отзывов, их добавление. Получение, обновление и удаление конкретного отзыва
- Получение списка всех комментариев, их добавление. Получение, обновление и удаление конкретного комментария
- Возможность получения подробной информации о себе и удаления своего аккаунта
- Фильтрация по полям


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
python -m venv venv
```

Активировать виртуальное окружение:

``` 
source venv/Scripts/activate
```

Обновить pip:

``` 
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

``` 
pip install -r requirements.txt
```

Выполнить миграции:

``` 
python manage.py migrate
```

Запустить проект:

``` 
python manage.py runserver
```

### Примеры некоторых запросов API

Регистрация пользователя:  
``` 
POST /api/v1/auth/signup/
```  

Получение данных своей учетной записи:  
``` 
GET /api/v1/users/me/
```  

Добавление новой категории:  
``` 
POST /api/v1/categories/
```  

Удаление жанра:  
``` 
DELETE /api/v1/genres/{slug}
```  

Частичное обновление информации о произведении:  
``` 
PATCH /api/v1/titles/{titles_id}
```  

Получение списка всех отзывов:  
``` 
GET /api/v1/titles/{title_id}/reviews/
```  

Добавление комментария к отзыву:  
``` 
POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

#### Полный список запросов API находятся в документации

### Над проектом работали

- Волкова Лиана
- Юлия Пак [llliuliya](https://github.com/llliuliya)
- Всеволод Вишняков [cherryofmind](https://github.com/cherryofmind)
