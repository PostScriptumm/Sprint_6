from selenium.webdriver.common.by import By


# локаторы страницы оформления заказа
class OrderPageLocators:

    # поле "Имя"
    name_input = [By.XPATH, ".//input[@placeholder='* Имя']"]

    # поле "Фамилия"
    surname_input = [By.XPATH, ".//input[@placeholder='* Фамилия']"]

    # поле "Адрес: куда привезти заказ"
    address_input = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]

    # поле "Станция метро"
    metro_station_input = [By.XPATH, ".//input[@placeholder='* Станция метро']"]

    # поле "Станция метро"
    metro_station_drop_down = [By.XPATH, ".//div[@class = 'select-search__select']"]

    # кнопка "Бульвар Рокоссовского" в выпадающем списке поля "Станция метро"
    station_rokossovsky_boulevard_button = [By.XPATH, ".//button[@value = '1']"]

    # кнопка "Черкизовская" в выпадающем списке поля "Станция метро"
    station_cherkizovskaya_button = [By.XPATH, ".//button[@value = '2']"]

    # поле "Телефон: на него позвонит курьер"
    phone_number_input = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]

    # кнопка "Далее"
    next_button = [By.XPATH, ".//button[text()='Далее']"]

    # поле "Когда привезти самокат"
    date_input = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]

    # датапикер поля "Когда привезти самокат"
    date_datepicker = [By.XPATH, ".//div[@class='react-datepicker']"]

    # дата "31.12.2023" в датапикере поля "Когда привезти самокат"
    date_datepicker_31 = [By.XPATH, ".//div[text() = '31']"]

    # дата "11.12.2023" в датапикере поля "Когда привезти самокат"
    date_datepicker_1 = [By.XPATH, ".//div[text() = '1']"]

    # поле "Срок аренды"
    rental_period_input = [By.XPATH, ".//div[text()='* Срок аренды']/parent::div"]

    # выпадающий список поля "Срок аренды"
    rental_period_drop_down = [By.XPATH, ".//div[@class = 'Dropdown-menu']"]

    # вариант выбора "Сутки" выпадающий списка поля "Срок аренды"
    rental_period_day = [By.XPATH, ".//div[text() = 'сутки']"]

    # вариант выбора "Двое суток" выпадающий списка поля "Срок аренды"
    rental_period_two_days = [By.XPATH, ".//div[text() = 'двое суток']"]

    # поле "Комментарий для курьера"
    comment_input = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]

    # нижняя кнопка "Заказать"
    order_button_low = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]

    # кнопка "Да" в модальном окне "Хотите оформить заказ?"
    yes_button = [By.XPATH, ".//button[text()='Да']"]

    # надпись "Заказ оформлен"
    processed_order = [By.XPATH, ".//div[text()='Заказ оформлен']"]
