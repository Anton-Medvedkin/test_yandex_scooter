from selenium.webdriver.common.by import By

class HomePageLocators:
    #Кнопка Заказать сверху экрана
    LOCATOR_HOME_PAGE_ORDER_BUTTON_ABOVE = (By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[2]/button[1]")
    #Кнопка Заказать снизу экрана
    LOCATOR_HOME_PAGE_ORDER_BUTTON_UNDERNEATH = (By.XPATH, "//*[@id='root']/div/div/div[4]/div[2]/div[5]/button")

    #Первый выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_1 = (By.XPATH, "//*[@id='accordion__heading-0']")
    #Второй выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_2 = (By.XPATH, "//*[@id='accordion__heading-1']")
    #Третий выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_3 = (By.XPATH, "//*[@id='accordion__heading-2']")
    #Четвёртый выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_4 = (By.XPATH, "//*[@id='accordion__heading-3']")
    #Пятый выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_5 = (By.XPATH, "//*[@id='accordion__heading-4']")
    #Шестой выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_6 = (By.XPATH, "//*[@id='accordion__heading-5']")
    #Седьмой выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_7 = (By.XPATH, "//*[@id='accordion__heading-6']")
    #Восьмой выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_8 = (By.XPATH, "//*[@id='accordion__heading-7']")

    #Содержимое первого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_1 = (By.XPATH, "//*[@ id='accordion__panel-0']/p")
    #Содержимое второго выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_2 = (By.XPATH, "//*[@ id='accordion__panel-1']/p")
    #Содержимое третьего выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_3 = (By.XPATH, "//*[@ id='accordion__panel-2']/p")
    #Содержимое четвёртого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_4 = (By.XPATH, "//*[@ id='accordion__panel-3']/p")
    #Содержимое пятого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_5 = (By.XPATH, "//*[@ id='accordion__panel-4']/p")
    #Содержимое шестого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_6 = (By.XPATH, "//*[@ id='accordion__panel-5']/p")
    #Содержимое седьмого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_7 = (By.XPATH, "//*[@ id='accordion__panel-6']/p")
    #Содержимое восьмого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_8 = (By.XPATH, "//*[@ id='accordion__panel-7']/p")


    #Логотип Самокат
    LOCATOR_LOGO_SCOOTER = (By.XPATH, "//*[@id='root']/div/div[1]/div[1]/a[2]/img")
    #Логотип Яндекс
    LOCATOR_LOGO_YANDEX = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/a[1]/img")
    #Заголовок главной страницы
    LOCATOR_HOME_PAGE_CAPTION = (By.XPATH, "//*[@id='root']/div/div/div[2]/div[4]/text()[1]")

    #Cookie
    LOCATOR_COOKIE = (By.XPATH, "//*[@id='rcc-confirm-button']")

    #Кнопка статуса заказа
    LOCATOR_ORDER_STATUS_BUTTON = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[2]/button[2]")
    #Текстовое поле для ввода номера заказа
    LOCATOR_NUMBER_ORDER = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[3]/div/input")
    #Кнопка отправки номера заказа
    LOCATOR_NUMBER_ORDER_BUTTON = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[3]/button")
    #Картинка такого заказа нет
    LOCATOR_IMG = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/img")

