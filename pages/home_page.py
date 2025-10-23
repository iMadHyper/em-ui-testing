from playwright.sync_api import Page
from .base_page import BasePage
from components.navbar_component import NavbarComponent


class HomePage(BasePage):
    def __init__(self, page: Page):
        '''
        :param page: Экземпляр страницы playwright
        '''
        super().__init__(page)

        self.navbar = NavbarComponent(page)

    def visit_about(self):
        self.navbar.about_link.click()
        self.page.wait_for_load_state('networkidle')

    def visit_moreinfo(self):
        self.navbar.moreinfo_link.click()
        self.page.wait_for_load_state('networkidle')

    def visit_cases(self):
        self.navbar.cases_link.click()
        self.page.wait_for_load_state('networkidle')

    def visit_reviews(self):
        self.navbar.reviews_link.click()
        self.page.wait_for_load_state('networkidle')

    def visit_contacts(self):
        self.navbar.contacts_link.click()
        self.page.wait_for_load_state('networkidle')