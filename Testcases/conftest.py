from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=='Firefox':
        driver=webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")
        print("Mozilla")
    elif browser=='Chrome':
        driver=webdriver.Chrome()
        print("Chrome")
    else:
        driver=webdriver.Ie()
    return driver

def pytest_addoption(parser): #this will take the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##### Generate the html report ####

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Customer'] = 'Customers'
    config._metadata['Tester'] = 'Aditya'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_HOME", None)
    metadata.pop("Pugins", None)


