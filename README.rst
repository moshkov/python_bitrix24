python_bitrix24
===============
https://github.com/moshkov/python_bitrix24

.. image:: https://img.shields.io/pypi/v/python_bitrix24.svg
    :target: https://pypi.python.org/pypi/python_bitrix24

.. image:: https://img.shields.io/pypi/dm/python_bitrix24.svg
    :target: https://pypi.python.org/pypi/python_bitrix24

.. image:: https://img.shields.io/pypi/l/python_bitrix24.svg
    :target: https://pypi.python.org/pypi/python_bitrix24

Зависимости
-----------

- Python 2.7+
- requests


Установка
---------

.. code-block:: bash

    $ pip install python_bitrix24

Если используется Django, то в настройках проекта можно указать BITRIX24_API_LOGIN, BITRIX24_API_PASSWORD и BITRIX24_API_MAIN_USER_NAME.


Описание
--------

*Python Bitrix24 API*

Позволяет работать с API Bitrix24. В текущей версии реализовано только добавление лида.

- Bitrix24: https://www.bitrix24.ru
- Описание API: https://dev.1c-bitrix.ru/community/blogs/chaos/crm-sozdanie-lidov-iz-drugikh-servisov.php


Использование
-------------

.. code-block:: python

    from python_bitrix24.bitrix24 import Bitrix24Connection

    bitrix24Connection = Bitrix24Connection('YOU_BITRIX24_API_LOGIN', 'YOU_BITRIX24_API_PASSWORD', 'YOU_BITRIX24_API_MAIN_USER_NAME')

    b24_result = bitrix24Connection.add_lead('My dear Lead, {
        'NAME': 'Vasya Pupkin',
        'EMAIL_OTHER': 'lead@email.local',
        'UF_CRM_123456789': 'additional information',
        'UF_CRM_123456788': 'additional information 2',
    })

    if b24_result.get('error', '') == '201' == 0:
        print 'success'

    ...

Для Django (если в настройках заданы BITRIX24_API_LOGIN, BITRIX24_API_PASSWORD и BITRIX24_API_MAIN_USER_NAME):

.. code-block:: python

    from python_bitrix24.python_bitrix24_django import bitrix24Connection

    b24_result = bitrix24Connection.add_lead('My dear Lead, {
        'NAME': 'Vasya Pupkin',
        'EMAIL_OTHER': 'lead@email.local',
        'UF_CRM_123456789': 'additional information',
        'UF_CRM_123456788': 'additional information 2',
    })

    if b24_result.get('error', '') == '201' == 0:
        print 'success'

    ...

    ...


TODO
----

1. Проверка отвера API на корректность
2. Остальной функционал API Bitrix24
3. Тесты
4. Документация
