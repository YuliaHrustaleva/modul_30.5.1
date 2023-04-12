import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


def test_unicum_names(go_to_my_pets):
    '''Поверяем что на странице со списком моих питомцев, у всех питомцев разные имена'''

    # активируем неявное ожидание
    pytest.driver.implicitly_wait(5)

    # все имена
    names = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

    # Cоздаем список и добавляем имена
    pets_names = []

    for name in names:
        name = name.text
        pets_names.append(name)
        print()
        print(pets_names)
        print('name=', name)

        # проверяем количество питомцев с таким же именем среди уже имеющихся элементов
        # При r != 1 выходим из цикла
        r = pets_names.count(name)
        if r != 1:
            break

    # Проверяем, если r == 1, то повторяющихся имен нет.
    assert r == 1, "Есть питомцы с идентичными именами"
