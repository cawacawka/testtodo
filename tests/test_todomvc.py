# -*- coding: utf-8 -*-
import json
import time

import allure
import pytest
from selenium import webdriver

from tests.testdata.base_tests import base_cases
from tests.testdata.gen_tests import gen_cases
from common import common_functions as cf
from common.client import TodoHandler


@pytest.fixture(scope="session")
def todo():
    browser = webdriver.Chrome(
        executable_path="utilities/drivers/Win/chromedriver.exe")
    browser.delete_all_cookies()
    browser.implicitly_wait(10)
    browser.get("http://todomvc.com/examples/react/#/")

    yield TodoHandler(browser)
    browser.close()
    browser.quit()


@pytest.fixture(scope="function")
def clean_todo(todo):
    yield
    time.sleep(0.3)
    todo.click_all()
    todo.delete_all_notes()


@allure.feature('Тестирование todomvc')
@allure.story('Базовый функционал')
@pytest.mark.parametrize("case",
                         base_cases.values(),
                         ids=list(base_cases.keys()))
def test_base(todo,
              clean_todo,
              request,
              case):
    testname = request.node.name
    cf.allure_attach_str_data(testname, json.dumps(case, indent=4), "JSON")

    todo.do_steps(case["steps"])

    infos = todo.get_notes_text_and_status()
    cf.allure_attach_str_data("{}_notes".format(testname),
                              json.dumps(infos, indent=4), "JSON")

    cf.check_text_and_status(infos, case["expected_notes"])


@allure.feature('Тестирование todomvc')
@allure.story('Базовый функционал на генерированных данных')
@pytest.mark.parametrize("case",
                         [cf.generate_case(test) for test in
                          gen_cases.values()],
                         ids=list(gen_cases.keys()))
def test_generated(todo,
                   clean_todo,
                   request,
                   case):
    testname = request.node.name
    cf.allure_attach_str_data(testname, json.dumps(case, indent=4), "JSON")

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
