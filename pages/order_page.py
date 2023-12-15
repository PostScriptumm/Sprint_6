from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Вводим значение в поле Имя')
    def set_name_input(self, name):
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(name)

    @allure.step('Вводим значение в поле Фамилия')
    def set_surname_input(self, surname):
        self.driver.find_element(*OrderPageLocators.surname_input).send_keys(surname)

    @allure.step('Вводим значение в поле Адрес')
    def set_address_input(self, address):
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(address)

    @allure.step('Нажимаем на поле Метро')
    def click_metro_station_input(self):
        self.driver.find_element(*OrderPageLocators.metro_station_input).click()
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.visibility_of_element_located(OrderPageLocators.metro_station_drop_down))

    @allure.step('Выбираем станцию из выпадающего списка')
    def choose_metro_station_input(self, station):
        self.driver.find_element(*station).click()

    @allure.step('Вводим значение в поле Телефон')
    def set_phone_number_input(self, phone_number):
        self.driver.find_element(*OrderPageLocators.phone_number_input).send_keys(phone_number)

    @allure.step('Нажимаем на кнопку Далее')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.visibility_of_element_located(OrderPageLocators.date_input))

    @allure.step('Нажимаем на поле Дата')
    def click_date_input(self):
        self.driver.find_element(*OrderPageLocators.date_input).click()
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.visibility_of_element_located(OrderPageLocators.date_datepicker))

    @allure.step('Выбираем дату в датапикере')
    def choose_date_input(self, date):
        self.driver.find_element(*date).click()

    @allure.step('Нажимаем на поле Срок аренды')
    def click_rental_period_input(self):
        self.driver.find_element(*OrderPageLocators.rental_period_input).click()
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.element_to_be_clickable(OrderPageLocators.rental_period_drop_down))

    @allure.step('Выбираем срок аренды в выпадающем списке')
    def choose_rental_period_input(self, period):
        self.driver.find_element(*period).click()

    @allure.step('Нажимаем на кнопку Заказать')
    def click_order_button_low(self):
        self.driver.find_element(*OrderPageLocators.order_button_low).click()
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.element_to_be_clickable(OrderPageLocators.yes_button))

    @allure.step('Нажимаем на кнопку Да')
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()
        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.visibility_of_element_located(OrderPageLocators.processed_order))

    def full_order_flow(self, name, surname, address, station, number, date, period):
        self.set_name_input(name)
        self.set_surname_input(surname)
        self.set_address_input(address)
        self.click_metro_station_input()
        self.choose_metro_station_input(station)
        self.set_phone_number_input(number)
        self.click_next_button()
        self.click_date_input()
        self.choose_date_input(date)
        self.click_rental_period_input()
        self.choose_rental_period_input(period)
        self.click_order_button_low()
        self.click_yes_button()
