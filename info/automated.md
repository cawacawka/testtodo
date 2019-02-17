# AUTOMATED SMOKE tests

Allure-report публикуется в Gitlab Pages

## test_base

Набор тестов для проверки CRUD

Данные параметризованы.  

Создание, редактирование, удаление, изменение статуса.

Работает пока только с Chrome, Firefox. Можно добавлять-удалять драйверы. Параметризовано

Тестовые данные в виде python-модуля. для удобства вставки генерируемых значений и импорта

Последовательность шагов, проверка содержимого записи после выполнения шагов, и проверка статуса записи

Перечень: 
 - Base_add_empty_note'
 - Base_add_single_note'
 - Base_add_delete_single_note
 - Base_add_edit_single_note
 - Base_add_and_mark_single_note
 - Base_add_mark_delete_single_note
 - Base_add_mark_edit_single_note

В названии суть, подробные шаги в allure-отчете

### Запуск конкретного набора
```sh
python -m pytest <path_to>/testtodo/tests -k test_base
```
 - опционально можно добавить ключ -n <thread_counts> (пример -n 4, запустит тест в 4 потока, 4 сессии). см. pytest-xdist

# test_generated

Набор тестов для проверки корректности переходов между "кнопка", переключения состояния записей и тдю

Данные параметризованы. Записи и статусы генерируются.

Работает пока только с Chrome, Firefox. Можно добавлять-удалять драйверы. Параметризовано

Тестовые данные в виде python-модуля. для удобства вставки генерируемых значений и импорта

Последовательность шагов, наполнение генерируемыми записями, смена статусов, переключение между отображаемым набором записей. 
Контроль количества и типа отображаемых записей.

Перечень: 
- Add_many_notes_and_mark_some 
- Add_and_mark_click_active 
- Add_and_mark_click_completed
- Clear_from_All 
- Clear_from_Completed 
- Clear_from_Active 
- Save_state_after_refresh 
- Toggle_from_All
- Toggle_from_All_doubleclick
- Toggle_from_Active
- Toggle_from_Active_double_click
- Toggle_from_Complete
- Toggle_from_Complete_double_click


В названии суть, подробные шаги в allure-отчете

### Запуск конкретного набора
```sh
python -m pytest <path_to>/testtodo/tests -k test_generated
```
 - опционально можно добавить ключ -n <thread_counts> (пример -n 4, запустит тест в 4 потока, 4 сессии). см. pytest-xdist

