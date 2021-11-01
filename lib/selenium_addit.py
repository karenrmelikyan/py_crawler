from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def is_xpath_exist(browser, xpath):
    try:
        return browser.find_element_by_xpath(xpath)
    except Exception as ex:
        return None


def scroll_by_element(browser, element) -> None:
    browser.execute_script("arguments[0].scrollIntoView();", element)


def scroll_window_down(browser) -> None:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')


def wait_element_by_tag_name(browser, tag_name, time_out) -> WebDriverWait:
    return WebDriverWait(browser, time_out).until(
        ec.visibility_of_element_located((By.TAG_NAME, tag_name)))


def wait_element_by_class_name(browser, class_name, time_out) -> WebDriverWait:
    return WebDriverWait(browser, time_out).until(
        ec.visibility_of_element_located((By.CLASS_NAME, class_name)))


def wait_element_by_xpath(browser, xpath_element, time_out) -> WebDriverWait:
    return WebDriverWait(browser, time_out).until(
        ec.visibility_of_element_located((By.XPATH, xpath_element)))
