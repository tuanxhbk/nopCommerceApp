from selenium import webdriver
import pytest


# from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser.........")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser.........")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser.........")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ##############
# It's hook for adding environment info into HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Tuan'


# It's hook to delete/modify environment info into HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
