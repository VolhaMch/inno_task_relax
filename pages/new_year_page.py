from playwright.async_api import expect

from pages.base_page import BasePage

class NewYearPage(BasePage):
    CLOSE_NEW_YEAR_ADS = "(//div[starts-with( @ style, 'background-image')])[last()]"
    FIND_PLACE_FOR_NEW_YEAR = "//span[contains(text(), 'Где отметить Новый год?')]"
    START = "//button[contains(text(), 'Начать')]"
    CORPORATIVE = "//span[contains(text(), 'Корпоратив')]"
    NEXT = "//span[contains(text(), 'Далее')]"
    PLACE_OUTSIDE_CITY = "//p[contains(text(), 'За городом: база отдыха, коттедж, санаторий')]"
    INPUT_DATE_FIELD = "//input[@placeholder='19 или 26 декабря']"
    CHOSE_COST_500_MORE = "//div[@data-element-index='6']"
    NEED_SHOW = "//p[contains(text(), 'Желательно, чтобы было новогоднее шоу')]"
    LAST_STEP = "//span[contains(text(), 'Последний шаг')]"
    AGREE = "//span[@class='check']"

    def __init__(self, page):
        self.page = page
        self.frame_locator = page.frame_locator("iframe#marquiz__frame_684037f2c0a16f0019668180")

    def ignore_new_year_ads(self):
        locator = self.page.locator(self.CLOSE_NEW_YEAR_ADS)
        if locator.is_visible():
            locator.click(timeout=10000)

    def choose_find_place_for_new_year(self):
        self.page.locator(self.FIND_PLACE_FOR_NEW_YEAR).click(timeout=10000)
        self.frame_locator.wait_for()

    def start_find_place_for_new_year(self):
        self.frame_locator.locator(self.START).click(timeout=10000)

    def chose_destination_corporativ(self):
        self.frame_locator.locator(self.CORPORATIVE, timeout=self.timeout)

    def click_next_button(self):
        self.frame_locator.click(self.NEXT, timeout=self.timeout)

    def choose_outside_city_place(self):
        self.frame_locator.click(self.PLACE_OUTSIDE_CITY, timeout=self.timeout)

    def input_date(self, date):
        self.frame_locator.get_by_placeholder('19 или 26 декабря').fill(date)

    def choose_cost_500_more(self):
        self.frame_locator.click(self.CHOSE_COST_500_MORE, timeout=self.timeout)

    def input_city(self, city):
        self.frame_locator.get_by_placeholder('Минск').fill(city)

    def need_show(self):
        self.frame_locator.click(self.NEED_SHOW, timeout=self.timeout)

    def click_button_last(self):
        self.frame_locator.click(self.LAST_STEP, timeout=self.timeout)

    def agreement_page_is_visible(self):
        locator = self.frame_locator.locator(self.AGREE, timeout=self.timeout)
        expect(locator).to_be_visible()


