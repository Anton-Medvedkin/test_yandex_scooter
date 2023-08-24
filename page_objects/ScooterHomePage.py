from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_on_the_cookie(self):
        self.find_element(HomePageLocators.LOCATOR_COOKIE, time=10).click()

    def click_on_the_drop_down_list_1(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_DROP_LIST_1, time=10).click()
        return self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_PANEL_1).text

    def click_on_the_drop_down_list_2(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_DROP_LIST_2, time=10).click()
        return self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_PANEL_2).text

    def click_on_the_drop_down_list_3(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_DROP_LIST_3, time=10).click()
        return self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_PANEL_3).text

    def click_on_the_drop_down_list_4(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_DROP_LIST_4, time=10).click()
        return self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_PANEL_4).text

    def click_on_the_drop_down_list_5(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_DROP_LIST_5, time=10).click()
        return self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_PANEL_5).text

    def click_on_the_drop_down_list_6(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_DROP_LIST_6, time=10).click()
        return self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_PANEL_6).text

    def click_on_the_drop_down_list_7(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_DROP_LIST_7, time=10).click()
        return self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_PANEL_7).text

    def click_on_the_drop_down_list_8(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_DROP_LIST_8, time=10).click()
        return self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_PANEL_8).text

    def click_on_the_order_button_above(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_ORDER_BUTTON_ABOVE).click()

    def click_on_the_order_button_below(self):
        self.find_element(HomePageLocators.LOCATOR_HOME_PAGE_ORDER_BUTTON_BELOW).click()

    def click_on_the_logo_scooter(self):
        self.find_element(HomePageLocators.LOCATOR_LOGO_SCOOTER).click()

    def click_on_the_logo_yandex(self):
        self.find_element(HomePageLocators.LOCATOR_LOGO_YANDEX).click()

    def check_order_status(self, number):
        self.find_element(HomePageLocators.LOCATOR_ORDER_STATUS_BUTTON).click()
        self.find_element(HomePageLocators.LOCATOR_NUMBER_ORDER).send_keys(number)
        self.find_element(HomePageLocators.LOCATOR_SEND_ORDER_NUMBER_BUTTON).click()
        return self.find_element(HomePageLocators.LOCATOR_STATUS_IMG).get_attribute('src')


