from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

from data import UrlPageData
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.dzen_locators import DzenLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переходим на главную страницу сервиса')
    def get_main_page(self):
        self.driver.get(UrlPageData.MAIN_PAGE_URL)
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.visibility_of_element_located(MainPageLocators.training_simulator))

    @allure.step('Нажимаем на кнопку Заказать')
    def click_order_button(self, order_button):
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.element_to_be_clickable(order_button))
        self.driver.find_element(*order_button).click()
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.visibility_of_element_located(OrderPageLocators.name_input))

    @allure.step('Скролим вниз до кнопки Заказать')
    def scroll_to_order_button_low(self):
        element = self.driver.find_element(*MainPageLocators.order_button_low)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимаем на лого Яндекс')
    def click_yandex_logo(self):
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.element_to_be_clickable(MainPageLocators.yandex_logo))
        self.driver.find_element(*MainPageLocators.yandex_logo).click()

    @allure.step('Переходим к новой вкладке Дзена')
    def go_to_dzen_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.visibility_of_element_located(DzenLocators.dzen_logo))

    @allure.step('Получаем url страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Нажимаем на лого Самокат')
    def click_scooter_logo(self):
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.element_to_be_clickable(OrderPageLocators.scooter_logo))
        self.driver.find_element(*OrderPageLocators.scooter_logo).click()


class ImportantQuestions:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролим страницу к блоку Важные вопросы')
    def scroll_to_important_questions(self):
        element = self.driver.find_element(*MainPageLocators.important_questions)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимаем на вопрос')
    def click_question(self, question_locator, answer_locator):
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(answer_locator))

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, answer_locator):
        text = self.driver.find_element(*answer_locator).text
        return text
