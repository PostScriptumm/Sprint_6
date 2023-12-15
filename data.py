from locators.main_page_locators import MainPageLocators


class UrlPageData:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/order'


class UrlYandexDzenData:
    YANDEX_DZEN_URL = 'https://dzen.ru/?yredirect=true'


class AnswerTextData:
    price = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    several = ('Пока что у нас так: один заказ — один самокат. '
               'Если хотите покататься с друзьями, '
               'можете просто сделать несколько заказов — один за другим.')

    time_rent = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                 'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                 'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')

    today_order = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    extension = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    charger = ('Самокат приезжает к вам с полной зарядкой. '
               'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
               'Зарядка не понадобится.')

    cancel = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    delivery_area = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


# параметры для тестирования блока Важные вопросы
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
