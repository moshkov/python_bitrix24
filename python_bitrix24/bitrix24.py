# -*- coding: utf-8 -*-

import requests
import json


class Bitrix24Connection(object):

    _api_main_user_name = None
    _api_login = None
    _api_password = None
    _api_url = None

    def __init__(self, api_login, api_password, api_main_user_name):
        self._api_login = api_login
        self._api_password = api_password
        self._api_main_user_name = api_main_user_name
        self._api_url = "https://%s.bitrix24.ru/" % self._api_main_user_name

    def _build_url(self, path):
        return "%s%s" % (self._api_url, path)

    def _build_data(self, data):
        _data = {
            'LOGIN': self._api_login,
            'PASSWORD': self._api_password,
        }

        _data.update(data)

        result_data = {}

        for k, v in _data.iteritems():
            result_data[unicode(k).encode('utf-8')] = unicode(v).encode('utf-8')

        return result_data

    def _send_request(self, url, data):
        """ Отправляет запрос с API и получает ответ

        :param url: URL на кототорый отправляем запрос
        :param data: передаваемые данные
        :return: словарь с ответом от сервера
        """

        r = requests.post(url, data=self._build_data(data))

        try:
            return json.loads(r.content.replace('\'', '"'))
        except:
            return None

    def add_lead(self, lead_title, extra=None):
        """Добавление лида

        https://dev.1c-bitrix.ru/community/blogs/chaos/crm-sozdanie-lidov-iz-drugikh-servisov.php

        :param lead_title: Название лида
        :param extra: дополнительные параметры (подробнее в документации к API)
        :return: словарь с ответом сервера
        """
        url = self._build_url('crm/configs/import/lead.php')
        data = {
            'TITLE': lead_title
        }

        if extra is not None:
            data.update(extra)

        return self._send_request(url, data)
