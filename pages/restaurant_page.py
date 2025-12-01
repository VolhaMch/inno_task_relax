from pages.base_page import BasePage

class RestaurantPage(BasePage):

    FILTERS = "//span[text()='Фильтры']"
    REGION = "(//div[@class='Select FilterSidebar__select'])[2]"
    ZAVODSKOI_REGION = "//span[text()='Заводской']"
    TAKEAWAY_FOOD = "(//span[text()='Еда навынос'])[1]"
    CUISINE_MORE = "(//div[@class='CompositeButtons__toggle'])[1]"
    CUISINE_COUNTRY = "//span[text()='{text}']"
    YES_TAKEAWAY_MENU = "(//span[text()='Да'])[1]"
    CLOSE_WRAP = "//span[@class='marquiz-pops__close-wrapper']"
    SHOW_FILTER_RESULTS = "//span[text()='Показать']"

    def choose_region(self, region):
        self.page.click(self.REGION)
        self.page.click(region)

    def choose_takeaway_food(self):
        self.page.click(self.TAKEAWAY_FOOD)

    def choose_cuisine(self, text):
        locator = self.CUISINE_COUNTRY.format(text=text)
        self.page.click(self.CUISINE_MORE)
        self.page.click(locator)

    def choose_takeaway_menu(self):
        self.page.click(self.YES_TAKEAWAY_MENU)

    def close_ads(self):
        self.page.click(self.CLOSE_WRAP)

    def show_filter_results(self):
        self.page.click(self.SHOW_FILTER_RESULTS)