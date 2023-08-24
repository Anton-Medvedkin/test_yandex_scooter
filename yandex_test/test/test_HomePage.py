import time
from page_objects import HomePage

class TestDropDownList:

    def test_drop_down_list(self, browser):
        main_home_page = HomePage(browser)
        main_home_page.go_to_site()
        main_home_page.click_on_the_cookie()
        assert main_home_page.click_on_the_drop_down_list_1() == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        assert main_home_page.click_on_the_drop_down_list_2() == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        assert main_home_page.click_on_the_drop_down_list_3() == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        assert main_home_page.click_on_the_drop_down_list_4() == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        assert main_home_page.click_on_the_drop_down_list_5() == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        assert main_home_page.click_on_the_drop_down_list_6() == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        assert main_home_page.click_on_the_drop_down_list_7() == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        assert main_home_page.click_on_the_drop_down_list_8() == "Да, обязательно. Всем самокатов! И Москве, и Московской области."


class TestLogo:

    def test_logo_scooter(self, browser):
        main_home_page = HomePage(browser)
        main_home_page.go_to_site()
        main_home_page.click_on_the_order_button_above()
        main_home_page.click_on_the_logo_scooter()
        assert main_home_page.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    def test_logo_yandex(self, browser):
        main_home_page = HomePage(browser)
        main_home_page.go_to_site()
        main_home_page.click_on_the_logo_yandex()
        main_home_page.driver.switch_to.window(main_home_page.driver.window_handles[1])
        time.sleep(5)
        assert main_home_page.driver.current_url == "https://dzen.ru/?yredirect=true"



class TestOrderStatus:

    def test_number_order_status(self, browser):
        main_home_page = HomePage(browser)
        main_home_page.go_to_site()
        assert main_home_page.check_order_status(123789) == "https://qa-scooter.praktikum-services.ru/assets/not-found.png"


