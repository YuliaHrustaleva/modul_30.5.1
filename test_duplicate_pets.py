import pytest
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_no_duplicate_pets(go_to_my_pets):
    '''Проверяем на отсутствие повторяющихся питомцев'''

    # активируем неявное ожидание
    pytest.driver.implicitly_wait(5)
    # все имена
    names = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

    # активируем неявное ожидание
    pytest.driver.implicitly_wait(5)
    # все породы
    breeds = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')

    # активируем неявное ожидание
    pytest.driver.implicitly_wait(5)
    # все возрасты
    ages = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')

    # Создаем пустой список и счетчик
    pets = []
    r = 0
    print()

    for i in range(len(names)):
        # Собираем полученные данные в массив
        pets.append({
            'name': names[i].text,
            'breed': breeds[i].text,
            'age': ages[i].text
        })

        print('pets[', str(i), ']=', pets[i])

        # проверяем количество питомцев с такими же данными среди имеющихся элементов
        # при повторе питомца выходим из цикла
        r = pets.count(pets[i])
        print('количество вхождений =', str(r))
        if r != 1:
            break

    assert r == 1, "Есть повторяющиеся питомцы (с одинаковыми именами, породой и возрастом)"



