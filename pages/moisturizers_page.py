from playwright.sync_api import expect
from playwright.sync_api import Page, expect

class MoisturizersPage:   
    
    products_locator = ".text-center.col-4"
    product_name_locator = "p.font-weight-bold"
    product_price_locator = "p:has-text('Price:')"
    price = "Price:"
    price_rs = 'Price: Rs.'
    product_price_rs_locator = "p:has-text('Price:')"
    cheapest_product_locator = "button.btn.btn-primary"
    products_selector = ".text-center.col-4"
    product_name_selector = "p.font-weight-bold"
    aloe = "Aloe"
    almond = "Almond"

    def __init__(self, page):
        self.page = page
    
    def add_moisturizers_to_card(self, page:Page):

        cheapest_price = float('inf')
        cheapest_product = None
        page.wait_for_timeout(1000)
        
        products = page.query_selector_all(self.products_selector)
        for product in products:
            product_name = product.query_selector(self.product_name_selector).text_content()
            try:
                 product_price = float(product.query_selector(self.product_price_locator).text_content().replace(self.price, ''))
            except:
                 product_price = float(product.query_selector(self.product_price_rs_locator).text_content().replace(self.price_rs, ''))

            if self.aloe in product_name and product_price < cheapest_price:
                cheapest_price = product_price
                cheapest_product = product

        if cheapest_product:
            cheapest_product.query_selector(self.cheapest_product_locator).click()

            if self.almond in product_name and product_price < cheapest_price:
                cheapest_price = product_price
                cheapest_product = product

        if cheapest_product:
            page.wait_for_timeout(500)
            cheapest_product.query_selector(self.cheapest_product_locator).click()

