# -*- coding: utf-8 -*-
import json

import allure
import pytest

from common import common_functions as cf
from tests.testdata.base_tests import base_cases
from tests.testdata.gen_tests import gen_cases


@allure.feature('Тестирование todomvc')
@allure.story('Базовый функционал')
@pytest.mark.todobase
@pytest.mark.parametrize("case",
                         base_cases.values(),
                         ids=list(base_cases.keys()))
def test_base(todo,
              clean_todo,
              request,
              case):
    """
    Базовая тестовая функция, с прямым указанием текста записей,
    и порядком действий.
    Параметризована.

    Проверяет базовый CRUD

    :param todo: инстанс клиента драйвера, возвращен фикстурой todo
    :param clean_todo: teardown фикстура, очищает все записи (можно убрать, если
    todo фикстура имеет scope function)
    :param request: объект pytest, используется для получения полного имени
    теста, включающего тестовую функцию и идентификатор теста
    :param case: тестовый набор, шаги и ожидаемый результат
    :return:
    """
    testname = request.node.name
    cf.allure_attach_str_data(testname, json.dumps(case, indent=4), "JSON")
    with cf.ExcHandler(testname, todohandler=todo):
        todo.do_steps(case["steps"])
        infos = todo.get_notes_text_and_status()
        cf.allure_attach_str_data("{}_notes".format(testname),
                                  json.dumps(infos, indent=4), "JSON")
        cf.check_text_and_status(infos, case["expected_notes"])


@allure.feature('Тестирование todomvc')
@allure.story('Базовый функционал на генерированных данных')
@pytest.mark.todogen
@pytest.mark.parametrize("case",
                         [cf.generate_case(test) for test in
                          gen_cases.values()],
                         ids=list(gen_cases.keys()))
def test_generated(todo,
                   clean_todo,
                   request,
                   case):
    """
    Тестовая функция, с генирированными данными, и порядком действий.
    Параметризована.

    Заполняет todo различным числом записей, помечает часть их, если требуется

    Проверяет корректность количества отображаемых на странице записей
    различного типа (active, completed) при переходах по различным режимам
    отображения и т.п.


    :param todo: инстанс клиента драйвера, возвращен фикстурой todo
    :param clean_todo: teardown фикстура, очищает все записи (можно убрать, если
    todo фикстура имеет scope function)
    :param request: объект pytest, используется для получения полного имени
    теста, включающего тестовую функцию и идентификатор теста
    :param case: тестовый набор, шаги и ожидаемый результат
    :return:
    """
    testname = request.node.name
    cf.allure_attach_str_data(testname, json.dumps(case, indent=4), "JSON")
    with cf.ExcHandler(testname, todohandler=todo):
        todo.do_steps(case["steps"])

        infos = todo.get_notes_text_and_status()
        cf.allure_attach_str_data("{}_notes".format(testname),
                                  json.dumps(infos, indent=4), "JSON")

        fact_from_bottom = todo.get_status_string()
        fact_active = len(todo.find_all_active())
        fact_completed = len(todo.find_all_completed())

        cf.check_notes_count(
            fact_from_bottom,
            fact_active,
            fact_completed,
            case["expected"]["bottom"],
            case["expected"]["active"],
            case["expected"]["marked"]
        )
