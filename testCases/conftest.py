from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):  # Launching browser using setup method using the passed from CLI
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser..............")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser..............")
    else:
        driver = webdriver.Edge()  # Launching Edge as default browser if no browser argument have been passed through CLI
        print("Launching Edge browser..............")
    return driver

    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Project Name": "Hybrid Framework Practice",
        "Module Name": "Customers",
        "Tester": "Shilpi",
    }


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
