# -*- coding: utf-8 -*-
import allure
from faker import Faker


@allure.step("Проверка статуса и содержимого записи")
def check_text_and_status(fact, expected):
    """
    Специализированная функция
    Проверка соответствия количества записей, а также их содержимого и статуса
    ожидаемому результату
    :return:
    """
    assert len(fact) == len(expected), "Unexpected number of notes"
    if len(fact) > 0:
        for ind in range(len(expected)):
            assert fact[ind]["status"] == expected[ind][
                "status"], "Incorrect status of note"
            assert fact[ind]["text"] == expected[ind][
                "text"], "Incorrect text of note"


@allure.step("Проверка корректности количества активных и выполненных записей")
def check_notes_count(fact_from_bottom, fact_active, fact_completed,
                      expected_bottom, expected_active, expected_completed):
    """
    Специализированная функция для теста с генерируемыми данными
    Проверка соответствия количества записей и их типа
    :return:
    """
    assert fact_from_bottom == expected_bottom, \
        "Incorrect active notes count in bottom bar"
    assert fact_active == expected_active, "Incorrect active notes count"
    assert fact_completed == expected_completed, "Incorrect active notes count"


@allure.step("Генерация тесткейса")
def generate_case(case_data):
    """
    Специализированная функция для теста с генерируемыми данными
    Генерирует данные, возвращает тестовый набор из шагов теста и ожидаемого
    результата
    :return: тестовый набор, тип - dict
    """
    fake = Faker()
    active = case_data["generated_steps"]["active"]
    marked = case_data["generated_steps"]["marked"]
    count = int(active) + int(marked)
    texts = fake.sentences(count)
    marked = fake.random_elements(elements=texts, length=marked, unique=True)
    add_steps = [dict(action="add_note", text=s) for s in texts]
    mark_steps = [dict(action="mark_note", text=s) for s in marked]
    steps = add_steps + mark_steps + case_data["extra_steps"]

    case = dict(steps=steps, expected=case_data["expected"])

    return case


def allure_attach_str_data(attach_name, attach_data, attachment_type="TEXT"):
    """
    Специализированная функция
    Прикрепляет в allure-отчет данные
    :param attach_name: имя прикрепляемого файла
    :param attach_data: данные которые должны быть записаны
    :param attachment_type: тип вложения.
    :return:
    """
    allure.attach(
        attach_data,
        attach_name,
        attachment_type=getattr(allure.attachment_type, attachment_type)
    )
