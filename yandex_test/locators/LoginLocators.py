from selenium.webdriver.common.by import By

class LoginPageLocators:
    #Заголовок формы для заполнения
    LOCATOR_CAPTION = (By.XPATH, "//*[@id='root']/div/div[2]/div[1]")
    #Текстовое поле для ввода имени
    LOCATOR_TEXT_FIELD_NAME = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/input")
    #Текстовое поле для ввода фамилии
    LOCATOR_TEXT_FIELD_SURNAME = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/input")
    #Текстовое поле для ввода адреса
    LOCATOR_TEXT_FIELD_ADDRESS = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[3]/input")
    #Текстовое поле для ввода станции метро
    LOCATOR_TEXT_FIELD_METRO = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/div/div/input")
    #Станция из списка
    LOCATOR_TEXT_FIELD_METRO_STATE = (By.XPATH, "//div[@class='select-search__select']//*[contains(text(),'Черкизовская')]")
    #Текстовое поле для ввода телефона
    LOCATOR_TEXT_FIELD_PHONE = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[5]/input")
    #Кнопка Далее для отправки формы
    LOCATOR_BUTTON_NEXT = (By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button")
    #Текстовое поле для даты заказа
    LOCATOR_TEXT_FIELD_DATE = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[1]/div/input")
    #Календарь для ввода даты
    LOCATOR_TEXT_FIELD_DATE_CALENDAR = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[3]")
    #Срок аренды
    LOCATOR_DROP_LEASE_TERM = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div[1]/div[1]")
    #Выпадающий список для срока аренды
    LOCATOR_DROP_LEASE = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div[2]/div[1]")
    #Цвет самоката
    LOCATOR_CHECKBOX_COLOR = (By.XPATH, "//*[@id='black']")
    #Комментарии
    LOCATOR_TEXT_FIELD_COMMENT = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/input")
    #Кнопка заказать в конце формы
    LOCATOR_BUTTON_ORDER = (By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button[2]")
    #Подтверждение заказа
    LOCATOR_BUTTON_YES = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/div[2]/button[2]")
    #Статус заказа
    LOCATOR_ORDER_STATUS = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")


    #Ошибка ввода имени
    LOCATOR_ERROR_NAME = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div")
    #Ошибка ввода фамилии
    LOCATOR_ERROR_SURNAME = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div")
    #Ошибка ввода адреса
    LOCATOR_ERROR_ADDRESS = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[3]/div")
    #Ошибка ввода станции
    LOCATOR_ERROR_STATE = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/div[2]")
    #Ошибка ввода телефона
    LOCATOR_ERROR_NUMBER = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[5]/div")
