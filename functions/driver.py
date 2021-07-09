import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def go_next(driver):
    driver.find_element_by_xpath("//*[contains(@ng-click, 'goNext()')]").click()


def wait_for_it(driver, name, by=By.CLASS_NAME, timeout=60):
    element_present = EC.presence_of_element_located((by, name))
    WebDriverWait(driver, timeout).until(element_present)


def send_keys_delay(driver, parola, delay=0.1):
    for lettera in parola:
        driver.send_keys(lettera)
        time.sleep(delay)
