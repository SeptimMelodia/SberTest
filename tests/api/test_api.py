import allure


@allure.title("Создание репозитория")
@allure.step
def test_create_repo(api_base_url, api_client, repo_name):
    """
    Тест на создание репозитория.

    Args:
        api_base_url (str): Базовый URL для API GitHub.
        api_client (requests.Session): Сессия с API GitHub.
        repo_name (str): Имя репозитория для создания.

    Returns:
        None
    """
    data = {'name': repo_name, 'private': True}
    response = api_client.post(f'{api_base_url}/user/repos', json=data)
    assert response.status_code == 201
    assert response.json()['name'] == repo_name
    assert response.json()['private']

@allure.title("Получить репозиторий")
@allure.step
def test_get_repos(api_client, api_base_url, repo_name, config):
    """
    Тест на получение репозитория.

    Args:
        api_client (requests.Session): Сессия с API GitHub.
        api_base_url (str): Базовый URL для API GitHub.
        repo_name (str): Имя репозитория для получения.
        config (Config): Конфигурационные данные.

    Returns:
        None
    """
    response = api_client.get(f'{api_base_url}/repos/{config["username"]}/{repo_name}')
    assert response.status_code == 200
    repo = response.json()
    assert repo['name'] == repo_name
    assert repo['private'] == True

@allure.title("Обновить репо")
@allure.step
def test_update_repo(api_base_url, api_client, repo_name, config):
    """
    Тест на обновление репозитория.

    Args:
        api_base_url (str): Базовый URL для API GitHub.
        api_client (requests.Session): Сессия с API GitHub.
        repo_name (str): Имя репозитория для обновления.
        config (Config): Конфигурационные данные.

    Returns:
        None
    """
    data = {'name': repo_name + '1'}
    url = f'{api_base_url}/repos/{config["username"]}/{repo_name}'
    response = api_client.patch(f'{api_base_url}/repos/{config["username"]}/{repo_name}', json=data)
    assert response.status_code == 200
    assert response.json()['name'] == repo_name + '1'

@allure.title("Удалить репо")
@allure.step
def test_delete_repo(api_base_url, api_client, repo_name, config):
    """
    Тест на удаление репозитория.

    Args:
        api_base_url (str): Базовый URL для API GitHub.
        api_client (requests.Session): Сессия с API GitHub.
        repo_name (str): Имя репозитория для удаления.
        config (Config): Конфигурационные данные.

    Returns:
        None
    """
    response = api_client.delete(f'{api_base_url}/repos/{config["username"]}/{repo_name}1')
    assert response.status_code == 204
