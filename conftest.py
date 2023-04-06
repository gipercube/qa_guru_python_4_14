import pytest
from selene.support.shared import browser


@pytest.fixture()
def window_size_mobile():
    browser.config.window_width = 390
    browser.config.window_height = 844
    browser.open('https://github.com/')


@pytest.fixture()
def window_size_desktop():
    browser.config.window_width = 1440
    browser.config.window_height = 1080
    browser.open('https://github.com/')


