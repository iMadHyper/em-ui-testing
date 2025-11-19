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
        self.home_page.check_current_url(f'{self.home_url}#about')
        self.home_page.navbar.check_visible()

    def test_moreinfo(self):
        self.home_page.visit_moreinfo()
        self.home_page.check_current_url(f'{self.home_url}#moreinfo')
        self.home_page.navbar.check_visible()

    def test_cases(self):
        self.home_page.visit_cases()
        self.home_page.check_current_url(f'{self.home_url}#cases')
        self.home_page.navbar.check_visible()

    def test_reviews(self):
        self.home_page.visit_reviews()
        self.home_page.check_current_url(f'{self.home_url}#Reviews')
        self.home_page.navbar.check_visible()

    def test_contacts(self):
        self.home_page.visit_contacts()
        self.home_page.check_current_url(f'{self.home_url}#contacts')
        self.home_page.navbar.check_visible()


# Скриншот при ошибке
# import allure
# @pytest.fixture(autouse=True)
# def attach_screenshot_on_fail(request, page):
#     yield
#     if request.node.rep_call.failed:
#         allure.attach(
#             page.screenshot(full_page=True),
#             name="screenshot_on_failure",
#             attachment_type=allure.attachment_type.PNG,
#         )