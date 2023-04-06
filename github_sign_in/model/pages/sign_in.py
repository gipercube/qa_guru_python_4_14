from selene import have
from selene.support.shared import browser


class SignInMobile:
    def __init__(self):
        self.toggle_navigation = browser.element('.flex-order-2 .Button-content')
        self.sign_in_button = browser.element('[href="/login"]')
        self.title = browser.element('h1')

    def toggle_navigation_click(self):
        self.toggle_navigation.click()
        return self

    def sign_in_button_click(self):
        self.sign_in_button.click()
        return self

    def should_be_title_sign_in(self):
        assert self.title.should(have.text('Sign in to GitHub'))


class SignInDesktop:
    def __init__(self):
        self.sign_in_button = browser.element('[href="/login"]')
        self.title = browser.element('h1')

    def sign_in_button_click(self):
        self.sign_in_button.click()
        return self

    def should_be_title_sign_in(self):
        assert self.title.should(have.text('Sign in to GitHub'))
