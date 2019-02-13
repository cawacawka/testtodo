# -*- coding: utf-8 -*-
import time

import pytest
from selenium import webdriver

from common.client import TodoHandler


@pytest.fixture(scope="session", params=["Chrome", "Firefox"])
def todo(request):
    """
    Базовая фикстура, возвращает инстанс драйвера.
    Запускается раз за тестовую сессию, при необходимости
    можно изменить scope на function, тогда каждый новый тест будет запускаться
    в отдельном инстансе браузера.
    Параметризован. Варианты Chrome и Firefox
    По завершения закрывает браузер

    :param request: объект pytest
    :return:
    """
    dname = request.param
    if dname == "Chrome":
        browser = webdriver.Chrome()
    elif dname == "Firefox":
        browser = webdriver.Firefox()
    browser.delete_all_cookies()
    browser.implicitly_wait(10)
    browser.get("http://todomvc.com/examples/react/#/")

    yield TodoHandler(browser)
    browser.close()
    browser.quit()


@pytest.fixture(scope="function")
def clean_todo(todo):
    """
    Тирдаун фикстура, запускается на каждую тестовую функцию
    по завершению каждого теста удаляет все внесенные в todomvc записи
    Если фикстура todo имеет scope function, данную фикстуру можно не
    вызывать.

    :param todo: инстанс клиента драйвера, возвращен фикстурой todo
    :return:
    """
    yield
    time.sleep(0.3)
    todo.click_all()
    todo.delete_all_notes()