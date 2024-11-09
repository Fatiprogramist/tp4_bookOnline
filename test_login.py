from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Открываем браузер Chrome и заходим на страницу входа в интернет-магазин
driver = webdriver.Chrome()
driver.get("file:///C:/Users/user/Desktop/s5/testing/tp4/bookStore.html")
time.sleep(10)

# Вводим email и пароль
driver.find_element(By.ID, "email").send_keys("fatima43tair@gmail.com")
print("Email успешно введен")
driver.find_element(By.ID, "password").send_keys("password123")
print("Пароль успешно введен")
driver.find_element(By.TAG_NAME, "button").click()
print("Кнопка входа успешно нажата")

# Ожидаем появления всплывающего сообщения и принимаем его
try:
    alert = Alert(driver)
    alert_text = alert.text
    assert alert_text == "Login"
    alert.accept()
    
except:
    print("Всплывающее сообщение отсутствует")

# Добавляем небольшую задержку для перехода на следующую страницу, если необходимо
time.sleep(10)

# Проверяем, что перенаправление на страницу продуктов прошло успешно
assert "Products - Online Bookstore" in driver.title
driver.quit()

# Открываем браузер Chrome и заходим на страницу с продуктами
driver = webdriver.Chrome()
driver.get("file:///C:/Users/user/Desktop/s5/testing/tp4/products.html")

# Добавляем "Книгу 1" в корзину
driver.find_element(By.XPATH, "//li[contains(text(), 'Book 1')]//button").click()

try:
    # Ожидаем, пока "Книга 1" появится в элементах корзины
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "cartItems"), "Book 1")
    )
    # Ожидаем, пока "Итого: $10" появится в общей сумме
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "totalPrice"), "Total: $10")
    )

    # Проверка утверждений
    cart_text = driver.find_element(By.ID, "cartItems").text
    assert "Book 1" in cart_text
    assert "Total: $10" in driver.find_element(By.ID, "totalPrice").text
    print("Корзина и итоговая сумма успешно проверены")

finally:
    time.sleep(10)

# Нажимаем на ссылку "Contact Us"
driver.find_element(By.LINK_TEXT, "Contact Us").click()
print("Кнопка 'Contact Us' успешно проверена")

# Проверяем, что открыта страница с контактной формой
assert "contacts.html" in driver.current_url
time.sleep(10)

# Закрываем браузер
driver.quit()
