from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import pytest
import allure

from conftest import driver
from pages.main_page import MainPage, ImportantQuestions
from locators.main_page_locators import MainPageLocators
from locators.dzen_locators import DzenLocators
from locators.base_page_locators import BasePageLocators
from data import question_answer_text, UrlYandexDzenData, UrlPageData


class TestImportantQuestions:

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Переходим к разделу вопросы о важном, нажимаем на вопрос, сравниваем текст ответа')
    @pytest.mark.parametrize('question, answer, text', question_answer_text)
    def test_drop_down_list_of_important_questions(self, driver, question, answer, text):
        answers = MainPage(driver)
        answers.get_page(UrlPageData.MAIN_PAGE_URL, MainPageLocators.training_simulator)
        answers = ImportantQuestions(driver)
        answers.scroll_to_element(MainPageLocators.important_questions)
        answers.click_question(question, answer)
        assert answers.get_text(answer) == text


class TestHeaderLogo:

    @allure.title('Проверка перехода на главную страницу при нажатии на лого Самокат')
    @allure.description('Переходим на страницу заказа, нажимаем на лого самокат, проверяем возвращение на главную')
    def test_click_scooter_logo_in_header(self, driver):
        logo = MainPage(driver)
        logo.get_page(UrlPageData.MAIN_PAGE_URL, MainPageLocators.training_simulator)
        logo.click_order_button(BasePageLocators.order_button_top)
        logo.click_scooter_logo()
        assert logo.get_current_url() == UrlPageData.MAIN_PAGE_URL \
               and expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.training_simulator))

    @allure.title('Проверка перехода на страницу Дзена при нажатии на лого Яндекс')
    @allure.description('Нажимаем на лого Яндекс, проверяем, что перешли на страницу Дзен')
    def test_click_yandex_logo_in_header(self, driver):
        logo = MainPage(driver)
        logo.get_page(UrlPageData.MAIN_PAGE_URL, MainPageLocators.training_simulator)
        logo.click_yandex_logo()
        logo.go_to_dzen_page()
        assert logo.get_current_url() == UrlYandexDzenData.YANDEX_DZEN_URL \
               and expected_conditions.visibility_of_element_located((By.XPATH, DzenLocators.dzen_header))
