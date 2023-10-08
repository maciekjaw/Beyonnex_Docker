from playwright.sync_api import Page

class Common:   
    
    role_button = "button"
    cart_locator = "button:has-text('Cart')"
    expected_num_of_items = "2"

    def __init__(self, page):
        self.page = page

    def click_cart(self, page:Page) -> None:
        page.locator(self.cart_locator).click()

    def get_num_of_items_after_adding_to_cart(self, page:Page) -> None:
        page.wait_for_timeout(1000)
        get_number = page.locator(self.cart_locator).text_content().__contains__(self.expected_num_of_items)
        assert get_number == True

    def wait_until_element_is_loaded(self,time):
        self.page.wait_for_timeout(time)

        