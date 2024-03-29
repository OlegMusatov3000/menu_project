# Древовидное меню
### Описание

В этом проекте реализовано древовидное меню, соблюдаются следующие условия:
- Меню реализовано через template tag
- Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
- Хранится в БД.
- Редактируется в стандартной админке Django
- Активный пункт меню определяется исходя из URL текущей страницы
- Меню на одной странице может быть несколько. Они определяются по названию.
- При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
- На отрисовку каждого меню требуется ровно 1 запрос к БД

### Технологии
- Python 3.9
- Django 4.2.6

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:OlegMusatov3000/menu_project.git
```

```
cd menu_project
```

Cоздать виртуальное окружение:

```
python3.9 -m venv venv
```

Активировать виртуальное окружение:

Команда для Windows:

```
source venv/Scripts/activate
```

Для Linux и macOS:

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Автор
- Олег Мусатов
- Tg: @OlegMusatov
