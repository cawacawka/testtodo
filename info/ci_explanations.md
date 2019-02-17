# AUTOMATED SMOKE tests

Allure-report публикуется в Gitlab Pages

Для всех стадий использовался один и тот же docker-imane. python:latest

## stage build

Билд приложение. 

В идеале, надо клонировать todomvc, запускать сервер, шарить его

Не заимплеменчено. На будущее заведена stageю

## stage test

Готовит окружение. 
 - Ставит Chrome и chromedriver
 - Ставит Firefox и geckodriver
 - Ставит venv и в него зависимости для тест-рана
 - Запускает тест
 - на выходе атрефакт с allure-report'ом, который еще надо собрать 
 
## stage report
 - Ставит окружение для allure-commandline (java)
 - Генерирует html-репорт из артефактов на stage test
 - Выкладывает его в public, делает доступным для просмотра на Gitlab Pages