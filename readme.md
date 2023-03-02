# Uptrader test task
## Доступные urls:
   ```bash
   localhost:8000/admin/ - админ меню (login: admin, pass: admin)
   localhost:8000/ - главное меню
   localhost:8000/full-menu/ - полностью раскрытые меню
   localhost:8000/<slug:slug>/ - раскрытые меню по слагу
   ```
## Инструкция для запуска с использованием Docker'а.
1. Установить docker
2. Создать файл .env, можно скопировать из example.env
3. С помощью команды запустить docker-compose
   ```bash
   docker-compose up --build -d
   ```
## Инструкция для запуска без использования Docker.

1. Настройка виртуального окружения

   1.1 Создать и активировать виртуальное окружение

    ```bash
   # Windows:
    python -m venv venv
   .\venv\Scripts\activate
   
   # Linux:
   virtualenv -p python3.8 .venv
   source .venv/bin/activate
    ```
   1.2 Установка необходимых библиотек

    ```bash
    pip install -r requirements.txt
    ```

2. Настройка базы данных

   2.1. Установить PostgreSQL

   2.2. Открыть sql shell

   2.3. Выполнить следующие команды:
    ```postgresplsql
    CREATE DATABASE test_db with encoding='UTF-8' LC_CTYPE='en_US.UTF-8' LC_COLLATE='en_US.UTF-8' TEMPLATE=template0;
    CREATE ROLE test_user WITH PASSWORD 'testpassword';
    GRANT ALL PRIVILEGES ON DATABASE test_db to test_user;
    ALTER ROLE test_user LOGIN CREATEDB;
    ```
   2.4. Добавить в .env, информацию о базе данных

3. Сделать миграции

    ```bash
    ./manage.py makemigrations
    ./manage.py migrate
    ```

4. Запустить сервер и проверить его работу открыв `localhost:8000` в браузере

    ```bash
    python manage.py runserver
    ```