# AUTOMATED SMOKE tests

Allure-report публикуется в Gitlab Pages

## stage build

Билд приложения. 

В идеале, надо клонировать todomvc, запускать сервер, шарить его

Не заимплеменчено. Stage "на будущее" + для отображения предполагаемой схемы.

А пока используется приложение из интернетов.

docker-image не указан. берется дефолтный

## stage test

Готовит окружение. 
 - Ставит Chrome и chromedriver
 - Ставит Firefox и geckodriver
 - Ставит venv и в него зависимости для тест-рана
 - Запускает тест
 - на выходе атрефакт с allure-report'ом, который еще надо собрать 
 
Используется docker-imane. python:latest 
C предустановленным питоном
 
## stage report_gen
 - Ставит окружение для allure-commandline (java)
 - Генерирует html-репорт из артефактов на stage test
 - Выкладывает его в public, делает доступным для просмотра на Gitlab Pages
 
 Используется docker-imane. atlassian/default-image
 с предустановленной java
 
 ## stage report_publish
 - Публикует отчет в Gitlab Pages
 
 docker-image не указан. берется дефолтный