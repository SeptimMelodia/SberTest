import pytest
from bestconfig import Config
from selenium import webdriver


@pytest.fixture(scope='module')
def browser():
    """
        Фикстура для инициализации WebDriver.

        Returns:
            webdriver.Chrome: Инициализированный WebDriver.
        """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()


@pytest.fixture(scope='session')
def config():
    """
        Фикстура для загрузки конфигурационных данных.

        Returns:
            Config: Объект конфигурации.
        """
    return Config('../../configs/config_ui.json')
