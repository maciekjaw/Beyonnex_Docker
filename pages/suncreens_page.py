from playwright.sync_api import Page

class SunscreensPage:   
    
    product_price_locator = "p:has-text('Price:')"
    price = "Price:"
    price_rs = 'Price: Rs.'
    product_price_rs_locator = "p:has-text('Price:')"
    cheapest_product_locator = "button.btn.btn-primary"
    products_selector = ".text-center.col-4"
    product_name_selector = "p.font-weight-bold"
    SFP50 = 'SPF-50'
    SFP30 = 'SPF-30'

    def __init__(self, page):
        self.page = page
     
    def add_sunscreens_to_card(self, page:Page):
        
        cheapest_price = float('inf')
        cheapest_product = None
        page.wait_for_timeout(2000)

        products = page.query_selector_all(self.products_selector)
        for product in products:
            product_name = product.query_selector(self.product_name_selector).text_content()
            try:
                 product_price = float(product.query_selector(self.product_price_locator).text_content().replace(self.price, ''))
            except:
                 product_price = float(product.query_selector(self.product_price_rs_locator).text_content().replace(self.price_rs, ''))

            if self.SFP50 in product_name and product_price < cheapest_price:
                cheapest_price = product_price
                cheapest_product = product

        if cheapest_product:
            cheapest_product.query_selector(self.cheapest_product_locator).click()
            if self.SFP30 in product_name and product_price < cheapest_price:
                cheapest_price = product_price
                cheapest_product = product

        if cheapest_product:
            cheapest_product.query_selector(self.cheapest_product_locator).click()