import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage


class TestNavLinks:
    '''
    Тестирует ссылки навигации: переход по ним, проверка url
    '''
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.home_url = 'https://effective-mobile.ru/'
        self.home_page = HomePage(page)
        self.home_page.visit(self.home_url)

    def test_about(self):
        self.home_page.visit_about()
        assert f'{self.home_url}#about' == self.page.url

    def test_moreinfo(self):
        self.home_page.visit_moreinfo()
        assert f'{self.home_url}#moreinfo' == self.page.url

    def test_cases(self):
        self.home_page.visit_cases()
        assert f'{self.home_url}#cases' == self.page.url

    def test_reviews(self):
        self.home_page.visit_reviews()
        assert f'{self.home_url}#Reviews' == self.page.url

    def test_contacts(self):
        self.home_page.visit_contacts()
        assert f'{self.home_url}#contacts' == self.page.url