"""
Smoke test
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

URL = 'https://testqastudio.me/'

def test_product_view_sku(browser):
    """
    Test case WERT-1
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # open Browser in maximized mode
    chrome_options.add_argument("--disable-infobars") # disabling infobars
    chrome_options.add_argument("--disable-extensions") # disabling extensions
    chrome_options.add_argument("--disable-gpu") #  applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
    # chrome_options.add_argument("--headless")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    browser.get(url=URL)
		# ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
		# ищем по селектору карточку "ДИВВИНА Журнальный столик" и кликаем по нему,
    # чтобы просмотреть детали
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]')
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"

    