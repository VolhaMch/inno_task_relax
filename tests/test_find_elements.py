import allure
import pytest

from pages.afisha_page import AfishaPage
from pages.luna_page import LunaPage
from pages.movie_page import MoviePage
from pages.restaurant_page import RestaurantPage
from utils.config import LUNA_URL, RESTAURANTS_URL


class TestValidateSearch:

    @allure.title("Validate Luna restaurant contact information")
    @allure.description("Open relax.by, search for Luna, navigate to its page and verify phone, address, and working hours")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("restaurant_name, expected_url", [
        ("Luna", LUNA_URL)
    ])
    def test_luna_contact_info(self, open_main_page, page, restaurant_name, expected_url):
        base_page = open_main_page
        luna_page = LunaPage(page)

        with allure.step("Enter 'Luna' into the search field"):
            base_page.fill_text_in_search_line(restaurant_name)
        with allure.step("Select Luna restaurant page from search results"):
            base_page.choose_luna_page_in_search_line()
        with allure.step("Verify that 'Luna restaurant page' is opened"):
            luna_page.check_page_url(expected_url)
        with allure.step("Close ads"):
            luna_page.ignore_fonbet()
        with allure.step("Click on the phone button to reveal contacts"):
            luna_page.click_phone_button()
        with allure.step("Extract phone, address and working hours of Luna restaurant"):
            info = luna_page.get_contact_info()
            allure.attach(str(info), "Contact Info", allure.attachment_type.TEXT)
        with allure.step("Validate contact info is not empty"):
            assert info["phone"], "Phone is empty"
            assert info["address"], "Address is empty"
            assert info["hours"], "Working hours are empty"


class TestFiltersValidation:

    @allure.title("Navigate to Restaurants and open filters")
    @allure.description("User goes to 'Food' → 'Restaurants' and clicks filters on the restaurants page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("cuisine", ["Белорусская"])

    def test_open_restaurants_filters(self, open_main_page, page, cuisine):
        base_page = open_main_page
        restaurant_page = RestaurantPage(page)

        with allure.step("Navigate to 'Food' section"):
            base_page.open_restaurants_section()
        with allure.step("Choose 'Restaurants' section"):
            restaurant_page.open_filters()
        with allure.step("Verify 'Restaurants' page is opened"):
            base_page.check_page_url(RESTAURANTS_URL)
        with allure.step("Open 'Filters'"):
            restaurant_page.click(RestaurantPage.FILTERS)
        with allure.step("Apply filters for region, takeaway, cuisine and menu"):
            restaurant_page.choose_region(RestaurantPage.ZAVODSKOI_REGION)
            restaurant_page.choose_takeaway_food()
            restaurant_page.choose_cuisine(cuisine)
            restaurant_page.choose_takeaway_menu()
        with allure.step("Close ads"):
            restaurant_page.close_ads()
        with allure.step("Verify filtered results"):
            restaurant_page.show_filter_results()


class TestPosterValidation:

    @allure.title("Navigate to afisha and open film")
    @allure.description("User goes to to Afisha section, open choose one film and check his page is opened")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("card_index", [3])
    def test_choose_afisha_card_category_and_check_feedback(self, open_main_page, page, card_index):
        base_page = open_main_page
        afisha_page = AfishaPage(page)
        movie_page = MoviePage(page)

        with allure.step('Open section "Afisha"'):
            base_page.open_afisha_section()
        with allure.step(f'Select film card at index {card_index}'):
            chosen_film_title = afisha_page.get_item_title(card_index)
            allure.attach(chosen_film_title, "Chosen film title")
            afisha_page.choose_event(card_index)
        with allure.step('Verify the opened movie page matches the chosen film'):
            movie_page.should_be_correct_film(chosen_film_title)
        with allure.step('Check that feedback section is presented'):
            movie_page.should_have_feedback_section()
