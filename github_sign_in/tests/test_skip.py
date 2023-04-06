"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser
from github_sign_in.model.pages.sign_in import SignInMobile, SignInDesktop


@pytest.fixture(params=['desktop-1024', 'desktop-1440', 'desktop-1920', 'mobile'])
def browser_open_for_skip(request):
    if request.param == 'desktop-1152':
        browser.config.window_width = 1152
        browser.config.window_height = 864
    if request.param == 'desktop-1440':
        browser.config.window_width = 1440
        browser.config.window_height = 960
    if request.param == 'desktop-1920':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    if request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844
    browser.open('https://github.com/')


@pytest.mark.parametrize("browser_open_for_skip", [
    pytest.param("desktop-1152"),
    pytest.param("desktop-1440"),
    pytest.param("desktop-1920"),
    pytest.param("mobile", marks=[pytest.mark.skip(reason="param for mobile")])
], indirect=True)
def test_github_desktop(browser_open_for_skip):
    # GIVEN
    sign_in = SignInDesktop()

    # WHEN
    sign_in.sign_in_button_click()

    # THEN
    sign_in.should_be_title_sign_in()


@pytest.mark.parametrize("browser_open_for_skip", [
    pytest.param("desktop-1024", marks=[pytest.mark.skip(reason="param for desktop")]),
    pytest.param("desktop-1440", marks=[pytest.mark.skip(reason="param for desktop")]),
    pytest.param("desktop-1920", marks=[pytest.mark.skip(reason="param for desktop")]),
    pytest.param("mobile")
], indirect=True)
def test_github_mobile(browser_open_for_skip):
    # GIVEN
    sign_in = SignInMobile()

    # WHEN
    sign_in.toggle_navigation_click()
    sign_in.sign_in_button_click()

    # THEN
    sign_in.should_be_title_sign_in()
