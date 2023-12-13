from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import pytest
import allure

from conftest import driver
from pages.main_page import MainPage, ImportantQuestions
from locators.main_page_locators import MainPageLocators
from locators.dzen_locators import DzenLocators
from data import AnswerTextData, UrlYandexDzenData, UrlPageData

question_answer_text = \
    [
        [MainPageLocators.price_question, MainPageLocators.price_answer, AnswerTextData.price],
        [MainPageLocators.several_scooters_question, MainPageLocators.several_scooters_answer, AnswerTextData.several],
        [MainPageLocators.time_rent_question, MainPageLocators.time_rent_answer, AnswerTextData.time_rent],
        [MainPageLocators.today_order_question, MainPageLocators.today_order_answer, AnswerTextData.today_order],
        [MainPageLocators.extension_question, MainPageLocators.extension_answer, AnswerTextData.extension],
        [MainPageLocators.charger_question, MainPageLocators.charger_answer, AnswerTextData.charger],
        [MainPageLocators.cancel_question, MainPageLocators.cancel_answer, AnswerTextData.cancel],
        [MainPageLocators.delivery_area_question, MainPageLocators.delivery_area_answer, AnswerTextData.delivery_area]
    ]


class TestImportantQuestions:

    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Переходим к разделу вопросы о важном, нажимаем на вопрос, сравниваем текст ответа')
    @pytest.mark.parametrize('question, answer, text', question_answer_text)
    def test_drop_down_list_of_important_questions(self, driver, question, answer, text):
        answers = MainPage(driver)
        answers.get_main_page()
        answers = ImportantQuestions(driver)
        answers.scroll_to_important_questions()
        answers.click_question(question, answer)
        assert answers.get_answer_text(answer) == text


class TestHeaderLogo:

    @allure.title('Проверка перехода на главную страницу при нажатии на лого Самокат')
    @allure.description('Переходим на страницу заказа, нажимаем на лого самокат, проверяем возвращение на главную')
    def test_click_scooter_logo_in_header(self, driver):
        logo = MainPage(driver)
        logo.get_main_page()
        logo.click_order_button(MainPageLocators.order_button_top)
        logo.click_scooter_logo()
        assert logo.get_current_url() == UrlPageData.MAIN_PAGE_URL \
               and expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.training_simulator))

    @allure.title('Проверка перехода на страницу Дзена при нажатии на лого Яндекс')
    @allure.description('Нажимаем на лого Яндекс, проверяем, что перешли на страницу Дзен')
    def test_click_yandex_logo_in_header(self, driver):
        logo = MainPage(driver)
        logo.get_main_page()
        logo.click_yandex_logo()
        logo.go_to_dzen_page()
        assert logo.get_current_url() == UrlYandexDzenData.YANDEX_DZEN_URL \
               and expected_conditions.visibility_of_element_located((By.XPATH, DzenLocators.dzen_logo))
