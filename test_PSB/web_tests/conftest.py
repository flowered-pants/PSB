import pytest
from selene import browser

@pytest.fixture
def browser_managment(scope='function'):
    browser.config.hold_browser_open = True
    browser.config.type_by_js = True
    browser.config.browser_name = 'firefox'
    yield browser
    browser.quit()
