import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Неподдерживаемый браузер")
    yield driver
    driver.quit()



#Локаторы. Переменные (сократить).


