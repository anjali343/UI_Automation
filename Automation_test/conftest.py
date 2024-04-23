import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://practice.automationtesting.in/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
