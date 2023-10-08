from pages.landing_page import LandingPage
from pages.moisturizers_page import MoisturizersPage
from pages.common_page import Common
from pages.suncreens_page import SunscreensPage
from pages.cart_page import CartPage
from pages.confirmation_page import ConfirmationPage

def test_shopping(page):
    
    landing_page = LandingPage(page=page)
    moisturizers_page = MoisturizersPage(page=page)
    suncreens_page = SunscreensPage(page=page)
    common_page = Common(page=page)
    cart_page = CartPage(page=page)
    confirmation_page = ConfirmationPage(page=page)

    landing_page.go_to_home_page(page=page)
    temperaure = landing_page.get_temperature()

    if temperaure < 19:
        landing_page.go_to_moisturizers_page(page=page)
        moisturizers_page.add_moisturizers_to_card(page=page)
        common_page.get_num_of_items_after_adding_to_cart(page=page)
        common_page.click_cart(page=page)
        cart_page.check_cart_url(page=page)
        cart_page.get_moisturizer_in_cart(page=page)
        cart_page.click_pay_with_card(page=page)
        cart_page.fill_form_with_data_and_pay(page=page)
        confirmation_page.get_success_url(page=page)
        confirmation_page.get_success_payment_info(page=page)


    elif temperaure > 34:
        landing_page.go_to_sunscreen_page(page=page)
        suncreens_page.add_sunscreens_to_card(page=page)
        common_page.get_num_of_items_after_adding_to_cart(page=page)
        common_page.click_cart(page=page)
        cart_page.check_cart_url(page=page)
        cart_page.get_sunscreeners_in_cart(page=page)
        cart_page.click_pay_with_card(page=page)
        cart_page.fill_form_with_data_and_pay(page=page)
        confirmation_page.get_success_url(page=page)
        confirmation_page.get_success_payment_info(page=page)










    