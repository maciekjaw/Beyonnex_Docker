from playwright.sync_api import expect
from playwright.sync_api import Page, expect

class CartPage():   
    
    cart_page_url:str = "https://weathershopper.pythonanywhere.com/cart"
    expected_cart_page_url:str = cart_page_url
    role_button = "button"
    table_locator = "table.table-striped tbody tr"
    items_locator = "table.table-striped tbody tr td:first-child"
    pay_with_card :str = "Pay with Card"
    emial = "test@gmail.com"
    SPF30 = "SPF-30"
    SPF50 = "SPF-50"
    aloe = "Aloe"
    almond = "Almond"
    fake_email = "fakeemail@gmail.com"
    tab = "Tab"
    enter = "Enter"
    expiry_date = "0224"
    card_number = "4000 0566 5566 5556"
    ccv_number = "123"
    post_code = "12345"

    def __init__(self, page):
        self.page = page

    def check_cart_url(self, page:Page):
        expect(page).to_have_url(self.expected_cart_page_url)
    
    def click_pay_with_card(self, page:Page):
        page.get_by_role(role=self.role_button, name=self.pay_with_card).click()
    
    def get_moisturizer_in_cart(self, page:Page):
        elements_in_table = page.locator(self.table_locator).count()
        print(elements_in_table)
        get_items = page.locator(self.items_locator).all_text_contents()
        if(elements_in_table == 2):
            assert self.aloe in get_items[0] or get_items[1]
            assert self.almond in get_items[0] or get_items[1]
        else:
            assert self.aloe in get_items[0] or self.almond in get_items[0]

    def get_sunscreeners_in_cart(self, page:Page):
        elements_in_table = page.locator(self.table_locator).count()
        print(elements_in_table)
        get_items = page.locator(self.items_locator).all_text_contents()
        if(elements_in_table == 2):
            assert self.SPF30 in get_items[0] or get_items[1]
            assert self.SPF50 in get_items[0] or get_items[1]
        else:
            assert self.SPF30 in get_items[0] or self.SPF50 in get_items[0]
    

    def fill_form_with_data_and_pay(self, page:Page):
        page.wait_for_timeout(2000)
        page.keyboard.insert_text(self.fake_email)    
        page.keyboard.press(self.tab)
        page.keyboard.insert_text(self.card_number)
        page.keyboard.press(self.tab)
        page.keyboard.insert_text(self.expiry_date)
        page.keyboard.press(self.tab)
        page.keyboard.insert_text(self.ccv_number)
        page.keyboard.press(self.tab)
        page.wait_for_timeout(1000)
        page.keyboard.insert_text(self.post_code)
        page.keyboard.press(self.tab)
        page.keyboard.press(self.enter)


        






        
