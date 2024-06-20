# Проект «Виджет финансовых операций»

## Описание:

В проекте реализуется виджет, который показывает несколько последних успешных банковских операций клиента.В проекте будет реализована подготовка данных для отображения в новом виджете.

## Установка:

1.Клонируйте репозиторий:
'''
git clone https://github.com/viktorefimovich/home_work.git
'''

## Тестирование:

1.Установите фреймворк pytest:
'''
poetry add --group dev pytest
'''

2.Запустите тест pytest:
'''
pytest
'''

3.В pytest для анализа покрытия кода надо поставить библиотеку pytest-cov:
'''
poetry add --group dev pytest-cov
'''

4.Запустите тесты с оценкой покрытия, при активированном виртуальном окружении:
'''
pytest --cov
'''
