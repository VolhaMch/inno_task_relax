import time

import allure
import pytest

from pages.afisha_page import AfishaPage
from pages.restaurants.luna_page import LunaPage
from pages.movie_page import MoviePage
from pages.new_year_page import NewYearPage
from pages.restaurants.restaurant_page import RestaurantPage
from config.config import LUNA_URL, RESTAURANTS_URL


class TestPosterValidation:
    @allure.title("")
    @allure.description("")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_find_place_for_new_year(self, open_main_page, page):
        base_page = open_main_page
        new_year_page = NewYearPage(page)

        with allure.step("Navigate to new year page"):
            base_page.open_new_year_section()
            time.sleep(2)
            new_year_page.ignore_new_year_ads()
            time.sleep(2)
            new_year_page.choose_find_place_for_new_year()
            time.sleep(2)

            # new_year_page.start_find_place_for_new_year()
            # time.sleep(5)
            # new_year_page.chose_destination_corporativ()
            # time.sleep(5)
            #
            # new_year_page.click_next_button()
            # new_year_page.choose_outside_city_place()
            # new_year_page.click_next_button()
            # new_year_page.input_date("31 Декабря")
            # new_year_page.click_next_button()
            # new_year_page.click_next_button()
            # new_year_page.choose_cost_500_more()
            # new_year_page.click_next_button()
            # new_year_page.input_city('Минск')
            # new_year_page.click_next_button()
            # new_year_page.need_show()
            # new_year_page.click_next_button()
            # new_year_page.click_button_last()
            # new_year_page.agreement_page_is_visible()