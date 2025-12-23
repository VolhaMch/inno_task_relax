from pages.base_page import BasePage

class LunaPage(BasePage):

    PHONE_BUTTON = "//a[@class='Button PersonalHeaderButton Button--big']//span[contains(text(), 'Телефоны')]"
    PHONE_NUMBER = "//span[@class='PhoneLink__number']"
    WORKING_HOURS = "//span[@class='TimeMarker__text']"
    ADDRESS = "//div[@itemprop='address']"
    IGNORE_FONBET = "//div[starts-with(@style, 'background-image')]"


    def click_phone_button(self):
        self.click(self.PHONE_BUTTON)

    def get_phone_number(self) -> str:
        self.wait_for_element(self.PHONE_NUMBER)
        return self.get_text(self.PHONE_NUMBER)

    def get_working_hours(self) -> str:
        self.wait_for_element(self.WORKING_HOURS)
        return self.get_text(self.WORKING_HOURS)

    def get_address(self) -> str:
        self.wait_for_element(self.ADDRESS)
        return self.get_text(self.ADDRESS)

    def get_contact_info(self):
        return {
            "phone": self.get_phone_number(),
            "hours": self.get_working_hours(),
            "address": self.get_address()
        }


    def ignore_fonbet(self):
        locator = self.page.locator(self.IGNORE_FONBET)
        if locator.is_visible():
            locator.click(timeout=10000)





