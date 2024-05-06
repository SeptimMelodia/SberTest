# Подготовка окружения

1. **Склонируйте репозиторий с тестами на локальную машину:**

```bash
git clone https://github.com/your-username/your-repository.git
```
   
2. **Установите необходимые зависимости:**
```bash
pip install -r requirements.txt
```
# Инструкция по использованию и запуску тестов для API GitHub

1. **Измените файл config_api.json в директории configs и добавьте свои данные**

*При создании токена GitHub необходимо выдать ему права администрирования*

*Для корректной работы необходима версия python 3.8*

2. **Запустите тесты с помощью pytest:**

```bash
python3.8 -m pytest tests/api --alluredir=./allure-reports
```
3. **Посмотреть отчет**

```bash
python3.8 -m allure serve ./allure-reports --host localhost --port 8888
```

# Инструкция по использованию и запуску UI тестов для интернет-магазина
*Ожидание ответа может занять некоторое время, сайт довольно долго прогружается*
1. **Измените файл config_ui.json в директории configs и добавьте свои данные**

## Запуск тестов
*Для корректной работы необходима версия python 3.8*
1. **Запустите тесты с помощью pytest:**

```bash
python3.8 -m pytest tests/ui --alluredir=./allure-reports
```
2. **Посмотреть отчет**

```bash
python3.8 -m allure serve ./allure-reports --host localhost --port 8888
```
