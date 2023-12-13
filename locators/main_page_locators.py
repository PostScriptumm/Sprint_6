from selenium.webdriver.common.by import By


# локаторы главной страницы
class MainPageLocators:

    # надпись "Учебный тренажер"
    training_simulator = [By.XPATH, ".//div[text()='Учебный тренажер']"]

    # надпись "Вопросы о важном"
    important_questions = [By.XPATH, ".//div[text()='Вопросы о важном']"]

    # вопрос "Сколько это стоит? И как оплатить?"
    price_question = [By.ID, "accordion__heading-0"]

    # ответ "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    price_answer = [By.XPATH, ".//div[@id='accordion__panel-0']/child::p"]

    # вопрос "Хочу сразу несколько самокатов! Так можно?"
    several_scooters_question = [By.ID, "accordion__heading-1"]

    # ответ "Пока что у нас так: один заказ — один самокат.
    # Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    several_scooters_answer = [By.XPATH, ".//div[@id='accordion__panel-1']/child::p"]

    # вопрос "Как рассчитывается время аренды?"
    time_rent_question = [By.ID, "accordion__heading-2"]

    # ответ "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня.
    # Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру.
    # Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.
    time_rent_answer = [By.XPATH, ".//div[@id='accordion__panel-2']/child::p"]

    # вопрос "Можно ли заказать самокат прямо на сегодня?"
    today_order_question = [By.ID, "accordion__heading-3"]

    # ответ "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    today_order_answer = [By.XPATH, ".//div[@id='accordion__panel-3']/child::p"]

    # вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    extension_question = [By.ID, "accordion__heading-4"]

    # ответ "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    extension_answer = [By.XPATH, ".//div[@id='accordion__panel-4']/child::p"]

    # вопрос "Вы привозите зарядку вместе с самокатом?"
    charger_question = [By.ID, "accordion__heading-5"]

    # ответ "Самокат приезжает к вам с полной зарядкой.
    # Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    charger_answer = [By.XPATH, ".//div[@id='accordion__panel-5']/child::p"]

    # вопрос "Можно ли отменить заказ?"
    cancel_question = [By.ID, "accordion__heading-6"]

    # ответ "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    cancel_answer = [By.XPATH, ".//div[@id='accordion__panel-6']/child::p"]

    # вопрос "Я жизу за МКАДом, привезёте?"
    delivery_area_question = [By.ID, "accordion__heading-7"]

    # ответ "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    delivery_area_answer = [By.XPATH, ".//div[@id='accordion__panel-7']/child::p"]

    # кнопка "Заказать" в шапке страницы
    order_button_top = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]

    # кнопка "Заказать" внизу страницы
    order_button_low = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/child::button"]

    # логотип "Яндеск"
    yandex_logo = [By.XPATH, ".//a[@href='//yandex.ru']"]
