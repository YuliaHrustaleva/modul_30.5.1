import pytest
from settings import valid_email, valid_password
from selenium.webdriver.common.by import By

def test_show_pet_friends(go_to_my_pets):
   '''Проверка карточек питомцев на наличие фото, имени, возраста и породы'''

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(3)

   # Проверяем, что мы оказались на странице "Мои питомцы"
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')



   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0









