"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene.support.shared import browser
from github_sign_in.model.pages.sign_in import SignInMobile, SignInDesktop


@pytest.fixture(params=['desktop', 'mobile'])
def browser_open(request):
    if request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844
    if request.param == 'desktop':
        browser.config.window_width = 1440
        browser.config.window_height = 1080
    browser.open('https://github.com/')


@pytest.mark.parametrize("browser_open", ["desktop"], indirect=True)
def test_github_desktop(browser_open):
    # GIVEN
    sign_in = SignInDesktop()

    # WHEN
    sign_in.sign_in_button_click()

    # THEN
    sign_in.should_be_title_sign_in()


@pytest.mark.parametrize("browser_open", ["mobile"], indirect=True)
def test_github_mobile(browser_open):
    # GIVEN
    sign_in = SignInMobile()

    # WHEN
    sign_in.toggle_navigation_click()
    sign_in.sign_in_button_click()

    # THEN
    sign_in.should_be_title_sign_in()
