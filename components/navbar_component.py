import allure

from playwright.sync_api import Page

from .base_component import BaseComponent
from elements.link import Link


class NavbarComponent(BaseComponent):
    '''
    Компонент меню навигации. Содержит ссылки: о нас, услуги, проекты, отзывы, контакты.
    Предостовляет метод для проверки отображения меню.
    '''
    def __init__(self, page: Page):
        '''
        :param page: Экземпляр страницы playwright
        '''
        super().__init__(page)

        # Сслыка [О нас]
        self.about_link = Link(page, '//a[@class="tn-atom" and contains(@href,"#about")]', 'About link')
        # Ссылка [Услуги]
        self.moreinfo_link = Link(page, 'div[data-elem-id="1680606406485"] a.tn-atom[href="#moreinfo"]', 'More info link')
        # Ссылка [Проекты]
        self.cases_link = Link(page, '//a[@class="tn-atom" and contains(@href,"#cases")]', 'Cases link')
        # Ссылка [Отзывы]
        self.reviews_link = Link(page, '//a[@class="tn-atom" and contains(@href,"#Reviews")]', 'Reviews link')
        # Ссылка [Контакты]
        self.contacts_link = Link(page, '//a[@class="tn-atom" and @href="#contacts"][normalize-space(text())="[ Контакты ]"]', 'Contacts link')
    
    @allure.step('Check that navbar is visible')
    def check_visible(self):
        '''
        Проверяет, что ссылки навигации отображаются
        '''
        self.about_link.check_visible()
        self.moreinfo_link.check_visible()
        self.cases_link.check_visible()
        self.reviews_link.check_visible()
        self.contacts_link.check_visible()