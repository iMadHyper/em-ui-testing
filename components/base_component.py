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