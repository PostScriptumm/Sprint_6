from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Ожидаем появление надписи "Учебный тренажёр"')
    def wait_training_simulator(self):
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.visibility_of_element_located(MainPageLocators.training_simulator))

    @allure.step('Нажимаем на кнопку Заказать')
    def click_order_button(self, order_button):
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.element_to_be_clickable(order_button))
        self.driver.find_element(*order_button).click()
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.visibility_of_element_located(OrderPageLocators.name_input))

    @allure.step('Нажимаем на лого Яндекс')
    def click_yandex_logo(self):
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.element_to_be_clickable(BasePageLocators.yandex_logo))
        self.driver.find_element(*BasePageLocators.yandex_logo).click()

    @allure.step('Нажимаем на лого Самокат')
    def click_scooter_logo(self):
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.element_to_be_clickable(BasePageLocators.scooter_logo))
        self.driver.find_element(*BasePageLocators.scooter_logo).click()


class ImportantQuestions(BasePage):

    @allure.step('Нажимаем на вопрос')
    def click_question(self, question_locator, answer_locator):
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(answer_locator))
