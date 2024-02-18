from selenium import webdriver
import pytest


# фикстура setup_teardown
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
