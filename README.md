
# api_yamdb


## Описание проетка:
Проект YaMDb собирает отзывы пользователей на различные произведения.


## Как запустить проект:

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