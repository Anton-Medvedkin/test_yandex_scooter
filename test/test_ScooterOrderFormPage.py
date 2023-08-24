from page_objects import HomePage, OrderFormPage

class TestScooterOrder:

    def test_form_filing_using_above_button(self, browser):
        main_order_form_page = OrderFormPage(browser)
        main_order_form_page.go_to_site()
        main_home_page = HomePage(browser)
        main_home_page.click_on_the_cookie()
        main_home_page.click_on_the_order_button_above()
        main_order_form_page.filling_in_the_first_order_form("Антон", "Медведкин", "Лиможа", "+375298696154")
        main_order_form_page.сlick_on_the_next_button()
        main_order_form_page.filling_in_the_second_order_form("Очень жду свой заказ!")
        main_order_form_page.сlick_on_the_order_button()
        main_order_form_page.сlick_on_the_yes_button()
        assert "Заказ оформлен" in main_order_form_page.check_order_status()

    def test_form_filing_using_below_button(self, browser):
        main_order_form_page = OrderFormPage(browser)
        main_order_form_page.go_to_site()
        main_home_page = HomePage(browser)
        main_home_page.click_on_the_cookie()
        main_home_page.click_on_the_order_button_below()
        main_order_form_page.filling_in_the_first_order_form("Иван", "Иванов", "Ленина", "+375298475212")
        main_order_form_page.сlick_on_the_next_button()
        main_order_form_page.filling_in_the_second_order_form("Надеюсь заказ доставят вовремя!")
        main_order_form_page.сlick_on_the_order_button()
        main_order_form_page.сlick_on_the_yes_button()
        assert "Заказ оформлен" in main_order_form_page.check_order_status()




class TestFieldErrors:

    def test_errors_on_forms(self, browser):
        main_order_form_page = OrderFormPage(browser)
        main_order_form_page.go_to_site()
        main_home_page = HomePage(browser)
        main_home_page.click_on_the_cookie()
        main_home_page.click_on_the_order_button_above()
        main_order_form_page.сlick_on_the_next_button()
        assert main_order_form_page.check_error_name() == "Введите корректное имя"
        assert main_order_form_page.check_error_surname() == "Введите корректную фамилию"
        assert main_order_form_page.check_error_address() == "Введите корректный адрес"
        assert main_order_form_page.check_error_state() == "Выберите станцию"
        assert main_order_form_page.check_error_number() == "Введите корректный номер"








