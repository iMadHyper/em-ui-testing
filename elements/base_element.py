import allure

from playwright.sync_api import Page, Locator, expect


class BaseElement:
    '''
    Базовый элемент страницы

    Содержит общие методы:
    - получение локатора
    - клик по элементу
    - проверка видимости элемента
    '''
    def __init__(self, page: Page, locator_xpath: str, name: str):
        '''
        :param page: Экземпляр страницы playwright
        :paramn locator_xpath: xpath элемента для его поиска
        :param name: Название элемента (для логирования и allure)
        '''
        self.page = page
        self.locator_xpath = locator_xpath
        self.name = name
    
    @property
    def type_of(self) -> str:
        return 'base element'
    
    def get_locator(self) -> Locator:
        '''
        Формирует локатор элемента по xpath
        '''
        step = f'Getting locator with "xpath={self.locator_xpath}"'

        with allure.step(step):
            return self.page.locator(self.locator_xpath)
        
    def click(self):
        '''
        Клик по элементу
        '''
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator()
            locator.click()
    
    def check_visible(self):
        '''
        Проверяет, что элемент виден на странице
        '''
        step = f'Checking {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            locator = self.get_locator()
            expect(locator).to_be_visible()