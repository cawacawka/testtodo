# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TodoHandler:
    """
    Класс для удобной работы с todomvc
    Содержит функции реализующие необходимый для тестов набор действий
    со станицей "списка дел"
    """
    def __init__(self, driver):
        """
        Инициализация класса
        :param driver: инстанс драйвера
        """
        self.driver = driver

    @allure.step("Добавление записи")
    def add_note(self, text):
        """
        Добавляет запись
        :param text: добавляемый текст, тип - str
        :return:
        """
        base_elem = self.driver.find_element_by_class_name("new-todo")
        base_elem.send_keys(text, Keys.ENTER)

    @allure.step("Удаление записи")
    def delete_note(self, text):
        """
        Удаляет запись, содержащую указанный текст
        :param text: текст, содержащийся в удаляемой записи, тип - str
        :return:
        """
        note = self.find_note(text)
        view = note.find_element_by_class_name('view')
        destroy = note.find_element_by_class_name('destroy')
        ActionChains(self.driver).move_to_element(view).move_to_element(
            destroy).perform()
        destroy.click()

    @allure.step("Редактирование записи")
    def edit_note(self, old, new):
        """
        Редактирует запись.
        Дваойной клик по записи, очистка формы и заполнение новым текстом
        :param old: старый текст
        :param new: новый текст
        :return:
        """
        note = self.find_note(old)
        wait = WebDriverWait(self.driver, 10)
        view = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "view")))
        edit = note.find_element_by_class_name('edit')
        ActionChains(self.driver).double_click(view).perform()
        if edit.is_displayed():
            # .clear() doesn't worked. don't know why
            edit.send_keys(Keys.CONTROL + "a")
            edit.send_keys(Keys.BACK_SPACE)
            edit.send_keys(new, Keys.ENTER)

    @allure.step("Изменение статуса записи")
    def mark_note(self, text):
        """
        Изменить состояние записи с active на complete или наоборот.
        :param text: текст, содержащийся в записи, тип - str
        :return:
        """
        note = self.find_note(text)
        note.find_element_by_class_name('toggle').click()

    @allure.step("Поиск записи по содержимому")
    def find_note(self, text):
        """
        Базовая функция, осуществяет поиск записи содержащей переданный текст
        :param text: искомый текст, тип - str
        :return: элемент страницы, запись содержащую указнный текст
        """
        list_todos = self.find_todo_list()
        todo = list_todos.find_element_by_xpath(
            "//li/div[@class='view']/label[contains(text(),{})]".format(
                self.prepare_string_to_xpath(text)))
        return todo.find_element_by_xpath('../..')

    def find_todo_list(self):
        """
        Базовая функция, осуществяет поиск "опорного" элемента, внутри которого
        содержатся все имеющиеся записи
        :return: элемент todolist страницы
        """
        return self.driver.find_element_by_class_name('todo-list')

    @allure.step("Поиск всех имеющихся записей")
    def find_all_notes(self):
        """
        Базовая функция, осуществяет поиск "опорного" элемента, внутри которого
        содержатся все имеющиеся записи
        :return: список (list) элементов внутри
        """
        notes = list()

        # dirty hack to better performance if list of tasks is empty
        # https://stackoverflow.com/a/8790334
        self.driver.implicitly_wait(0.3)
        exists = self.driver.find_elements_by_class_name('todo-list')
        self.driver.implicitly_wait(5)
        # end of hack

        if len(exists) != 0:
            list_todos = self.find_todo_list()
            all_notes = list_todos.find_elements_by_xpath(
                "//li/div[@class='view']/label[string-length(text()) > 0]")
            notes = [note_obj.find_element_by_xpath("../..") for note_obj in
                     all_notes]
        return notes

    @allure.step("Удаление всех имеющихся записей")
    def delete_all_notes(self):
        """
        Удаляет все имющиеся записи
        :return:
        """
        notes_obj = self.find_all_notes()
        for note_obj in notes_obj:
            wait = WebDriverWait(self.driver, 10)
            view = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "view")))
            destroy = note_obj.find_element_by_class_name('destroy')
            ActionChains(self.driver).move_to_element(view).move_to_element(
                destroy).perform()
            destroy.click()

    @allure.step("Получение количества активных записей на нижней панели TODO")
    def get_status_string(self):
        """
        Возвращает число active записей, указанных в строке на нижней панели
        приложения
        :return: число active записей, тип - int
        """
        status_str = self.driver.find_element_by_class_name('todo-count').text
        count_active = int(status_str.split()[0])
        return count_active

    @allure.step("Поиск всех активных записей")
    def find_all_active(self):
        """
        Возвращает список active записей
        :return: список active записей, тип - list
        """
        todos = self.find_todo_list()
        return todos.find_elements_by_xpath("//li[@class='']")

    @allure.step("Поиск всех завершенных записей")
    def find_all_completed(self):
        """
        Возвращает список completed записей
        :return: список completed записей, тип - list
        """
        todos = self.find_todo_list()
        return todos.find_elements_by_xpath("//li[@class='completed']")

    @allure.step("Клик по кнопке фильтра All")
    def click_all(self):
        """
        Клик по фильтру All на нижней панели приложения
        :return:
        """
        # dirty hack to better performance
        # https://stackoverflow.com/a/8790334
        self.driver.implicitly_wait(0.3)
        exists = self.driver.find_elements_by_class_name('filters')
        self.driver.implicitly_wait(5)
        # end of hack

        if len(exists):
            bottom_bar = self.driver.find_element_by_class_name('filters')
            bottom_bar.find_element_by_xpath(
                "//li/a[contains(text(), 'All')]").click()

    @allure.step("Клик по кнопке фильтра Active")
    def click_active(self):
        """
        Клик по фильтру Active на нижней панели приложения
        :return:
        """
        # dirty hack to better performance if list of tasks is empty
        # https://stackoverflow.com/a/8790334
        self.driver.implicitly_wait(0.3)
        exists = self.driver.find_elements_by_class_name('filters')
        self.driver.implicitly_wait(5)
        # end of hack
        if len(exists):
            bottom_bar = self.driver.find_element_by_class_name('filters')
            bottom_bar.find_element_by_xpath(
                "//li/a[contains(text(), 'Active')]").click()

    @allure.step("Клик по кнопке фильтра Completed")
    def click_completed(self):
        """
        Клик по фильтру Completed на нижней панели приложения
        :return:
        """
        # dirty hack to better performance if list of tasks is empty
        # https://stackoverflow.com/a/8790334
        self.driver.implicitly_wait(0.3)
        exists = self.driver.find_elements_by_class_name('filters')
        self.driver.implicitly_wait(5)
        # end of hack
        if len(exists):
            bottom_bar = self.driver.find_element_by_class_name('filters')
            bottom_bar.find_element_by_xpath(
                "//li/a[contains(text(), 'Completed')]").click()

    @allure.step("Клик по кнопке Clear-completed")
    def click_clear(self):
        """
        Клик по кнопке Clear-completed на нижней панели приложения
        :return:
        """
        # dirty hack to better performance if list of tasks is empty
        # https://stackoverflow.com/a/8790334
        self.driver.implicitly_wait(0.3)
        exists = self.driver.find_elements_by_class_name('filters')
        self.driver.implicitly_wait(5)
        # end of hack
        if len(exists):
            self.driver.find_element_by_class_name('clear-completed').click()

    @allure.step("Клик по кнопке Toggle-all")
    def click_toggle_all(self):
        """
        Клик по кнопке toggle-all
        :return:
        """
        self.driver.find_element_by_xpath("//label[@for='toggle-all']").click()

    @allure.step("Обновление страницы")
    def refresh_page(self):
        """
        Обновить страницу
        :return:
        """
        self.driver.refresh()

    @staticmethod
    def prepare_string_to_xpath(st):
        """
        Формирует корректную строку для форматирования внутри xpath
        :return: готовая для xpath строка, тип - str
        """
        if "'" not in st:
            return "'{}'".format(st)
        if '"' not in st:
            return '"{}"'.format(st)

        return "concat('{}')".format(st.replace("'", "',\"'\",'"))

    # TEST SPECIFIED FUNCTIONS
    @allure.step("Получение содержимого и статуса всех записей")
    def get_notes_text_and_status(self):
        """
        Специализированная функция
        Перебирает все имеющиеся записи и создает список из словарей
        {
            "text": <note text>,
            "status": <note status>
        }
        для последующего удобного анализа
        :return: список словарей с информацией о записях, тип - list
        """
        notes_obj = self.find_all_notes()
        if notes_obj:
            result = list()
            for note_obj in notes_obj:
                text = note_obj.find_element_by_class_name("view").text
                status = self.find_note(text).get_attribute("class")
                info = {
                    "text": text,
                    "status": status
                }
                result.append(info)
            return result
        return notes_obj

    @allure.step("Создание скриншота")
    def take_screenshot(self, png_path):
        """
        Специализированная функция
        Делает скриншот текущего состояния страницы.
        :return:
        """
        self.driver.get_screenshot_as_file(png_path)

    @allure.step("Выполнение шагов теста")
    def do_steps(self, steps):
        """
        Специализированная функция
        Выполняет тестовый сценарий, последовательность вызова функций
        с передачей туда необходимых параметров
        :return:
        """
        for step in steps:
            if step["action"] == "add_note":
                self.add_note(step["text"])
            if step["action"] == "delete_note":
                self.delete_note(step["text"])
            if step["action"] == "mark_note":
                self.mark_note(step["text"])

            if step["action"] == "edit_note":
                self.edit_note(step["old_text"], step["new_text"])

            if step["action"] == "click_all":
                self.click_all()
            if step["action"] == "click_active":
                self.click_active()
            if step["action"] == "click_completed":
                self.click_completed()
            if step["action"] == "click_clear":
                self.click_clear()
            if step["action"] == "refresh_page":
                self.refresh_page()
            if step["action"] == "click_toggle_all":
                self.click_toggle_all()
