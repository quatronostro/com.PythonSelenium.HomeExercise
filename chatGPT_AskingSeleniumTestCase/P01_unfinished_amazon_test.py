from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Test Case 1:
# Website: www.amazon.com
# Objective: Search for a product, apply filters, and add it to the cart.

# Launch the browser and navigate to www.amazon.com
def launch_browser_navigate_website(url):
    driver.get(url)

# Enter a specific product name in the search bar and search it.
def enter_specific_product_to_search():
    driver.find_element(By.ID, search_bar_id).send_keys("samsung" + Keys.ENTER)

# Apply relevant filters, such as price range or customer ratings.
def apply_filter():
    driver.find_element(By.XPATH, "//*[@id='p_89/SAMSUNG']/span/a/div/label/i").click()
    filter2 = driver.find_element(By.XPATH, "//*[@id='p_n_feature_twelve_browse-bin/14674911011']/span/a/div/label/i")
    wait.until(EC.element_to_be_clickable(filter2))
    filter2.click()

# Select a product from the search results.
def select_product():
    driver.find_element(By.XPATH, "//div[@data-index='7']").click()

# Verify that the product page is displayed.
def verify_page_is_displayed():
    pass

# Add the product to the cart.
def add_product_to_cart():
    pass

# Verify that the product is successfully added to the cart.
def verify():
    pass



if __name__ == '__main__':
    url = "http://www.amazon.com"
    search_bar_id = "twotabsearchtextbox"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    launch_browser_navigate_website(url)
    enter_specific_product_to_search()
    apply_filter()
    select_product()
    verify_page_is_displayed()
    add_product_to_cart()
    verify()



## This code will stop here bc amazon implement some Captcha and we cant pass it. So I will try this case with another website
