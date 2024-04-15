import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_adoption(parser):
    parser.addoption("--browser name", action="store", default="chrome",
                     help="Choose browser: chrome")
    parser.addoption("--language", action="store",default="en-gb",
                     help="Language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome")
    yield browser
    print("\nquit browser..")
    browser.quit()