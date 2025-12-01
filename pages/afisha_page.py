from pages.base_page import BasePage

class AfishaPage(BasePage):
    CINEMA_SECTION_ITEM = "(//div[@class='slick-list draggable'])[2] //li[@data-slick-index='{ITEM}']"
    FILM_NAME = "(//div[@class='slick-list draggable'])[2] //li[@data-slick-index='{ITEM}']//a[@class='b-afisha_blocks-strap_item_lnk_txt link']"


    def choose_event(self, item):
        locator = self.CINEMA_SECTION_ITEM.format(ITEM=item)
        self.page.click(locator)

    def get_item_title(self, item):
        locator_str = self.FILM_NAME.format(ITEM=item)
        locator = self.page.locator(locator_str)
        return locator.text_content()
