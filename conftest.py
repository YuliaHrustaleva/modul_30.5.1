import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/chromedriver.exe')

   pytest.driver.maximize_window()

   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

@pytest.fixture()
def go_to_my_pets():

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   # Нажимаем на ссылку "Мои питомцы"
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

def test_show_my_pets(go_to_my_pets):
   '''Проверяем что мы оказались на странице "Мои питомцы"'''

   if not pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
      pytest.driver.quit()
      raise Exception("Это не страница 'Мои питомцы'")


      # Проверяем что мы оказались на странице "Мои питомцы"
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

