"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from github_sign_in.model.pages.sign_in import SignInMobile, SignInDesktop


def test_github_desktop(window_size_desktop):
    # GIVEN
    sign_in = SignInDesktop()

    # WHEN
    sign_in.sign_in_button_click()

    # THEN
    sign_in.should_be_title_sign_in()


def test_github_mobile(window_size_mobile):
    # GIVEN
    sign_in = SignInMobile()

    # WHEN
    sign_in.toggle_navigation_click()
    sign_in.sign_in_button_click()

    # THEN
    sign_in.should_be_title_sign_in()
