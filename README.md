
# api_yamdb


## Описание проетка:
Проект YaMDb собирает отзывы пользователей на различные произведения.


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:LianaVolkova/api_yamdb.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
py -m venv venv
```

Для *nix-систем:

```bash 
source venv/bin/activate
```

Для windows-систем:

```bash 
source venv/Scripts/activate
```

```
py -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
py manage.py migrate
```

Запустить проект:

```
py manage.py runserver
```

Документация с примерами запросов и ответов на них по адресу 
```
http://127.0.0.1:8000/redoc/
```