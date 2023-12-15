from selenium.webdriver.common.by import By


class BasePageLocators:

    # логотип "Самокат"
    scooter_logo = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]

    # логотип "Яндеск"
    yandex_logo = [By.XPATH, ".//a[@href='//yandex.ru']"]

    # кнопка "Заказать" в шапке страницы
    order_button_top = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]
