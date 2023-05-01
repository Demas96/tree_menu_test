# Древовидное меню Django
Тестовое задание  

Для запуска необходимо скачать репозиторий, создать виртуальное окружение, установить библиотеки из requirements.txt и 
запустить django сервер.

Реализованы следующие функции:
1) Меню реализовано через template tag.
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django.
5) Активный пункт меню определяется исходя из URL текущей страницы.
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД

Доступ к админке: admin admin