import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)

    yield driver
    time.sleep(10)