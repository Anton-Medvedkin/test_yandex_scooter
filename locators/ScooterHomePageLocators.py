from selenium.webdriver.common.by import By

class HomePageLocators:

    #Кнопка Заказать сверху экрана
    LOCATOR_HOME_PAGE_ORDER_BUTTON_ABOVE = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    #Кнопка Заказать снизу экрана
    LOCATOR_HOME_PAGE_ORDER_BUTTON_BELOW = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

    #Первый выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_1 = (By.XPATH, "//div[@id='accordion__heading-0' and @aria-controls='accordion__panel-0']")
    #Второй выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_2 = (By.XPATH, "//div[@id='accordion__heading-1' and @aria-controls='accordion__panel-1']")
    #Третий выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_3 = (By.XPATH, "//div[@id='accordion__heading-2' and @aria-controls='accordion__panel-2']")
    #Четвёртый выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_4 = (By.XPATH, "//div[@id='accordion__heading-3' and @aria-controls='accordion__panel-3']")
    #Пятый выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_5 = (By.XPATH, "//div[@id='accordion__heading-4' and @aria-controls='accordion__panel-4']")
    #Шестой выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_6 = (By.XPATH, "//div[@id='accordion__heading-5' and @aria-controls='accordion__panel-5']")
    #Седьмой выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_7 = (By.XPATH, "//div[@id='accordion__heading-6' and @aria-controls='accordion__panel-6']")
    #Восьмой выпадающий список
    LOCATOR_HOME_PAGE_DROP_LIST_8 = (By.XPATH, "//div[@id='accordion__heading-7' and @aria-controls='accordion__panel-7']")

    #Содержимое первого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_1 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-0' and @id='accordion__panel-0']/p")
    #Содержимое второго выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_2 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-1' and @id='accordion__panel-1']/p")
    #Содержимое третьего выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_3 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-2' and @id='accordion__panel-2']/p")
    #Содержимое четвёртого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_4 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-3' and @id='accordion__panel-3']/p")
    #Содержимое пятого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_5 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-4' and @id='accordion__panel-4']/p")
    #Содержимое шестого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_6 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-5' and @id='accordion__panel-5']/p")
    #Содержимое седьмого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_7 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-6' and @id='accordion__panel-6']/p")
    #Содержимое восьмого выпадающего списка
    LOCATOR_HOME_PAGE_PANEL_8 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-7' and @id='accordion__panel-7']/p")


    #Логотип Самокат
    LOCATOR_LOGO_SCOOTER = (By.XPATH, "//a[starts-with(@class,'Header_LogoScooter')]")
    #Логотип Яндекс
    LOCATOR_LOGO_YANDEX = (By.XPATH, "//a[starts-with(@class,'Header_LogoYandex')]")

    #Cookie
    LOCATOR_COOKIE = (By.XPATH, "//*[@id='rcc-confirm-button']")

    #Кнопка статуса заказа
    LOCATOR_ORDER_STATUS_BUTTON = (By.XPATH, "//button[starts-with(@class,'Header_Link') and text()='Статус заказа']")
    #Текстовое поле для ввода номера заказа
    LOCATOR_NUMBER_ORDER = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    #Кнопка отправки номера заказа
    LOCATOR_SEND_ORDER_NUMBER_BUTTON = (By.XPATH, "//button[starts-with(@class,'Button_Button') and text()='Go!']")
    #Картинка такого заказа нет
    LOCATOR_STATUS_IMG = (By.XPATH, "//div[starts-with(@class,'Track_NotFound')]//img[@alt='Not found']")

