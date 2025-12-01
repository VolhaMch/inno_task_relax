from playwright.sync_api import Page
from utils.config import BASE_URL

class BasePage:

    SEARCH_LINE = "//input[@class='Search__input']"
    SEARCH_LINE_INPUT = "(//input[@class='Search__input'])[2]"
    SEARCH_QUERY = "//div[@class='SearchResults__item--bordered']//div[contains(text(), 'Рестобар')]"
    ACCERT_COOKIES = "//span[@class='Button__text' and contains(text(), 'Принять')]"
    FOOD_MENU_ITEM = "(//div[@title='Еда']//div[contains(text(), 'Еда')])[1]"
    RESTAURANT_FOOD_MENU_ITEM = "//a[text()='Рестораны']"
    AFISHA_SECTION = "//a[@title='Афиша, кино']"

    def __init__(self, page, timeout=5000):
        self.page = page
        self.timeout = timeout

    def open_page(self, url):
        self.page.goto(url, timeout=10000)

    def click(self, selector: str):
        self.page.click(selector, timeout=self.timeout)

    def open_restaurants_section(self):
        self.page.click(BasePage.FOOD_MENU_ITEM, timeout=self.timeout)

    def open_filters(self):
        self.page.click(BasePage.RESTAURANT_FOOD_MENU_ITEM, timeout=self.timeout)

    def choose_luna_page_in_search_line(self):
        self.page.click(BasePage.SEARCH_QUERY, timeout=self.timeout)

    def check_page_url(self, page_url: str):
        self.page.wait_for_url(page_url, timeout=self.timeout)
        assert self.page.url == page_url, f"Expected {page_url}, but got {self.page.url}"

    def accept_cookies(self):
        self.page.click(BasePage.ACCERT_COOKIES, timeout=self.timeout)

    def fill_text_in_search_line(self, text):
        self.page.click(BasePage.SEARCH_LINE, timeout=self.timeout)
        self.page.click(BasePage.SEARCH_LINE_INPUT, timeout=self.timeout)
        self.page.type(BasePage.SEARCH_LINE_INPUT, text, timeout=self.timeout)

    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector, timeout=self.timeout)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector, timeout=self.timeout)

    def wait_for_element(self, selector: str):
        self.page.wait_for_selector(selector, timeout=self.timeout)

    def open_afisha_section(self):
        self.page.click(self.AFISHA_SECTION, timeout=self.timeout)
