
How to run test?

1. Download repo
2. Execute in terminal in a root folder <docker build -t beyonnex-playwright-docker ./>
3. Execute in terminal in a root folder <docker run beyonnex-playwright-docker pytest >

IMPORTANT:

I believe there is a bug on website. After adding items to a cart When I got to a checout very ofter there is one product on page.
Why i believe this is a bug ? 
Because I always check if there are 2 items in a cart by calling  get_num_of_items_after_adding_to_cart() function. It always returns 2 products.
In order to check it there are 2 items on checout webpage I call this method get_moisturizer_in_cart(self, page:Page) 
or that method  def get_sunscreeners_in_cart(self, page:Page) accordingly. 
A test passes always because I set a condition to check a number of products in a cart and run a test depends on a items number


How to debug?
Please add page.pause() and run code in VSC