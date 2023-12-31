import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Test Case 1:
# Website: www.hepsiburada.com
# Objective: Search for a product, apply filters, and add it to the cart.

# Launch the browser and navigate to www.hepsiburada.com.
def launch_browser_navigate_website(url):
    driver.get(url)

# Enter a specific product name in the search bar and search it.
def enter_specific_product_to_search():
    driver.find_element(By.ID, cookies_id).click()
    time.sleep(3)

    search_bar = driver.find_element(By.XPATH, search_bar_xpath)
    search_bar.click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("samsung" + Keys.ENTER)

# Apply relevant filters, such as price range or customer ratings.
def apply_filter():
    driver.find_element(By.XPATH, price_range_lowest).send_keys("7000")
    driver.find_element(By.XPATH, price_range_highest).send_keys("15000")
    driver.find_element(By.XPATH, price_search_button).click()

# Select a product from the search results.
def select_product():
    time.sleep(2)
    driver.find_element(By.XPATH, first_product).click()
    all_window_handles = driver.window_handles
    driver.switch_to.window(all_window_handles[1])

# Verify that the product page is displayed.
def verify_page_is_displayed():
    title = driver.title
    assert title.__contains__("Samsung")

# Add the product to the cart.
def add_product_to_cart():
    driver.find_element(By.ID, add_to_cart).click()

# Verify that the product is successfully added to the cart.
def verify():
    verify_element = driver.find_element(By.XPATH, verify_text)
    wait.until(EC.visibility_of(verify_element))

    assert verify_element.is_displayed()

if __name__ == '__main__':
    url = "https://www.hepsiburada.com"
    cookies_id = 'onetrust-accept-btn-handler'
    search_bar_xpath = "//*[@class='sf-OldHeader-MSHyIpigOpMg8jl1slwR']"
    price_range_lowest = "//*[@id='fiyat']/div/div/div/div[1]/div/div[1]/input"
    price_range_highest = "//*[@id='fiyat']/div/div/div/div[1]/div/div[2]/input"
    price_search_button = '//*[@id="fiyat"]/div/div/div/div[1]/button'
    first_product = "//*[@data-test-id='product-card-name'][1]"
    add_to_cart = 'addToCart'
    verify_text = "//span[text()=' Ürün sepetinizde']"

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options)
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
