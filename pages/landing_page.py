from playwright.sync_api import expect
from playwright.sync_api import Page, expect

class LandingPage():   
    
    base_page_url:str = "https://weathershopper.pythonanywhere.com/"
    expected_base_page_url:str = base_page_url
    locator_temperature = "#temperature"
    role_button = "button"
    button_moisturizers = "Buy moisturizers"
    button_sunscreens = "Buy sunscreens"
    expected_moisturizers_page:str = "https://weathershopper.pythonanywhere.com/moisturizer"
    expected_sunscreen_page:str = "https://weathershopper.pythonanywhere.com/sunscreen"

    def __init__(self, page):
        self.page = page

    def go_to_home_page(self, page:Page):
        self.page.goto(self.base_page_url)
        expect(page).to_have_url(self.expected_base_page_url)

    def get_temperature(self) -> int:
        temperature = int(self.page.locator(self.locator_temperature).text_content()[:2])
        return temperature
    
    def go_to_moisturizers_page(self, page:Page):
        self.page.get_by_role(role=self.role_button, name=self.button_moisturizers).click()
        expect(page).to_have_url(self.expected_moisturizers_page)

    def go_to_sunscreen_page(self, page:Page):
        self.page.get_by_role(role=self.role_button, name=self.button_sunscreens).click()
        expect(page).to_have_url(self.expected_sunscreen_page)
        

        