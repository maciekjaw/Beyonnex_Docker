from playwright.sync_api import expect
from playwright.sync_api import Page, expect

class ConfirmationPage():   
    
    confirmation_page_url:str = "https://weathershopper.pythonanywhere.com/confirmation"
    success_payment_info = "Your payment was successful. You should receive a follow-up call from our sales team."
    success_message_locator = ".text-justify"

    def __init__(self, page):
        self.page = page
    
    def get_success_url(self, page):
        page.wait_for_timeout(1500)
        expect(page).to_have_url(self.confirmation_page_url)

    def get_success_payment_info(self,page:Page):
        expected_message = page.locator(self.success_message_locator).text_content()
        assert self.success_payment_info == expected_message