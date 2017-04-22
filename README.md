# Github Trends

Данная программа находит 20 репозиоториев на GitHub, созданных за последнюю неделю, которые набрали наибольшее количество звезд.

# Как использовать
Программа использует стороннюю библиотеку [requests](https://github.com/kennethreitz/requests)
Библиотек requests можно установить через файл зависимостей приложения requirements.txt:
```#!bash
$ pip3 install -r requirements.txt
```
Рекомендуется устанавливать зависимости в виртуальном окружении используя [virtualenv](https://github.com/pypa/virtualenv), [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper).

Пример запуска в Linux, Python 3.5.2:
```#!bash
$ python github_trending.py
```
Пример вывода результатов:
```#!bash
-------------------------------------------------------------------------------------------------------
             Name              | Stars | Open issues | URL
-------------------------------------------------------------------------------------------------------
pytorch-CycleGAN-and-pix2pix   | 1175  |      5      | https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
-------------------------------------------------------------------------------------------------------
tamperchrome                   |  508  |      1      | https://github.com/google/tamperchrome
-------------------------------------------------------------------------------------------------------
SuperTextView                  |  483  |      2      | https://github.com/chenBingX/SuperTextView
-------------------------------------------------------------------------------------------------------
fastText_multilingual          |  370  |      1      | https://github.com/Babylonpartners/fastText_multilingual
-------------------------------------------------------------------------------------------------------
polaris                        |  348  |      6      | https://github.com/Shopify/polaris
-------------------------------------------------------------------------------------------------------
```

# Цели проекта

Код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
