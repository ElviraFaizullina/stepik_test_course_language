import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("--language")
    language = None
    if language_name == "ru":
        print("\nthe website opens in Russian.")
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": "ru"})
        browser = webdriver.Chrome(options=options)
    elif language_name == "en":
        print("\nthe website opens in English.")
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": "en"})
        browser = webdriver.Chrome(options=options)
    elif language_name == "es":
        print("\nthe website opens in Spain.")
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": "es"})
        browser = webdriver.Chrome(options=options)
    elif language_name == "fr":
        print("\nthe website opens in French.")
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": "fr"})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language must be selected")
    yield browser
    print("\nquit browser..")
    browser.quit()

