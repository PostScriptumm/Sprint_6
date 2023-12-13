import allure

from conftest import driver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class TestOrderFlow:

    # набор данных для тестирования сценария при нажатиии верхней кнопки "Заказать"
    options_test_top_button = ['Сергей', 'Ёжов', 'Лесная, 51', OrderPageLocators.station_cherkizovskaya_button,
                               '12345678901', OrderPageLocators.date_datepicker_1, OrderPageLocators.rental_period_day]

    # набор данных для тестирования сценария при нажатиии нижней кнопки "Заказать"
    options_test_low_button = ['Ва', 'Ли', 'Стр-0', OrderPageLocators.station_rokossovsky_boulevard_button,
                               '+123456789012',
                               OrderPageLocators.date_datepicker_31, OrderPageLocators.rental_period_two_days]

    @allure.title('Проверка ворк-флоу успешного заказа по кнопке Заказать в шапке страницы')
    @allure.description('Нажимаем на кнопку заказать в шапке страницы, заполняем обязательные поля, '
                        'проверяем, что появилось сообщение Заказ оформлен')
    def test_order_flow_top_button(self, driver):
        order = MainPage(driver)
        order.get_main_page()
        order.click_order_button(MainPageLocators.order_button_top)
        order = OrderPage(driver)
        order.full_order_flow(*self.options_test_top_button)
        assert 'Заказ оформлен' in order.get_processed_order_text()

    @allure.title('Проверка ворк-флоу успешного заказа по кнопке Заказать внизу страницы')
    @allure.description('Нажимаем на кнопку заказать внизу страницы, заполняем обязательные поля, '
                        'проверяем, что появилось сообщение Заказ оформлен')
    def test_order_flow_low_button(self, driver):
        order = MainPage(driver)
        order.get_main_page()
        order.scroll_to_order_button_low()
        order.click_order_button(MainPageLocators.order_button_low)
        order = OrderPage(driver)
        order.full_order_flow(*self.options_test_low_button)
        assert 'Заказ оформлен' in order.get_processed_order_text()
