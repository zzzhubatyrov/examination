#!/bin/sh

# Путь к файлу-флагу для проверки загрузки фикстур
FLAG_FILE=/usr/src/app/fixtures_loaded.flag

# Проверяем, существует ли файл-флаг. Если да, то фикстуры уже загружены.
if [ ! -f "$FLAG_FILE" ]; then
    # Переходим в директорию приложения
    until cd /usr/src/app/
    do
        echo "Waiting for server volume..."
    done

    # Проверяем доступность базы данных (если используется PostgreSQL)
    if [ "$DATABASE" = "postgres" ]; then
        while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
            sleep 0.1
        done
        echo "READY"
    fi

    # Применяем миграции
    python manage.py migrate

    # Собираем статические файлы
    ./manage.py collectstatic --noinput

    # Загружаем фикстуры
    ./manage.py loaddata fixtures/Departments.json --app Departments
    ./manage.py loaddata fixtures/User_Custom_User.json --app User_Custom_User
    ./manage.py loaddata fixtures/Supplier.json --app Supplier
    ./manage.py loaddata fixtures/Equipment.json --app Equipment
    ./manage.py loaddata fixtures/Consignee.json --app Consignee
    ./manage.py loaddata fixtures/Delivery.json --app Delivery
    ./manage.py loaddata fixtures/KPP_Status.json --app KPP_Status
    ./manage.py loaddata fixtures/Task_Status.json --app Task_Status
    ./manage.py loaddata fixtures/Facilities.json --app Facilities
    ./manage.py loaddata fixtures/Documents_templates.json --app Documents_templates
    ./manage.py loaddata fixtures/Tasks.json --app Tasks
    ./manage.py loaddata fixtures/KPP.json --app KPP
    ./manage.py loaddata fixtures/Roles.json --app Roles

    # Создаем файл-флаг, указывающий на то, что фикстуры были загружены
    touch $FLAG_FILE
fi

# Запускаем сервер Django
nohup python manage.py runserver 0.0.0.0:8000
