# Github Trends

Данная программа находит 20 репозиоториев на GitHub, созданных за последнюю неделю, которые набрали наибольшее количество звезд.

# Как использовать
Программа использует стороннюю библиотеку [requests](https://github.com/kennethreitz/requests).
Библиотеку requests можно установить через файл зависимостей приложения requirements.txt:
```#!bash
$ pip3 install -r requirements.txt
```
Рекомендуется устанавливать зависимости в виртуальном окружении, используя [virtualenv](https://github.com/pypa/virtualenv), [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) или [venv](https://docs.python.org/3/library/venv.html).

Для вывода помощи запустите скрипт с аргументом -h (--help):
```#!bash
$ python github_trending.py -h
```
### Параметры командной строки:
**-t --top_size** - количество репозиториев для поиска (по умолчанию = 20);
**-d --recent_days** - количество дней с момента создания репозитория (по умолчанию = 7);
**-v --verbose** - вывод url's для открытых issues.

Пример запуска в Linux, Python 3.5.2:
```#!bash
$ python github_trending.py
```
Пример вывода результатов:
```#!bash
-------------------------------------------------------------------------------------------------------
Name: tamperchrome  | Stars★ : 2076  | Open issues:   5   | URL https://github.com/google/tamperchrome       
-------------------------------------------------------------------------------------------------------
Name: timestrap     | Stars★ :  993  | Open issues:  21   | URL https://github.com/overshard/timestrap       
-------------------------------------------------------------------------------------------------------
Name: flexidie      | Stars★ :  523  | Open issues:   0   | URL https://github.com/Te-k/flexidie             
-------------------------------------------------------------------------------------------------------
...

```

# Цели проекта

Код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
