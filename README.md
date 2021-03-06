# google_sheets

Задача:

Необходимо разработать скрипт на языке Python 3,

который будет выполнять следующие функции:

1. Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit) (необходимо копировать в свой Google аккаунт и выдать самому себе права).
2. Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»

    a. Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.

    b. Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).

3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).

Дополнения, которые дадут дополнительные баллы :

4. a. Упаковка решения в docker контейнер

    b. Разработка функционала проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.

    c. Разработка одностраничного web-приложения на основе Django или Flask. Front-end React.

5. Решение на проверку передается в виде ссылки на проект на Github.
В описании необходимо указать ссылку на ваш Google Sheets документ
(открыть права чтения и записи для пользователя [irbispro10@gmail.com])
, а также инструкцию по запуску разработанных скриптов.


Описание работы с сервисом.

1. клонировать репозиторий.
2. создать и запустить контейнер с базой данных:
   - docker build -t db_postgress -f db.Dockerfile .
   - docker run -p 5430:5432 --name db_post_cont -d db_postgress
3. получить и скаачть "*.json" сервисного аккаунта.
4. переименовать "*.json" сервисного аккаунта в "sacc1.json" и сопировать его в
   папку "/src/sheets/" сервиса
5. создать и запустить контейнер с сервисом:
   - docker build -t kanal_image -f service.Dockerfile .
   - docker run --net=host --name kanal_image kanal_service
6. открыть в браузере страницу по адресу: "http://127.0.0.111:5010/"
   данные полученные из таблицы расположенной по адресу
   "https://docs.google.com/spreadsheets/d/16LDqbvPer7YVfgyJpIKMbIyspqJLhbzsX44RqIbNGZU/edit#gid=0"
   будут отображены.
7. все изменения производимые с таблицей "google-sheets" будут отображаться на
   странице отображаемой сервисом.



