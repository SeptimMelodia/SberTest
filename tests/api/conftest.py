from bestconfig import Config
import pytest
import requests


@pytest.fixture(scope='session')
def api_base_url():
    """
    Возвращает базовый URL для API GitHub.

    Returns:
        str: Базовый URL для API GitHub.
    """
    return 'https://api.github.com'


@pytest.fixture(scope='session')
def repo_name():
    """
    Возвращает имя репозитория по умолчанию.

    Returns:
        str: Имя репозитория по умолчанию.
    """
    return 'test-repo'


@pytest.fixture(scope='session')
def config():
    """
    Загружает конфигурационные данные из файла config_api.json.

    Returns:
        Config: Конфигурационные данные из файла.
    """
    return Config('../../configs/config_api.json')


@pytest.fixture(scope='session')
def api_headers(config):
    """
    Возвращает заголовки API с токеном авторизации.

    Args:
        config (Config): Конфигурационные данные.

    Returns:
        dict: Заголовки API с токеном авторизации.
    """
    return {'Authorization': f'token {config["token"]}'}


@pytest.fixture(scope='session')
def api_client(api_base_url, api_headers):
    """
    Создает сессию с API GitHub с использованием ключа API.

    Args:
        api_base_url (str): Базовый URL для API GitHub.
        api_headers (dict): Заголовки API с токеном авторизации.

    Returns:
        requests.Session: Сессия с API GitHub.
    """
    session = requests.Session()
    session.headers.update(api_headers)
    return session
