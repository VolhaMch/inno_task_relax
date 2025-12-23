import time

import pytest
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
        self.frame = page.frame_locator("iframe[src*='marquiz']")

    async def start_find_place_for_new_year(self):
        # show quiz through JS
        await self.page.evaluate(
            "() => window.Marquiz && Marquiz.showModal()"
        )

        await self.page.wait_for_selector(
            "iframe[src*='marquiz']", state="visible", timeout=45000
        )

        frame = self.page.frame_locator("iframe[src*='marquiz']")

        start_button = frame.locator("button:has-text('Начать')")
        await start_button.wait_for(state="visible", timeout=30000)
        await self.page.screenshot(path="quiz_before_click.png")

        await start_button.click()
        await self.page.screenshot(path="quiz_after_click.png")

        self.frame = frame

    async def chose_destination_corporativ(self):
        await self.frame.wait_for_selector(self.CORPORATIVE, state="visible", timeout=20000)
        await self.frame.locator(self.CORPORATIVE).click()

    async def click_next_button(self):
        frame = self.frame.wait_for_selector(self.NEXT, state="visible", timeout=20000)
        await frame.locator(self.NEXT).click()


    def choose_find_place_for_new_year(self):
        # self.page.wait_for_selector("a.marquiz-pops__body")
        self.page.locator('//a[@href="#popup:marquiz_684037f2c0a16f0019668180"]').click()




    def choose_outside_city_place(self):
        frame = self.frame.wait_for_selector(self.PLACE_OUTSIDE_CITY)
        frame.locator(self.PLACE_OUTSIDE_CITY).click()

    def input_date(self,  date):
        self.frame.get_by_placeholder('19 или 26 декабря').fill(date)

    def choose_cost_500_more(self):
        self.frame.click(self.CHOSE_COST_500_MORE, timeout=self.timeout)

    def input_city(self, city):
        self.frame.get_by_placeholder('Минск').fill(city)

    def need_show(self):
        self.frame.click(self.NEED_SHOW, timeout=self.timeout)

    def click_button_last(self):
        self.frame.click(self.LAST_STEP, timeout=self.timeout)

    def agreement_page_is_visible(self):
        locator = self.frame.locator(self.AGREE, timeout=self.timeout)
        expect(locator).to_be_visible()

    def ignore_new_year_ads(self):
        locator = self.page.locator(
            self.CLOSE_NEW_YEAR_ADS
        )
        locator.wait_for(timeout=5000)
        locator.click(force=True)





