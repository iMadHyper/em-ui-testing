import allure

from playwright.sync_api import Page, expect


class BaseComponent:
    '''
    Базовый компонент страницы

    Содержит общие методы:
    - открытие страницы
    - проверка текущего url
    '''
    def __init__(self, page: Page):
        '''
        :param page: Экземпляр страницы playwright
        '''
        self.page = page

    def visit(self, url: str):
        '''
        Открывает страницу по заданному url
        '''
        step = f'Opening the url "{url}"'

        with allure.step(step):
            self.page.goto(url)

    def check_current_url(self, expected_url: str):
        '''
        Проверяет, что текущий url соответствует ожидаемому
        '''
        step = f'Checking that current url matchers "{expected_url}"'

        with allure.step(step):
            expect(self.page).to_have_url(expected_url)