from selene import browser, be
import time

class CreditApplicationPage:
    def open_page(self):
        browser.open('https://ib.psbank.ru')
        browser.driver.execute_script('window.scrollBy(0, 300)')

    def choose_a_loan(self):
        time.sleep(5)
        browser.driver.execute_script('window.scrollBy(0, 600)')
        browser.element('.rui-cookie-consent').execute_script('element.remove()')
        browser.element('/html/body/rtl-root/rtl-main-page/div/div/rtl-page-block-host[3]'
                        '/rtl-financial-products/div/div/div[1]/div/div/div[2]/div/a').should(be.clickable).click()
        browser.element('.rui-sidenav-content-wrapper-content').execute_script('element.remove()')
        time.sleep(5)
        browser.element('.rui-sidenav-content-wrapper-content').execute_script('element.remove()')
        browser.driver.execute_script('window.scrollBy(0, 900)')

    def filling_out_application(self):
        browser.element('#mat-input-1').should(be.clickable).click().type('Петров')
        browser.element('#mat-input-2').should(be.clickable).click().type('Петр')
        browser.element('#mat-input-3').should(be.clickable).click().type('Петрович')
        browser.element('.rui-color-asphalt-400').should(be.clickable).click()
        browser.element('.ng-star-inserted [aria-label="1982"]').click()
        browser.element('.ng-star-inserted [aria-label="05.1982"]').click()
        browser.element('.ng-star-inserted[aria-label="20.05.1982"]').click()

        browser.driver.execute_script('window.scrollBy(0, 900)')
        browser.element('##formly_23_select_RussianFederationResident_0').click()
        browser.element('##formly_23_select_RussianFederationResident_0_0').click()





