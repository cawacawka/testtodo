# Not implemented tests

Часть для ручного тестирования, часть просто не подходит для SMOKE.
Практически все можно автоматизировать.

1.	Сгенерировать 1 запись гигантской длины (>10к символов например).
2.	Сгенерировать огромное число записей и удалить их по одной/все сразу
3.	Различные кодировки и символы, их комбинации, BOM и тд.
4.  Если бы это было приложение с реальной базой, мб имеело бы смысл попробовать sql или просто js-иньекции
6.	Создание одинаковых 2 записей и работа с ними (пометить, отредактировать и тд.). Контроллировать что меняется именно "та" запись, а не ее клон.