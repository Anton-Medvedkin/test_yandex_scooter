from selenium.webdriver.common.by import By

class OrderFormPageLocators:

    #Текстовое поле для ввода имени
    LOCATOR_TEXT_FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    #Текстовое поле для ввода фамилии
    LOCATOR_TEXT_FIELD_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    #Текстовое поле для ввода адреса
    LOCATOR_TEXT_FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    #Текстовое поле для ввода станции метро
    LOCATOR_TEXT_FIELD_METRO = (By.XPATH, "//input[@class='select-search__input'and @placeholder='* Станция метро']")
    #Станция из списка
    LOCATOR_LIST_ITEM_METRO_STATE = (By.XPATH, "//div[@class='select-search__select']//*[contains(text(),'Черкизовская')]")
    #Текстовое поле для ввода телефона
    LOCATOR_TEXT_FIELD_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    #Кнопка Далее для отправки формы
    LOCATOR_BUTTON_NEXT = (By.XPATH, "//button[starts-with(@class,'Button_Button') and text()='Далее']")
    #Текстовое поле для даты заказа
    LOCATOR_TEXT_FIELD_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    #Календарь для ввода даты
    LOCATOR_TEXT_FIELD_DATE_CALENDAR = (By.XPATH, "//div[starts-with(@class,'react-datepicker__day react-datepicker__day') and @aria-label='Choose четверг, 10-е августа 2023 г.']")
    #Срок аренды
    LOCATOR_DROP_LEASE_TERM = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    #Выпадающий список для срока аренды сутки
    LOCATOR_LIST_ITEM_LEASE_TWENTY_FOUR_HOURS = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    # Выпадающий список для срока аренды двое суток
    LOCATOR_LIST_ITEM_LEASE_TWO_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    # Выпадающий список для срока аренды трое суток
    LOCATOR_LIST_ITEM_LEASE_THREE_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    # Выпадающий список для срока аренды четверо суток
    LOCATOR_LIST_ITEM_LEASE_FOUR_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")
    # Выпадающий список для срока аренды пятеро суток
    LOCATOR_LIST_ITEM_LEASE_FIVE_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']")
    # Выпадающий список для срока аренды шестеро суток
    LOCATOR_LIST_ITEM_LEASE_SIX_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='шестеро суток']")
    # Выпадающий список для срока аренды семеро суток
    LOCATOR_LIST_ITEM_LEASE_SEVEN_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']")
    #Цвет самоката чёрный
    LOCATOR_CHECKBOX_COLOR_BLACK = (By.XPATH, "//input[@id='black']")
    # Цвет самоката серый
    LOCATOR_CHECKBOX_COLOR_GREY = (By.XPATH, "//input[@id='grey']")
    #Комментарии
    LOCATOR_TEXT_FIELD_COMMENT = (By.XPATH, "//input[starts-with(@class,'Input_Input') and @placeholder='Комментарий для курьера']")
    #Кнопка заказать в конце формы
    LOCATOR_BUTTON_ORDER = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']")
    #Подтверждение заказа
    LOCATOR_BUTTON_YES = (By.XPATH, "//button[starts-with(@class,'Button_Button') and text()='Да']")
    #Статус заказа
    LOCATOR_ORDER_STATUS_MESSAGE = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")


    #Ошибка ввода имени
    LOCATOR_ERROR_NAME = (By.XPATH, "//div[starts-with(@class,'Input_ErrorMessage') and text()='Введите корректное имя']")
    #Ошибка ввода фамилии
    LOCATOR_ERROR_SURNAME = (By.XPATH, "//div[starts-with(@class,'Input_ErrorMessage') and text()='Введите корректную фамилию']")
    #Ошибка ввода адреса
    LOCATOR_ERROR_ADDRESS = (By.XPATH, "//div[starts-with(@class,'Input_ErrorMessage') and text()='Введите корректный адрес']")
    #Ошибка ввода станции
    LOCATOR_ERROR_STATE = (By.XPATH, "//div[starts-with(@class,'Order_MetroError') and text()='Выберите станцию']")
    #Ошибка ввода телефона
    LOCATOR_ERROR_NUMBER = (By.XPATH, "//div[starts-with(@class,'Input_ErrorMessage') and text()='Введите корректный номер']")
