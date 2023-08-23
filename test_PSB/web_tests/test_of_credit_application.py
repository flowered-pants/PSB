import allure
from test_PSB.pages.page_of_applacation_to_getting_a_credit import CreditApplicationPage

credit_application_page = CreditApplicationPage()
def test_of_making_credit_application(browser_managment):
    with allure.step('Переход на страницу с заполнением заявки на кредит'):
        credit_application_page.open_page()
    with allure.step('Выбор кредита'):
        credit_application_page.choose_a_loan()
    with allure.step('Заполнение заявки на кредит'):
        credit_application_page.filling_out_application()
    with allure.step('Подтверждение данных'):
        credit_application_page.data_confirmation()

