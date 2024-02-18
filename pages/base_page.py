from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

from locators.dzen_locators import DzenLocators
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переходим к странице')
    def get_page(self, url, wait_element):
        self.driver.get(url)
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.visibility_of_element_located(wait_element))

    @allure.step('Скролим страницу')
    def scroll_to_element(self, element):
        element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переходим к новой вкладке Дзена')
    def go_to_dzen_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.visibility_of_element_located(DzenLocators.dzen_header))

    @allure.step('Получаем url страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получаем текст элемента')
    def get_text(self, element):
        text = self.driver.find_element(*element).text
        return text
