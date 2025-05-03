Инструкиця по запуску:
1. Создать папку, в которую будет помещен проект
2. Перейти в эту папку через git bash
3. Создать git репозиторий в этой папке при помощи команыд git init через git bash
4. Притянуть все файлы из репозитория командой git clone git@github.com:Alexander-Risovsky/Web-service-for-cash-flow-management.git
5. Открыть папку с проектом через IDE( я использую VS CODE)
6. Перейти в папку /Web-service-for-cash/DDS
7. Создать виртуальое окружение командой python -m venv venv
8. Активировать виртуальное окружение командой source venv/Scrpipts/activate
9. Установить все зависимости командой pip install -r requirements.txt
10. Создать таблички в базе данных командой python manage.py migrate
11. Запустить локальный сервер командой python manage.py runserver
Приложение запущено и готово к работе
   
