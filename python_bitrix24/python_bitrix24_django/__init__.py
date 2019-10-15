from python_bitrix24.bitrix24 import Bitrix24Connection
from django.conf import settings

bitrix24Connection = Bitrix24Connection(settings.BITRIX24_API_LOGIN, settings.BITRIX24_API_PASSWORD,
                                        settings.BITRIX24_API_MAIN_USER_NAME, settings.BITRIX24_API_DOMAIN)
