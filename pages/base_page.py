from playwright.sync_api import Page, expect
from config.config import BASE_URL
from utils.logger import get_logger

class BasePage:

    SEARCH_LINE = "//input[@class='Search__input']"
    SEARCH_LINE_INPUT = "(//input[@class='Search__input'])[2]"
    SEARCH_QUERY = "//div[@class='SearchResults__item--bordered']//div[contains(text(), 'Рестобар')]"
    ACCERT_COOKIES = "//span[@class='Button__text' and contains(text(), 'Принять')]"
    FOOD_MENU_ITEM = "(//div[@title='Еда']//div[contains(text(), 'Еда')])[1]"
    RESTAURANT_FOOD_MENU_ITEM = "//a[text()='Рестораны']"
    AFISHA_SECTION = "//a[@title='Афиша, кино']"
    NEW_YEAR_SECTION = "//div[contains(text(), 'НГ 2026')]"
    FIND_CITY = "//input[@placeholder='поиск по названию']"
    DEFAULT_CITY = "//span[@title='Минск']"
    NEWS_SECTION = "//div[@class='ArticleItem JournalWidget__item']"
    COOKIES_BANNER = "//div[@class='CookiesNotificationBy__wrapper']"


    def __init__(self, page, timeout=20000):
        self.page = page
        self.timeout = timeout
        self.log = get_logger(self.__class__.__name__)


    def open_page(self, url):
        self.log.info(f"Opening {url}")
        self.page.goto(url, timeout=15000)

    def click(self, selector: str):
        self.log.info(f"Click")
        self.page.click(selector, timeout=self.timeout)

    def open_filters(self):
        self.log.info(f"Open filters section")
        self.page.click(BasePage.RESTAURANT_FOOD_MENU_ITEM, timeout=self.timeout)

    def choose_luna_page_in_search_line(self):
        self.log.info(f"Choose luna page in search line")
        self.page.click(BasePage.SEARCH_QUERY, timeout=self.timeout)

    def check_page_url(self, page_url: str):
        self.log.info(f"Check {page_url} is valid")
        self.page.wait_for_url(page_url, timeout=self.timeout)
        assert self.page.url == page_url, f"Expected {page_url}, but got {self.page.url}"


    def fill_text_in_search_line(self, text):
        self.log.info(f"Fill in {text}")
        self.page.click(BasePage.SEARCH_LINE, timeout=self.timeout)
        self.page.click(BasePage.SEARCH_LINE_INPUT, timeout=self.timeout)
        self.page.type(BasePage.SEARCH_LINE_INPUT, text, timeout=self.timeout)

    def get_text(self, selector: str) -> str:
        self.log.info(f"Get text from {selector}")
        return self.page.text_content(selector, timeout=self.timeout)

    def is_visible(self, selector: str) -> bool:
        self.log.info(f"Check {selector} is visible")
        return self.page.is_visible(selector, timeout=self.timeout)

    def wait_for_element(self, selector: str):
        self.log.info(f"Wait for element {selector} is visible")
        self.page.wait_for_selector(selector, timeout=self.timeout)

    def open_new_year_section(self):
        self.log.info(f"Open new year section")
        self.page.click(self.NEW_YEAR_SECTION, timeout=self.timeout)

    def fill_city(self, city: str):
        self.log.info(f"Fill in {city}")
        self.page.click(BasePage.DEFAULT_CITY, timeout=self.timeout)
        self.page.fill(BasePage.FIND_CITY, city, timeout=self.timeout)
        city_list_locator = self.page.locator("//div[@class='CityFilter__modalList']")
        city_list_locator.wait_for(state="visible", timeout=self.timeout)
        city_list_locator.locator("div").first.click(timeout=self.timeout)


    def url_is_valid(self,  expected_url_part):
        self.log.info(f"Check url is valid")
        current_url = self.page.url
        expected_url = f'https://www.relax.by/main/{expected_url_part}'
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {self.page.url}"


    def assert_news_matches_selected_city(self, city):
        self.log.info(f"Assert news matches {city} city")
        items = self.page.locator("div.ArticleItem.JournalWidget__item")
        count = items.count()
        for i in range(count):
            text = items.nth(i).inner_text().strip()
            assert f"Новости {city}а".lower() in text.lower(), f"Element {i} does not contain 'новости {city}а'. Got: {text}"

    @property
    def restaurants_section(self):
        return self.page.locator(BasePage.FOOD_MENU_ITEM)

    def open_restaurants_section(self):
        self.log.info(f"Open restaurants section")
        self.restaurants_section.click(timeout=self.timeout)

    @property
    def cookies(self):
        return self.page.locator(BasePage.COOKIES_BANNER)

    def cookies_is_visible(self):
        self.log.info(f"Check if cookies is visible")
        assert self.cookies.is_visible(), "Cookies banner is not visible"

    def accept_cookies(self):
        self.log.info(f"Click accept cookies")
        self.page.click(BasePage.ACCERT_COOKIES, timeout=self.timeout)

    @property
    def afisha_section(self):
        return self.page.locator(self.AFISHA_SECTION).first

    def open_afisha_section(self):
        self.log.info(f"Open afisha section")
        self.afisha_section.click(timeout=self.timeout)







