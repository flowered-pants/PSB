from selene import be, have
import time
from selene.support.shared import browser


class CreditApplicationPage:
    def open_page(self):
        browser.open('https://ib.psbank.ru')
        browser.driver.execute_script('window.scrollBy(0, 300)')

    def choose_a_loan(self):
        time.sleep(5)
        browser.driver.execute_script('window.scrollBy(0, 600)')
        browser.element('.rui-cookie-consent').execute_script('element.remove()')
        browser.element('/html/body/rtl-root/rtl-main-page/div/div/rtl-page-block-host[3]'
                        '/rtl-financial-products/div/div/div[1]/div/div/div[2]/div/a').click()
        browser.element('.rui-sidenav-content-wrapper-content').execute_script('element.remove()')
        time.sleep(5)

    def filling_out_application(self):
        time.sleep(5)
        browser.element('.rui-sidenav-content-wrapper-content > .rui-cookie-consent').execute_script('element.remove()')
        browser.driver.execute_script('window.scrollBy(0, 900)')
        time.sleep(5)
        browser.driver.execute_script('window.scrollBy(0, 500)')
        browser.element('#mat-input-1').should(be.clickable).click().set_value('Петров')
        browser.element('#mat-input-2').should(be.clickable).click().set_value('Петр').press_tab()
        browser.element('#mat-input-3').should(be.clickable).click().set_value('Петрович').press_tab()
        browser.element('.rui-color-asphalt-400').should(be.clickable).click()
        browser.driver.execute_script('window.scrollBy(0, 300)')
        browser.element('.ng-star-inserted [aria-label="1982"]').click()
        browser.element('.ng-star-inserted [aria-label="05.1982"]').click()
        browser.element('.ng-star-inserted[aria-label="20.05.1982"]').click()
        browser.element('.wrapper > [data-appearance="outline"]').should(be.clickable).click()
        browser.element('#formly_23_select_RussianFederationResident_0').should(be.clickable).click()
        browser.element('#formly_23_select_RussianFederationResident_0_0').should(be.clickable).click()
        browser.element('#mat-select-value-5').should(be.clickable).click()
        browser.element('#formly_23_select_RussianEmployment_1_0').should(be.clickable).click()
        browser.element('#formly_26_input_Phone_0').click().set_value('99999999999')
        browser.driver.execute_script('window.scrollBy(0, 400)')
        browser.element('#formly_28_checkbox_PersonalDataProcessingAgreementConcent_0').click()
        browser.element('#formly_30_checkbox_ConsentPersonalDataPartners_0').click()
        browser.element('#formly_32_checkbox_BkiRequestAgreementConcent_0').click()
        browser.element('#formly_34_checkbox_PromotionAgreementConcent_0').click()
        browser.element('.registration-form__footer button').click()

        # проверки
        browser.element('div.confirm-section__name:nth-child(1) > b:nth-child(3)').should(have.text('Петров'))
        browser.element('div.confirm-section__name:nth-child(3) > b:nth-child(3)').should(have.text('Петр'))
        browser.element('div.confirm-section__name:nth-child(5) > b:nth-child(3)').should(have.text('Петрович'))
        browser.element('.confirm-section__birthdate > b:nth-child(3)').should(have.text('20.05.1982'))
        browser.element('.confirm-section__mobile-phone > b:nth-child(3)').should(have.text('+7 (999) 999-99-99'))

    def data_confirmation(self):
        browser.element('.confirm-data__confirm-registration-button').click()


