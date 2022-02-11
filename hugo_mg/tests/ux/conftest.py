"""pytest selenium wrapper"""
# pylint: disable=import-error
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

def pytest_addoption(parser):
    """pytest options"""
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--headless", action="store", default="No")
    parser.addoption("--username", action="store")
    parser.addoption("--userpass", action="store")
    parser.addoption("--url", action="store")

@pytest.fixture
def username(request):
    """get username option"""
    return  request.config.getoption("--username")

@pytest.fixture
def userpass(request):
    """get pasword option"""
    return  request.config.getoption("--userpass")

@pytest.fixture
def url(request):
    """get url option"""
    return  request.config.getoption("--url")

@pytest.fixture(scope="class")
def setup(request):
    """pylint setup for use with chrome and firefox"""
    requested_browser = request.config.getoption("--browser")
    requested_headless = request.config.getoption("--headless")
    if requested_browser.lower() == "firefox":
        options = FirefoxOptions()
        if requested_headless.lower() == "yes":
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if requested_headless.lower() == "yes":
            options.add_argument("--headless")
        options.add_argument('--hide-scrollbars')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--disable-popup-blocking")

        driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    # Start function
    yield driver

    # Teardown code
    driver.close()
    driver.quit()
