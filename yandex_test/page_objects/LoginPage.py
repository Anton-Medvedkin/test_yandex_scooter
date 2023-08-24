from locators import OrderFormPageLocators
from page_objects.BasePage import BasePage

class LoginPage(BasePage):

   def filling_text_fields_one(self, name, surname, address, phone):
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_NAME).clear()
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_NAME).send_keys(name)
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_SURNAME).clear()
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_SURNAME).send_keys(surname)
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_ADDRESS).clear()
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_ADDRESS).send_keys(address)
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_METRO).clear()
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_METRO).click()
       self.find_element(OrderFormPageLocators.LOCATOR_LIST_ITEM_METRO_STATE).click()
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_PHONE).clear()
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_PHONE).send_keys(phone)

   def сlick_on_the_next_button(self):
       self.find_element(OrderFormPageLocators.LOCATOR_BUTTON_NEXT).click()

   def filling_text_fields_two(self, comment):
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_DATE).click()
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_DATE_CALENDAR).click()
       self.find_element(OrderFormPageLocators.LOCATOR_DROP_LEASE_TERM).click()
       self.find_element(OrderFormPageLocators.LOCATOR_LIST_ITEM_LEASE_TWENTY_FOUR_HOURS).click()
       self.find_element(OrderFormPageLocators.LOCATOR_CHECKBOX_COLOR_BLACK).click()
       self.find_element(OrderFormPageLocators.LOCATOR_TEXT_FIELD_COMMENT).send_keys(comment)

   def сlick_on_the_order_button(self):
       self.find_element(OrderFormPageLocators.LOCATOR_BUTTON_ORDER).click()

   def сlick_on_the_yes_button(self):
       self.find_element(OrderFormPageLocators.LOCATOR_BUTTON_YES).click()

   def check_order_status(self):
       return self.find_element(OrderFormPageLocators.LOCATOR_ORDER_STATUS_MESSAGE).text

   def check_error_name(self):
       return  self.find_element(OrderFormPageLocators.LOCATOR_ERROR_NAME).text

   def check_error_surname(self):
       return  self.find_element(OrderFormPageLocators.LOCATOR_ERROR_SURNAME).text

   def check_error_address(self):
       return  self.find_element(OrderFormPageLocators.LOCATOR_ERROR_ADDRESS).text

   def check_error_state(self):
       return  self.find_element(OrderFormPageLocators.LOCATOR_ERROR_STATE).text

   def check_error_number(self):
       return  self.find_element(OrderFormPageLocators.LOCATOR_ERROR_NUMBER).text