from selene import browser

class CreditApplicationPage:
    def open_page(self):
        browser.open('https://ib.psbank.ru')
        browser.driver.execute_script('window.scrollBy(0, 100)')