from playwright.sync_api import expect

from pages.base_page import BasePage

class MoviePage(BasePage):
    FEEDBACK_SECTION = "//div[@class='send-feedback']"

    def should_be_correct_film(self, expected_title):
        actual_title = self.page.locator("//h1[@itemprop='name']").text_content()
        assert expected_title == actual_title, \
            f"Expected '{expected_title}', but got '{actual_title}'"

    def should_have_feedback_section(self):
        locator = self.page.locator(self.FEEDBACK_SECTION)
        expect(locator).to_be_visible()
        expect(locator).to_be_enabled()