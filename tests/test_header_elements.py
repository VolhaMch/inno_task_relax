import time

import allure
import pytest

from pages.afisha_page import AfishaPage
from pages.restaurants.luna_page import LunaPage
from pages.movie_page import MoviePage
from pages.new_year_page import NewYearPage
from pages.restaurants.restaurant_page import RestaurantPage
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




class TestNavigationMenu:
    @allure.title("")
    @allure.description("")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("city, url_part",[("Брест", "brest/"),("Волковыск", "volkovysk/"),("Бобруйск", "bobrujsk/")])
    def test_find_place_for_new_year(self, open_main_page, page, city, url_part):
        base_page = open_main_page
        base_page.fill_city(city)
        base_page.url_is_valid(url_part)








