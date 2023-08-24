from page_objects import HomePage, OrderFormPage

class TestScooterOrder:

    def test_form_filing_button_one(self, browser):
        main_login_page = OrderFormPage(browser)
        main_login_page.go_to_site()
        main_home_page = HomePage(browser)
        main_home_page.click_on_the_cookie()
        main_home_page.click_on_the_order_button_above()
        main_login_page.filling_in_the_first_order_form("Антон", "Медведкин", "Лиможа", "+375298696154")
        main_login_page.сlick_on_the_next_button()
        main_login_page.filling_in_the_second_order_form("Очень жду свой заказ!")
        main_login_page.сlick_on_the_order_button()
        main_login_page.сlick_on_the_yes_button()
        assert "Заказ оформлен" in main_login_page.check_order_status()

    def test_form_filing_button_two(self, browser):
        main_login_page = OrderFormPage(browser)
        main_login_page.go_to_site()
        main_home_page = HomePage(browser)
        main_home_page.click_on_the_cookie()
        main_home_page.click_on_the_order_button_below()
        main_login_page.filling_in_the_first_order_form("Иван", "Иванов", "Ленина", "+375298475212")
        main_login_page.сlick_on_the_next_button()
        main_login_page.filling_in_the_second_order_form("Надеюсь заказ доставят вовремя!")
        main_login_page.сlick_on_the_order_button()
        main_login_page.сlick_on_the_yes_button()
        assert "Заказ оформлен" in main_login_page.check_order_status()




class TestFieldErrors:

    def test_of_the_form(self, browser):
        main_login_page = OrderFormPage(browser)
        main_login_page.go_to_site()
        main_home_page = HomePage(browser)
        main_home_page.click_on_the_cookie()
        main_home_page.click_on_the_order_button_above()
        main_login_page.сlick_on_the_next_button()
        assert main_login_page.check_error_name() == "Введите корректное имя"
        assert main_login_page.check_error_surname() == "Введите корректную фамилию"
        assert main_login_page.check_error_address() == "Введите корректный адрес"
        assert main_login_page.check_error_state() == "Выберите станцию"
        assert main_login_page.check_error_number() == "Введите корректный номер"








